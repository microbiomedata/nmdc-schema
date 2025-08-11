#!/usr/bin/env node

// UnitEnum UCUM Compliance Checker
// Validates all UnitEnum permissible_values against UCUM standard using UCUM-LHC

const fs = require('fs');
const yaml = require('js-yaml');
const ucum = require('@lhncbc/ucum-lhc');

// Known false positives - units that are valid UCUM but flagged as invalid by this library version
// The UCUM-LHC library uses UCUM essence file from Jan 4, 2019
// Official UCUM has been updated since then, causing these false positives:
const KNOWN_FALSE_POSITIVES = {
  '[NTU]': 'Added to official UCUM on Aug 29, 2019 (commit b2e20a0), after library\'s last update'
};

const utils = ucum.UcumLhcUtils.getInstance();

// Function to extract all unit keys from UnitEnum
function extractUnitKeys(yamlFilePath) {
  try {
    const fileContents = fs.readFileSync(yamlFilePath, 'utf8');
    const data = yaml.load(fileContents);
    
    // Navigate to UnitEnum permissible_values
    const unitEnum = data.enums?.UnitEnum?.permissible_values;
    
    if (!unitEnum) {
      console.error('Could not find UnitEnum.permissible_values in the YAML file');
      return [];
    }
    
    // Extract all the keys (unit codes)
    const unitKeys = Object.keys(unitEnum);
    console.log(`Found ${unitKeys.length} units in UnitEnum`);
    
    return unitKeys;
  } catch (error) {
    console.error('Error reading or parsing YAML file:', error.message);
    return [];
  }
}

// Function to validate a single unit
function validateUnit(unit) {
  try {
    const validation = utils.validateUnitString(unit);
    return {
      unit: unit,
      valid: validation.status === 'valid',
      status: validation.status,
      name: validation.unit?.name || '',
      guidance: validation.unit?.guidance || '',
      messages: validation.msg || []
    };
  } catch (error) {
    return {
      unit: unit,
      valid: false,
      status: 'error',
      name: '',
      guidance: '',
      messages: [error.message]
    };
  }
}

// Main validation function
function validateAllUnits(yamlFilePath) {
  console.log('UCUM Unit Validation - All UnitEnum Values');
  console.log('==========================================\n');
  
  const unitKeys = extractUnitKeys(yamlFilePath);
  
  if (unitKeys.length === 0) {
    console.log('No units found to validate.');
    return;
  }
  
  console.log(`Validating ${unitKeys.length} units...\n`);
  
  const results = unitKeys.map(validateUnit);
  
  // Sort results: valid first, then invalid
  results.sort((a, b) => {
    if (a.valid && !b.valid) return -1;
    if (!a.valid && b.valid) return 1;
    return a.unit.localeCompare(b.unit);
  });
  
  // Display results
  let validCount = 0;
  let invalidCount = 0;
  const invalidUnits = [];
  
  console.log('VALID UNITS:');
  console.log('============');
  results.forEach(result => {
    if (result.valid) {
      console.log(`✅ "${result.unit}" → ${result.name}`);
      validCount++;
    }
  });
  
  console.log('\nINVALID UNITS:');
  console.log('==============');
  const actuallyInvalidUnits = [];
  const falsePositiveUnits = [];
  
  results.forEach(result => {
    if (!result.valid) {
      const isFalsePositive = KNOWN_FALSE_POSITIVES[result.unit];
      if (isFalsePositive) {
        console.log(`⚠️  "${result.unit}" (FALSE POSITIVE)`);
        console.log(`   Status: ${result.status}`);
        console.log(`   Note: ${isFalsePositive}`);
        falsePositiveUnits.push(result.unit);
      } else {
        console.log(`❌ "${result.unit}"`);
        console.log(`   Status: ${result.status}`);
        if (result.messages.length > 0) {
          console.log(`   Messages: ${result.messages.join(', ')}`);
        }
        actuallyInvalidUnits.push(result.unit);
      }
      console.log('');
      invalidCount++;
      invalidUnits.push(result.unit);
    }
  });
  
  // Summary
  console.log('='.repeat(60));
  console.log(`SUMMARY: ${validCount} valid, ${actuallyInvalidUnits.length} actually invalid, ${falsePositiveUnits.length} false positives`);
  console.log(`True compliance: ${((validCount + falsePositiveUnits.length) / results.length * 100).toFixed(1)}%`);
  console.log(`Library compliance: ${((validCount / results.length) * 100).toFixed(1)}%`);
  
  if (actuallyInvalidUnits.length > 0) {
    console.log('\nUnits that need attention:');
    actuallyInvalidUnits.forEach(unit => console.log(`  - "${unit}"`));
    
    console.log('\nRecommendations:');
    console.log('- Consider replacing invalid units with UCUM-compliant alternatives');
    console.log('- Check https://ucum.org for valid unit expressions');
  }
  
  if (falsePositiveUnits.length > 0) {
    console.log('\nFalse positives (valid in current UCUM but library is outdated):');
    falsePositiveUnits.forEach(unit => console.log(`  - "${unit}"`));
  }
  
  // Ensure local directory exists (relative to project root)
  const localDir = '../../local';
  if (!fs.existsSync(localDir)) {
    fs.mkdirSync(localDir, { recursive: true });
  }
  
  // Write invalid units to text file
  const invalidUnitsFile = `${localDir}/invalid_unitenum_units.txt`;
  const invalidContent = invalidUnits.length > 0 
    ? `# Invalid UnitEnum units that don't comply with UCUM\n# Generated: ${new Date().toISOString()}\n\n${invalidUnits.join('\n')}\n`
    : `# All UnitEnum units are UCUM compliant\n# Generated: ${new Date().toISOString()}\n`;
  
  fs.writeFileSync(invalidUnitsFile, invalidContent);
  console.log(`\nInvalid units written to: ${invalidUnitsFile}`);
  
  // Export detailed results to JSON
  const resultsFile = `${localDir}/unitenum_ucum_validation_results.json`;
  fs.writeFileSync(resultsFile, JSON.stringify({
    timestamp: new Date().toISOString(),
    summary: {
      total: results.length,
      valid: validCount,
      invalid: invalidCount,
      compliance: ((validCount / results.length) * 100).toFixed(1) + '%'
    },
    results: results
  }, null, 2));
  
  console.log(`Detailed results exported to: ${resultsFile}`);
}

// Command line usage
if (require.main === module) {
  const yamlFilePath = process.argv[2];
  
  if (!yamlFilePath) {
    console.error('Error: File path is required');
    console.log('Usage: node check_unitenum_ucum_compliance.js <path_to_attribute_values.yaml>');
    process.exit(1);
  }
  
  if (!fs.existsSync(yamlFilePath)) {
    console.error(`Error: File ${yamlFilePath} not found`);
    console.log('Usage: node check_unitenum_ucum_compliance.js <path_to_attribute_values.yaml>');
    process.exit(1);
  }
  
  validateAllUnits(yamlFilePath);
}

module.exports = { validateAllUnits, extractUnitKeys, validateUnit };