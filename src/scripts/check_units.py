#!/usr/bin/env python3
"""
UCUM Unit Validator

This script validates has_unit values from quantity_values.tsv against the UOM website
to identify invalid UCUM codes. It handles UCUM format conversion, annotation cleaning,
and provides comprehensive validation reporting.

Author: Generated with Claude Code
"""

import csv
import re
import sys
import time
import urllib.parse
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import requests


class ValidationStatus(Enum):
    """Status of unit validation."""
    VALID = "valid"
    INVALID = "invalid"
    SKIPPED = "skipped"
    ERROR = "error"


@dataclass
class ValidationResult:
    """Result of unit validation."""
    unit: str
    status: ValidationStatus
    message: str
    cleaned_unit: Optional[str] = None
    ucum_format: Optional[str] = None


@dataclass
class ValidationSummary:
    """Summary of validation results."""
    total_units: int
    valid_units: List[ValidationResult]
    invalid_units: List[ValidationResult]
    skipped_units: List[ValidationResult]
    error_units: List[ValidationResult]
    
    @property
    def success_rate(self) -> float:
        """Calculate success rate (valid + skipped / total)."""
        if self.total_units == 0:
            return 0.0
        return (len(self.valid_units) + len(self.skipped_units)) / self.total_units * 100


class UCUMValidator:
    """Validator for UCUM units using the UOM website."""
    
    BASE_URL = "https://units-of-measurement.org"
    REQUEST_DELAY = 0.5  # seconds
    REQUEST_TIMEOUT = 10  # seconds
    
    # Units that should be skipped (special cases)
    SKIP_UNITS = {'1', 'mm[Hg]'}
    
    def __init__(self, delay: float = REQUEST_DELAY, timeout: float = REQUEST_TIMEOUT):
        """Initialize validator with optional custom delay and timeout."""
        self.delay = delay
        self.timeout = timeout
    
    def extract_unique_units(self, tsv_file: Path) -> Set[str]:
        """Extract unique has_unit values from the TSV file."""
        unique_units = set()
        
        try:
            with open(tsv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter='\t')
                for row in reader:
                    unit = row.get('has_unit', '').strip()
                    if unit:  # Skip empty units
                        unique_units.add(unit)
        except KeyError as e:
            raise ValueError(f"Missing required column in TSV file: {e}")
        
        return unique_units
    
    def convert_to_ucum_format(self, unit: str) -> str:
        """
        Convert units with division (/) to UCUM format using multiplication (.) and inverse (-1).
        Also handle exponents properly (e.g., m3 -> m^3, so 1/m3 -> m-3).
        
        Examples:
            'g/g' -> 'g.g-1'
            'mg/L' -> 'mg.L-1'
            'mol/L/h' -> 'mol.L-1.h-1'
            'g/m3' -> 'g.m-3'
            'kW/m2' -> 'kW.m-2'
        """
        if '/' not in unit:
            return unit
        
        # Split on '/' and process each part
        parts = unit.split('/')
        
        # First part stays as is
        result = parts[0]
        
        # Subsequent parts get converted with proper exponent handling
        for part in parts[1:]:
            # Check if the part ends with a number (indicating an exponent)
            match = re.match(r'^([a-zA-Z\[\]\']+)(\d+)$', part)
            if match:
                base_unit = match.group(1)
                exponent = match.group(2)
                # For division, we negate the exponent
                result += f'.{base_unit}-{exponent}'
            else:
                # No exponent, just add -1
                result += f'.{part}-1'
        
        return result
    
    def clean_unit_for_checking(self, unit: str) -> Tuple[str, bool]:
        """
        Clean a unit for UCUM checking by removing curly bracket annotations.
        
        Returns:
            tuple: (cleaned_unit, should_skip)
                - cleaned_unit: unit with curly bracket portions removed
                - should_skip: True if the unit should be skipped entirely
        """
        # Skip these specific units
        if unit in self.SKIP_UNITS:
            return unit, True
        
        # Remove anything in curly brackets (annotations)
        cleaned = re.sub(r'\{[^}]*\}', '', unit)
        
        # If nothing is left after removing annotations, skip it
        if not cleaned.strip():
            return unit, True
        
        return cleaned.strip(), False
    
    def validate_unit_with_uom(self, unit: str) -> ValidationResult:
        """
        Validate a single unit against the UOM website.
        
        Args:
            unit: The unit string to validate
            
        Returns:
            ValidationResult with status and details
        """
        # Clean the unit and check if it should be skipped
        cleaned_unit, should_skip = self.clean_unit_for_checking(unit)
        
        if should_skip:
            return ValidationResult(
                unit=unit,
                status=ValidationStatus.SKIPPED,
                message="Skipped (dimensionless or custom unit)",
                cleaned_unit=cleaned_unit if cleaned_unit != unit else None
            )
        
        # Convert to UCUM format for units with division
        ucum_unit = self.convert_to_ucum_format(cleaned_unit)
        
        # Percent encode the unit for URL
        encoded_unit = urllib.parse.quote(ucum_unit, safe='')
        url = f"{self.BASE_URL}/{encoded_unit}"
        
        try:
            # Add a small delay to be respectful to the server
            time.sleep(self.delay)
            
            response = requests.get(url, timeout=self.timeout)
            response_text = response.text
            
            # Check for the error message indicating invalid UCUM code
            if "Oops!" in response_text and "is not a valid UCUM code" in response_text:
                return ValidationResult(
                    unit=unit,
                    status=ValidationStatus.INVALID,
                    message="Invalid UCUM code",
                    cleaned_unit=cleaned_unit if cleaned_unit != unit else None,
                    ucum_format=ucum_unit if ucum_unit != cleaned_unit else None
                )
            elif response.status_code == 200:
                return ValidationResult(
                    unit=unit,
                    status=ValidationStatus.VALID,
                    message=url,
                    cleaned_unit=cleaned_unit if cleaned_unit != unit else None,
                    ucum_format=ucum_unit if ucum_unit != cleaned_unit else None
                )
            else:
                return ValidationResult(
                    unit=unit,
                    status=ValidationStatus.ERROR,
                    message=f"HTTP {response.status_code}",
                    cleaned_unit=cleaned_unit if cleaned_unit != unit else None,
                    ucum_format=ucum_unit if ucum_unit != cleaned_unit else None
                )
                
        except requests.RequestException as e:
            return ValidationResult(
                unit=unit,
                status=ValidationStatus.ERROR,
                message=f"Request failed: {str(e)}",
                cleaned_unit=cleaned_unit if cleaned_unit != unit else None,
                ucum_format=ucum_unit if ucum_unit != cleaned_unit else None
            )
    
    def validate_units(self, units: Set[str], verbose: bool = True) -> ValidationSummary:
        """
        Validate a set of units and return comprehensive results.
        
        Args:
            units: Set of unit strings to validate
            verbose: Whether to print progress information
            
        Returns:
            ValidationSummary with all results
        """
        if verbose:
            print(f"Found {len(units)} unique has_unit values")
            print("\\nUnique units:")
            for unit in sorted(units):
                print(f"  '{unit}'")
            
            print(f"\\nChecking validity of {len(units)} units against UOM website...")
            print("(This may take a while due to rate limiting)")
        
        valid_units = []
        invalid_units = []
        error_units = []
        skipped_units = []
        
        for i, unit in enumerate(sorted(units), 1):
            result = self.validate_unit_with_uom(unit)
            
            if verbose:
                # Show the cleaning process if applicable
                display_parts = []
                if result.cleaned_unit:
                    display_parts.append(f"cleaned to '{result.cleaned_unit}'")
                if result.ucum_format:
                    display_parts.append(f"UCUM format '{result.ucum_format}'")
                
                if display_parts:
                    display_str = " (" + ", ".join(display_parts) + ")"
                    print(f"[{i}/{len(units)}] Checking '{unit}'{display_str}...")
                else:
                    print(f"[{i}/{len(units)}] Checking '{unit}'...")
            
            # Categorize results
            if result.status == ValidationStatus.VALID:
                valid_units.append(result)
                if verbose:
                    print(f"  ✓ Valid: {result.message}")
            elif result.status == ValidationStatus.INVALID:
                invalid_units.append(result)
                if verbose:
                    print(f"  ✗ Invalid: {result.message}")
            elif result.status == ValidationStatus.SKIPPED:
                skipped_units.append(result)
                if verbose:
                    print(f"  - Skipped: {result.unit}")
            else:  # ERROR
                error_units.append(result)
                if verbose:
                    print(f"  ? Error: {result.message}")
        
        return ValidationSummary(
            total_units=len(units),
            valid_units=valid_units,
            invalid_units=invalid_units,
            skipped_units=skipped_units,
            error_units=error_units
        )


