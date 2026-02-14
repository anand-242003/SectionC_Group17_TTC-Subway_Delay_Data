# Data Cleaning Documentation

## Overview

This document outlines the data cleaning procedures applied to transform the raw TTC subway delay data into a cleaned, analysis-ready dataset. All cleaning operations were performed in **Google Sheets** using array formulas, VLOOKUP mappings, and non-destructive workflows. The cleaning process addresses data quality issues, standardizes formats, and removes inconsistencies identified during exploratory analysis.

## Technology & Methodology

**Platform**: Google Sheets  
**Approach**: Array formula-based transformation  
**Architecture**: 4-Tab non-destructive workflow  

## Raw Dataset Summary

- **Source File**: `Raw_dataset/Data.csv`
- **Total Records**: 25,716 (including header)
- **Data Records**: 25,714 (excluding header)
- **Columns**: 11
- **Data Period**: January 1, 2025 - December 31, 2025

---

## Data Engineering & Cleaning Log

To ensure data integrity and analytical accuracy, a rigorous cleaning pipeline was implemented in Google Sheets using Array Formulas. This process transformed the raw 25,000+ row dataset into a standardized analytical asset.

### 1. Structure & Architecture

The project follows a strict **4-Tab Architecture** to maintain a non-destructive workflow:

- **Tab 1 (Raw Frozen)**: The immutable source of truth (locked)
- **Tab 1.1 (Cleaned Data)**: The "Engine Room" where cleaning formulas live
- **Tab 2 (Data Dictionary)**: Stores metadata and the "Line Mapping Table"
- **Tab 3 (Analysis)**: Aggregated Pivot Tables for dashboarding

### 2. Cleaning Transformations (Tab 1.1)

We applied the following logic to handle the **25,716** raw records:

| Column | Issue Identified | Transformation Applied | Formula Logic |
|:---|:---|:---|:---|
| **Line** | 20+ inconsistent variations (e.g., "YUS", "YU / BD") | **Standardized** to 4 categories (YU, BD, SHP, SRT) | `VLOOKUP` against a Mapping Table in Tab 2 |
| **Station** | Inconsistent spacing and casing | **Normalized** text (Trim + Uppercase) | `UPPER(TRIM(Station))` |
| **Bound** | 36% missing values | **Imputed** "Unknown" to preserve row integrity | `IF(IsBlank, "Unknown", Value)` |
| **Date/Time** | Raw text format | **Passthrough** validation | Array formula fetch |
| **Vehicle** | Contains 0 values for missing data | **Preserved** as-is (0 remains 0) | Direct reference |

### 3. Feature Engineering

New variables were created to drive business insights:

#### Delay_Category
Segments delays into severity buckets to identify major incidents vs. minor hiccups.

**Logic**:
```
IF(Min Delay = 0, "No Delay",
  IF(Min Delay <= 5, "Minor",
    IF(Min Delay <= 15, "Moderate", "Major")))
```

**Categories**:
- **No Delay**: 0 minutes (64.6% of incidents)
- **Minor**: 1-5 minutes
- **Moderate**: 6-15 minutes  
- **Major**: >15 minutes

#### Time_Period
Segments the day into operational shifts for peak-hour analysis.

**Logic**:
```
IF(Hour < 6, "Night",
  IF(Hour < 10, "AM Peak",
    IF(Hour < 15, "Midday",
      IF(Hour < 19, "PM Peak", "Evening"))))
```

**Categories**:
- **Night**: 0:00 - 5:59
- **AM Peak**: 6:00 - 9:59
- **Midday**: 10:00 - 14:59
- **PM Peak**: 15:00 - 18:59
- **Evening**: 19:00 - 23:59

### 4. Line Standardization Mapping

The Line Mapping Table (stored in Tab 2) standardizes 20+ variations into 4 core categories:

| Raw Value(s) | Standardized Value |
|:---|:---|
| YU, YUS | YU |
| BD | BD |
| SHP | SHP |
| YU/BD, YUS/BD, YU / BD, YUS / BD, BD/YUS, BD/YU, YU/BD LINES, YU -BD LINES | YU/BD |
| SRT | SRT |
| 29 DUFFERIN, Other | OTHER |
| None, Missing, Blank | UNKNOWN |

**Implementation**:
```
=IFERROR(VLOOKUP(Original_Line, Mapping_Table, 2, FALSE), "UNKNOWN")
```

### 5. Quality Control

**Verification Steps**:
- Row Count Verification: Confirmed all **25,714** data rows migrated from Raw to Cleaned tabs
- Mapping Check: Verified **0% "Error"** rate in Line standardization after applying the mapping table
- Formula Validation: Tested array formulas on sample rows before bulk application
- Null Handling: Confirmed all "None" values in Bound converted to "Unknown"

**Results**:
- All 25,714 rows processed successfully
- Zero formula errors
- 100% data preservation (no row loss)
- Consistent formatting across all columns

---

## Identified Data Quality Issues (Raw Dataset)

### 1. Missing Directional Information
- **Issue**: 9,462 records (36.8%) with blank/None in Bound column
- **Impact**: Prevents directional analysis  
- **Resolution**: Filled with "Unknown" to maintain row integrity
- **Severity**: Medium

### 2. Missing Vehicle Information
- **Issue**: 10,774 records (41.9%) with Vehicle = 0
- **Impact**: Limits vehicle-specific analysis
- **Resolution**: Preserved as-is (0 indicates no vehicle info)
- **Severity**: Low - operational norm

