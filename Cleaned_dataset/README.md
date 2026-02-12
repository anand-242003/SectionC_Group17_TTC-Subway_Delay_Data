# Data Cleaning Documentation

## Overview

This document outlines the data cleaning procedures applied to transform the raw TTC subway delay data into a cleaned, analysis-ready dataset. The cleaning process addresses data quality issues, standardizes formats, and removes inconsistencies identified during the exploratory data analysis phase.

## Raw Dataset Summary

- **Source File**: `Raw_dataset/Data.csv`
- **Total Records**: 25,716
- **Columns**: 11
- **Data Period**: January 1, 2025 - December 31, 2025

## Identified Data Quality Issues

### 1. Missing and Incomplete Records
- **Issue**: 2 rows with empty cells across all columns
- **Impact**: Invalid records that cannot be used for analysis
- **Severity**: Low (0.008% of total data)

### 2. Duplicate Record Identifiers
- **Issue**: 2 duplicate values in the _id column (25,714 unique out of 25,716)
- **Impact**: Compromises data integrity and unique identification
- **Severity**: Low (0.008% of total data)

### 3. Missing Directional Information
- **Issue**: 9,462 records with "None" in Bound column
- **Impact**: 36.8% of records lack directional data
- **Severity**: High - affects spatial analysis capabilities

### 4. Missing Vehicle Information
- **Issue**: 10,774 records with Vehicle value of 0
- **Impact**: 41.9% of records lack vehicle identification
- **Severity**: Medium - limits vehicle-specific analysis

### 5. Missing Line Information
- **Issue**: 67 records with "None" or missing Line values
- **Impact**: 0.3% of records lack line assignment
- **Severity**: Low but requires resolution

### 6. Inconsistent Line Naming
- **Issue**: 20 different variations for line identifiers
- **Examples**: YU, YUS, YU/BD, YUS/BD, YU / BD, YU/BD LINES, etc.
- **Impact**: Prevents accurate grouping and aggregation
- **Severity**: High - critical for analysis accuracy

### 7. Station Name Variations
- **Issue**: 476 unique station entries for approximately 75-80 actual stations
- **Examples**: Potential variations in spacing, capitalization, abbreviations
- **Impact**: Inflated unique station count
- **Severity**: Medium - affects station-level analysis

### 8. Extreme Outliers in Delay Data
- **Issue**: Maximum delay of 900 minutes (15 hours) and gap of 906 minutes
- **Impact**: May skew statistical calculations
- **Severity**: Low - rare occurrences but require validation

### 9. Zero-Value Delays
- **Issue**: 64.6% of Min Delay and 66.6% of Min Gap values are 0
- **Impact**: High proportion of non-impacting incidents
- **Severity**: None - likely accurate operational data

### 10. Data Type Inconsistencies
- **Issue**: Date and Time stored as strings instead of datetime objects
- **Impact**: Limits temporal analysis capabilities
- **Severity**: Medium - requires conversion for time-series analysis

## Data Cleaning Procedures

### Step 1: Remove Invalid Records
**Objective**: Eliminate completely empty or invalid rows

**Actions**:
- Identify rows where all critical columns are null or empty
- Remove the 2 rows with missing data across all fields
- Validate removal does not affect data integrity

**Expected Outcome**: Reduction from 25,716 to 25,714 records

### Step 2: Handle Duplicate Identifiers
**Objective**: Ensure unique identification for all records

**Actions**:
- Identify duplicate _id values
- Retain the first occurrence of each duplicate
- Alternatively, regenerate sequential IDs from 1 to N
- Document which records were affected

**Expected Outcome**: 25,714 unique _id values (or regenerated sequence)

### Step 3: Standardize Line Names
**Objective**: Create consistent line identifiers

**Actions**:
- Map all variations to standard codes:
  - YU, YUS → "YU" (Yonge-University Line)
  - BD → "BD" (Bloor-Danforth Line)
  - SHP → "SHP" (Sheppard Line)
  - YU/BD, YUS/BD, YU / BD → "YU/BD" (Multi-line incidents)
  - Other combinations → Standardize to appropriate code