class ReportGenerator:
    """Generate validation reports."""
    
    @staticmethod
    def print_summary_report(summary: ValidationSummary) -> None:
        """Print a comprehensive summary report."""
        print(f"\\n{'='*60}")
        print("SUMMARY REPORT")
        print(f"{'='*60}")
        print(f"Total units found: {summary.total_units}")
        print(f"Valid units: {len(summary.valid_units)}")
        print(f"Invalid units: {len(summary.invalid_units)}")
        print(f"Error/Unable to check: {len(summary.error_units)}")
        print(f"Skipped units: {len(summary.skipped_units)}")
        print(f"Success rate: {summary.success_rate:.1f}%")
        
        if summary.skipped_units:
            print(f"\\n{'='*60}")
            print("SKIPPED UNITS:")
            print(f"{'='*60}")
            for result in summary.skipped_units:
                print(f"  '{result.unit}' - {result.message}")
        
        if summary.invalid_units:
            print(f"\\n{'='*60}")
            print("INVALID UCUM CODES FOUND:")
            print(f"{'='*60}")
            for result in summary.invalid_units:
                print(f"  '{result.unit}' - {result.message}")
        
        if summary.error_units:
            print(f"\\n{'='*60}")
            print("UNITS WITH ERRORS (unable to verify):")
            print(f"{'='*60}")
            for result in summary.error_units:
                print(f"  '{result.unit}' - {result.message}")
        
        if summary.valid_units:
            print(f"\\n{'='*60}")
            print("VALID UCUM CODES:")
            print(f"{'='*60}")
            for result in summary.valid_units:
                print(f"  '{result.unit}' - {result.message}")
    
    @staticmethod
    def save_csv_report(summary: ValidationSummary, output_file: Path) -> None:
        """Save validation results to a CSV file."""
        all_results = (
            summary.valid_units + 
            summary.invalid_units + 
            summary.skipped_units + 
            summary.error_units
        )
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['unit', 'status', 'message', 'cleaned_unit', 'ucum_format'])
            
            for result in all_results:
                writer.writerow([
                    result.unit,
                    result.status.value,
                    result.message,
                    result.cleaned_unit or '',
                    result.ucum_format or ''
                ])


def main() -> None:
    """Main entry point."""
    tsv_file = Path('../../quantity_values.tsv')
    
    try:
        # Initialize validator
        validator = UCUMValidator()
        
        # Extract unique units from TSV file
        unique_units = validator.extract_unique_units(tsv_file)
        
        # Validate units
        summary = validator.validate_units(unique_units, verbose=True)
        
        # Generate report
        ReportGenerator.print_summary_report(summary)
        
        # Optionally save CSV report
        # ReportGenerator.save_csv_report(summary, Path('validation_results.csv'))
        
    except FileNotFoundError:
        print(f"Error: File {tsv_file} not found", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()