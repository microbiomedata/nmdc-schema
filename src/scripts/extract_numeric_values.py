#!/usr/bin/env python3

import re
import yaml
import sys
from pathlib import Path

def extract_numeric_from_raw_value(raw_value):
    """Extract numeric value from has_raw_value string."""
    if not raw_value or raw_value == "xxx":
        return None
    
    # Handle special cases
    if raw_value == "0.417361111":  # carb_nitro_ratio
        return 0.417361111
    if raw_value == "2%":  # tot_org_carb
        return 2
    if raw_value == "35":  # max_occup
        return 35
    if raw_value == "3":  # number_pets/number_resident
        return 3
    if raw_value == "4":  # number_plants
        return 4
    
    # Try to extract first number from the string
    # Look for patterns like "50 milligram per liter", "0.005 mole per liter", etc.
    number_patterns = [
        r'^([0-9]*\.?[0-9]+(?:[eE][+-]?[0-9]+)?)',  # Scientific notation and decimals
        r'([0-9]*\.?[0-9]+)',  # Regular decimals
    ]
    
    for pattern in number_patterns:
        match = re.search(pattern, raw_value)
        if match:
            try:
                return float(match.group(1))
            except ValueError:
                continue
    
    return None

def main():
    # Read the YAML file
    yaml_file = Path("../data/valid/Biosample-possibly-exhaustive.yaml")
    
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)
    
    # Fields that need has_numeric_value extracted from TSV analysis
    fields_to_update = [
        # Fields with parseable numeric values in has_raw_value
        "alkalinity",  # "50 milligram per liter" -> 50
        "alkyl_diethers",  # "0.005 mole per liter" -> 0.005
        "alt",  # "100 meter" -> 100
        "aminopept_act",  # "0.269 mole per liter per hour" -> 0.269
        "ammonium",  # "1.5 milligram per liter" -> 1.5
        "annual_temp",  # "12.5 degree Celsius" -> 12.5
        "bishomohopanol",  # "14 microgram per liter" -> 14
        "bromide",  # "0.05 parts per million" -> 0.05
        "calcium",  # "0.2 micromole per liter" -> 0.2
        "carb_nitro_ratio",  # "0.417361111" -> 0.417361111
        "chloride",  # "5000 milligram per liter" -> 5000
        "chlorophyll",  # "5 milligram per cubic meter" -> 5
        "density",  # "1000 kilogram per cubic meter" -> 1000
        "diss_carb_dioxide",  # "5 milligram per liter" -> 5
        "diss_hydrogen",  # "0.3 micromole per liter" -> 0.3
        "diss_inorg_carb",  # "2059 micromole per kilogram" -> 2059
        "diss_inorg_phosp",  # "56.5 micromole per liter" -> 56.5
        "diss_org_carb",  # "197 micromole per liter" -> 197
        "diss_org_nitro",  # "0.05 micromole per liter" -> 0.05
        "diss_oxygen",  # "175 micromole per kilogram" -> 175
        "glucosidase_act",  # "5 mol per liter per hour" -> 5
        "lbc_thirty",  # "543 mg/kg" -> 543
        "lbceq",  # "1575 mg/kg" -> 1575
        "magnesium",  # "52.8 micromole per kilogram" -> 52.8
        "manganese",  # "24.7 mg/kg" -> 24.7
        "max_occup",  # "35" -> 35
        "mean_frict_vel",  # "0.5 meter per second" -> 0.5
        "mean_peak_frict_vel",  # "1 meter per second" -> 1
        "nitrate",  # "65 micromole per liter" -> 65
        "nitrite",  # "0.5 micromole per liter" -> 0.5
        "nitrite_nitrogen",  # "1.2 mg/kg" -> 1.2
        "number_pets",  # "3" -> 3
        "number_plants",  # "4" -> 4
        "number_resident",  # "3" -> 3
        "org_matter",  # "1.75 milligram per cubic meter" -> 1.75
        "org_nitro",  # "4 micromole per liter" -> 4
        "part_org_carb",  # "1.92 micromole per liter" -> 1.92
        "petroleum_hydrocarb",  # "0.05 micromole per liter" -> 0.05
        "phosphate",  # "0.7 micromole per liter" -> 0.7
        "potassium",  # "463 milligram per liter" -> 463
        "pressure",  # "50 atmosphere" -> 50
        "redox_potential",  # "300 millivolt" -> 300
        "samp_store_temp",  # "-80 degree Celsius" -> -80
        "season_precpt",  # "75 millimeters" -> 75
        "season_temp",  # "18 degree Celsius" -> 18
        "size_frac_low",  # "0.2 micrometer" -> 0.2
        "size_frac_up",  # "20 micrometer" -> 20
        "sodium",  # "10.5 milligram per liter" -> 10.5
        "sulfate",  # "5 micromole per liter" -> 5
        "sulfide",  # "2 micromole per liter" -> 2
        "temp",  # "25 degree Celsius" -> 25
        "tot_depth_water_col",  # "500 meter" -> 500
        "tot_diss_nitro",  # "40 microgram per liter" -> 40
        "tot_nitro_content",  # "35 milligrams Nitrogen per kilogram of soil" -> 35
        "tot_org_carb",  # "2%" -> 2
        "tot_phosp",  # "0.03 milligram per liter" -> 0.03
    ]
    
    updates_made = 0
    
    for field_name in fields_to_update:
        if field_name in data:
            field_data = data[field_name]
            if isinstance(field_data, dict) and field_data.get('type') == 'nmdc:QuantityValue':
                raw_value = field_data.get('has_raw_value')
                if raw_value and not field_data.get('has_numeric_value'):
                    numeric_value = extract_numeric_from_raw_value(raw_value)
                    if numeric_value is not None:
                        field_data['has_numeric_value'] = numeric_value
                        updates_made += 1
                        print(f"Updated {field_name}: {raw_value} -> {numeric_value}")
    
    # Write back the updated YAML
    if updates_made > 0:
        with open(yaml_file, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)
        print(f"\nUpdated {updates_made} fields with has_numeric_value")
    else:
        print("No updates needed")

if __name__ == "__main__":
    main()