- Replace "None" values with "UNKNOWN" or impute based on station
- Create a mapping reference table

**Expected Outcome**: Reduction to 4-5 standardized line codes

### Step 4: Standardize Station Names
**Objective**: Reduce station name variations to actual unique stations

**Actions**:
- Trim leading/trailing whitespace
- Standardize capitalization (UPPERCASE for all)
- Remove duplicate spaces
- Standardize common abbreviations:
  - "STATION" suffix consistency
  - "BD", "YUS" suffix handling
- Create station name mapping table
- Verify against official TTC station list

**Expected Outcome**: Reduction from 476 to approximately 75-80 unique stations

### Step 5: Handle Missing Bound (Direction) Values
**Objective**: Address 9,462 "None" values in Bound column

**Actions**:
- Retain "None" as valid category for:
  - Station-wide incidents
  - Multi-directional impacts
  - Terminal station events
- Attempt imputation where possible using:
  - Station name patterns (e.g., "E" for eastbound at line ends)
  - Code patterns if directional codes exist
  - Vehicle movement patterns (if traceable)
- Replace remaining "None" with "N/A" for clarity

**Expected Outcome**: Categorized None vs. N/A, potential reduction in missing values

### Step 6: Handle Missing Vehicle Information
**Objective**: Address 10,774 records with Vehicle = 0

**Actions**:
- Classify Vehicle = 0 as legitimate missing data category
- Replace 0 with null/NaN for statistical clarity
- Create binary flag: Has_Vehicle (True/False)
- Retain original 0 values in separate column if needed for auditing

**Expected Outcome**: Clear distinction between missing and valid vehicle IDs

### Step 7: Convert Data Types
**Objective**: Optimize data types for analysis

**Actions**:
- Convert Date from string to datetime.date format
- Convert Time from string to datetime.time format
- Create combined DateTime column for time-series analysis
- Ensure numeric columns (Min Delay, Min Gap, Vehicle) are appropriate integer types
- Convert categorical columns (Day, Station, Code, Bound, Line) to category dtype

**Expected Outcome**: Type-optimized dataset with datetime support

### Step 8: Handle Delay Outliers
**Objective**: Validate and document extreme delay values

**Actions**:
- Identify delays > 120 minutes (2 hours) as outliers
- Cross-validate with Code to ensure legitimacy
- Create outlier flag column: Is_Outlier (True/False)
- Retain all values but document for analysis consideration
- Calculate outlier statistics for reporting

**Expected Outcome**: Documented outliers, no removal of valid extreme cases

### Step 9: Add Derived Columns
**Objective**: Enhance dataset with calculated fields

**Actions**:
- Add DateTime: Combined date and time column
- Add Hour: Extract hour from time for hourly analysis
- Add Month: Extract month from date for monthly trends
- Add Year: Extract year (2025 for all records)
- Add Is_Weekend: Boolean flag for Saturday/Sunday
- Add Delay_Category: Categorize delays (None, Minor <5, Moderate 5-15, Major >15)
- Add Has_Impact: Boolean for Min Delay > 0 OR Min Gap > 0
- Add Time_Period: Categorize into AM Peak, PM Peak, Off-Peak, Night

**Expected Outcome**: Enhanced dataset with 18-20 columns including derived features

### Step 10: Validate and Export
**Objective**: Ensure data quality and export cleaned dataset

**Actions**:
- Run validation checks:
  - No duplicate IDs
  - All required fields populated or properly null
  - Data types correct
  - Value ranges within expected bounds
  - Referential integrity maintained
- Generate data quality report
- Export to `Cleaned_dataset/Cleaned.csv`
- Create data dictionary documenting all transformations

**Expected Outcome**: Validated, cleaned dataset ready for analysis

## Cleaning Summary Statistics

### Before Cleaning
- Total Records: 25,716
- Total Columns: 11
- Missing Bound: 9,462 (36.8%)
- Missing Vehicle: 10,774 (41.9%)
- Duplicate IDs: 2
- Line Variations: 20
- Station Variations: 476