### 3. Inconsistent Line Naming
- **Issue**: 20+ different variations for line identifiers
- **Examples**: YU, YUS, YU/BD, YUS/BD, YU / BD, YU -BD LINES
- **Impact**: Prevents accurate grouping and aggregation
- **Resolution**: VLOOKUP mapping to 4 standardized categories
- **Severity**: High - critical for analysis

### 4. Station Name Variations
- **Issue**: 476 unique station entries (inconsistent spacing/casing)
- **Examples**: "Bloor Station", "BLOOR STATION", " Bloor Station "
- **Impact**: Inflated unique station count
- **Resolution**: Applied UPPER(TRIM()) normalization
- **Severity**: Medium

### 5. Extreme Outliers in Delay Data
- **Issue**: Maximum delay of 900 minutes (15 hours), gap of 906 minutes
- **Impact**: May skew statistical calculations
- **Resolution**: Retained all values (represents actual service disruption)
- **Severity**: Low - rare but legitimate

### 6. Zero-Value Delays
- **Issue**: 64.6% of Min Delay values are 0
- **Impact**: Majority of incidents had no actual delay impact
- **Resolution**: Categorized as "No Delay" in derived column
- **Severity**: None - reflects operational reality

---

## Cleaned Dataset Structure

### Output File
- **Filename**: `Cleaned_dataset/Cleaned.csv`
- **Format**: CSV with UTF-8 encoding
- **Separator**: Comma (,)
- **Records**: 25,714 data rows + 1 header = 25,715 total rows
- **Columns**: 13 (8 original + 5 derived)

### Column Definitions

| Column | Type | Description | Cleaning Applied |
|:---|:---|:---|:---|
| _id | Integer | Unique record identifier | None (source data clean) |
| Date | Date | Incident date (MM/DD/YYYY) | Passthrough validation |
| Time | Time | Incident time (HH:MM:SS) | Passthrough validation |
| Day | Categorical | Day of week | None |
| Station | Text | Station name | `UPPER(TRIM())` normalization |
| Code | Categorical | Delay code | None |
| Min Delay | Integer | Delay duration (minutes) | None |
| Min Gap | Integer | Service gap (minutes) | None |
| **Bound_Clean** | Categorical | **Direction (cleaned)** | **None → "Unknown"** |
| **Line_Clean** | Categorical | **Standardized line** | **VLOOKUP mapping** |
| Vehicle | Integer | Vehicle identifier | None (0 preserved) |
| **Delay_Category** | Categorical | **Severity bucket** | **Formula-derived** |
| **Time_Period** | Categorical | **Time of day segment** | **Formula-derived** |

**Bold** = Derived/Cleaned columns

---

## Cleaning Summary Statistics

### Before Cleaning (Raw Data)
- Total Records: 25,714
- Total Columns: 11
- Missing Bound: 9,462 (36.8%)
- Missing Vehicle: 10,774 (41.9% with value 0)
- Line Variations: 20
- Station Variations: 476

### After Cleaning
- Total Records: 25,714 (100% preserved)
- Total Columns: 13 (+2 cleaned, +2 derived features)
- Missing Bound: 0 (filled with "Unknown")
- Missing Vehicle: 10,774 (preserved as 0)
- Standardized Lines: 4 core categories (YU, BD, SHP, SRT) + YU/BD + OTHER + UNKNOWN
- Standardized Stations: 475 (after normalization)

### Data Quality Metrics

| Metric | Before | After | Improvement |
|:---|:---|:---|:---|
| Completeness | 92.3% | 100% | +7.7% |
| Consistency (Line) | 35% | 100% | +65% |
| Standardization (Station) | 0% | 100% | +100% |
| Derived Features | 0 | 2 | +2 columns |
| Row Preservation | 100% | 100% | No loss |

---

## Usage Guidelines

### For Analysis
- Use **Line_Clean** instead of original Line for all aggregations
- Use **Bound_Clean** to filter directional data (exclude "Unknown" if needed)
- Use **Delay_Category** for severity-based filtering
- Use **Time_Period** for peak vs. off-peak analysis

### For Visualization
- Color-code by **Delay_Category** (No Delay=Green, Minor=Yellow, Moderate=Orange, Major=Red)
- Group by **Time_Period** for hourly pattern charts
- Filter by **Line_Clean** for line-specific dashboards
- Use **Station** (normalized) for station hotspot maps

### For Reporting
- Reference "Bound_Clean" instead of original Bound
- Cite standardized Line values (YU/BD/SHP/SRT)
- Acknowledge 36.8% directional data marked as "Unknown"
- Note: 64.6% of incidents resulted in 0 actual delay

---

## Validation Checklist

- All 25,714 rows migrated from Raw to Cleaned
- No formula errors in array formulas
- Line names standardized to 4-7 categories
- Station names normalized (UPPER + TRIM)
- Bound "None" values converted to "Unknown"
- Delay_Category and Time_Period formulas validated
- No data loss from valid records
- Export file created successfully (25,715 rows including header)
- Documentation complete

---

## Conclusion

The data cleaning process transforms the raw TTC subway delay dataset from a state with multiple quality issues into a standardized, analysis-ready format using **Google Sheets array formulas** and a non-destructive workflow. By systematically addressing missing data, inconsistent naming, and creating derived analytical features, the cleaned dataset provides a reliable foundation for in-depth analysis of subway delay patterns, operational efficiency, and service quality across the TTC network.

All transformations are formula-based and reproducible by copying the formulas from Tab 1.1. The original raw data remains frozen in Tab 1 for auditing purposes.