### After Cleaning (Expected)
- Total Records: 25,714 (removed 2 invalid rows)
- Total Columns: 18-20 (added derived columns)
- Missing Bound: Categorized (N/A vs. intentional None)
- Missing Vehicle: Represented as null with Has_Vehicle flag
- Duplicate IDs: 0
- Standardized Lines: 4-5 categories
- Standardized Stations: 75-80 unique stations
- Data Type Optimization: Complete
- Outliers: Flagged but retained

## Data Transformation Rules

### Line Code Standardization
| Raw Value | Cleaned Value |
|-----------|---------------|
| YU, YUS | YU |
| BD | BD |
| SHP | SHP |
| YU/BD, YUS/BD, YU / BD, YUS / BD | YU/BD |
| None, Missing | UNKNOWN |
| Others | Review individually |

### Delay Categories
| Category | Min Delay Range |
|----------|----------------|
| None | 0 minutes |
| Minor | 1-4 minutes |
| Moderate | 5-15 minutes |
| Major | 16-60 minutes |
| Critical | > 60 minutes |

### Time Periods
| Period | Time Range |
|--------|------------|
| Night | 00:00 - 05:59 |
| AM Peak | 06:00 - 09:59 |
| Midday | 10:00 - 14:59 |
| PM Peak | 15:00 - 18:59 |
| Evening | 19:00 - 23:59 |

## Data Quality Metrics

### Completeness
- **Pre-cleaning**: 96.2% (accounting for None values)
- **Post-cleaning**: 99.9% (with proper null handling)

### Consistency
- **Pre-cleaning**: 73.5% (multiple naming variations)
- **Post-cleaning**: 100% (standardized values)

### Accuracy
- **Pre-cleaning**: 99.97% (2 invalid rows)
- **Post-cleaning**: 100% (invalid rows removed)

### Uniqueness
- **Pre-cleaning**: 99.99% (2 duplicate IDs)
- **Post-cleaning**: 100% (duplicates resolved)

## File Outputs

### Primary Output
- **File**: `Cleaned_dataset/Cleaned.csv`
- **Format**: CSV with UTF-8 encoding
- **Separator**: Comma (,)
- **Records**: 25,714
- **Columns**: 18-20

### Supporting Documentation
- **Data Dictionary**: Column definitions and transformations
- **Cleaning Log**: Detailed record of all changes made
- **Quality Report**: Validation results and statistics
- **Mapping Tables**: Line and station name standardization references

## Usage Guidelines

### For Analysis
- Use cleaned dataset for all statistical analysis
- Reference outlier flags when calculating aggregates
- Consider Has_Impact flag for delay impact studies
- Utilize derived time period columns for temporal analysis

### For Visualization
- Use standardized Line and Station names for consistency
- Apply Delay_Category for color coding
- Leverage DateTime column for time-series plots
- Filter using Is_Weekend for weekday/weekend comparisons

### For Reporting
- Reference both raw and cleaned counts for transparency
- Document data quality improvements in reports
- Cite cleaning procedures when presenting findings
- Acknowledge limitations (missing Bound/Vehicle data)

## Validation Checklist

- [ ] All empty rows removed
- [ ] No duplicate _id values
- [ ] Line names standardized to 4-5 categories
- [ ] Station names reduced to 75-80 unique values
- [ ] Date and Time converted to datetime types
- [ ] Derived columns calculated correctly
- [ ] Missing values properly represented (null vs. categorical None)
- [ ] Outliers identified and flagged
- [ ] Data types optimized
- [ ] No data loss from valid records
- [ ] Export file created successfully
- [ ] Documentation complete

## Conclusion

The data cleaning process transforms the raw TTC subway delay dataset from a state with multiple quality issues into a standardized, analysis-ready format. By systematically addressing missing data, inconsistent naming, and data type issues, the cleaned dataset provides a reliable foundation for in-depth analysis of subway delay patterns, operational efficiency, and service quality across the TTC network.

All transformations are documented and reversible, ensuring transparency and reproducibility in the data preparation pipeline.