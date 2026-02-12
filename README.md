# TTC Subway Delay Data Analysis

## Project Overview

This project contains a comprehensive analysis of Toronto Transit Commission (TTC) subway delay data for the year 2025. The dataset includes detailed information about delay incidents across the TTC subway network, providing insights into operational patterns, peak delay periods, and affected stations.

## Dataset Information

- **Total Records**: 25,716 delay incidents
- **Time Period**: January 1, 2025 to December 31, 2025 (Full year coverage)
- **Lines Covered**: Yonge-University (YU), Bloor-Danforth (BD), Sheppard (SHP)
- **Number of Stations**: 476 unique station entries
- **Delay Codes**: 132 distinct delay classification codes

## Directory Structure

```
├── Raw_dataset/          # Original unprocessed data
├── Cleaned_dataset/      # Cleaned and processed data
├── Calculation_and_Pivot_Table/  # Statistical calculations
├── Dashboard/            # Dashboard-ready data
├── Documentation/        # Project documentation
├── Presentation/         # Presentation materials
└── analyze_data.py       # Data analysis script
```

## Column Specifications and Statistical Analysis

### 1. _id (Record Identifier)
- **Type**: Numeric Identifier
- **Total Rows**: 25,716
- **Unique Values**: 25,714
- **Empty Cells**: 2
- **Range**: 1 to 25,713
- **Mean/Median**: 12,857
- **Note**: 2 duplicate IDs identified in the raw dataset

### 2. Date (Incident Date)
- **Type**: Temporal (Date)
- **Total Rows**: 25,716
- **Unique Dates**: 366
- **Empty Cells**: 2
- **Date Range**: 2025-01-01 to 2025-12-31
- **Median Date**: 2025-07-05
- **Average Date**: 2025-07-02
- **Note**: 366 unique dates indicates leap year coverage

### 3. Time (Incident Time)
- **Type**: Temporal (Time)
- **Total Rows**: 25,716
- **Unique Values**: 1,427
- **Empty Cells**: 2
- **Time Range**: 00:00 to 23:59
- **Average Time**: 13:17
- **Median Time**: 13:50
- **Note**: Incidents distributed across all hours of operation

### 4. Day (Day of Week)
- **Type**: Categorical
- **Total Rows**: 25,716
- **Unique Values**: 8
- **Empty Cells**: 2
- **Distribution**:
  - Wednesday: 4,035 (15.7%)
  - Thursday: 3,910 (15.2%)
  - Friday: 3,893 (15.1%)
  - Monday: 3,878 (15.1%)
  - Tuesday: 3,809 (14.8%)
  - Saturday: ~3,200 (12.4%)
  - Sunday: ~2,900 (11.3%)
- **Insight**: Weekdays show higher delay frequency than weekends

### 5. Station (Station Name)
- **Type**: Categorical
- **Total Rows**: 25,716
- **Unique Values**: 476
- **Empty Cells**: 2
- **Top 5 Most Affected Stations**:
  1. KENNEDY BD STATION: 991 incidents (3.9%)
  2. BLOOR STATION: 924 incidents (3.6%)
  3. FINCH STATION: 898 incidents (3.5%)
  4. KIPLING STATION: 870 incidents (3.4%)
  5. EGLINTON STATION: 666 incidents (2.6%)
- **Note**: High number of unique values may indicate naming inconsistencies

### 6. Code (Delay Code)
- **Type**: Categorical
- **Total Rows**: 25,716
- **Unique Values**: 132
- **Empty Cells**: 2
- **Top 5 Most Frequent Codes**:
  1. SUDP: 2,945 incidents (11.5%)
  2. MUIS: 2,328 incidents (9.1%)
  3. SUO: 1,672 incidents (6.5%)
  4. MUPAA: 1,367 incidents (5.3%)
  5. PUOPO: 1,264 incidents (4.9%)
- **Note**: Codes represent different types of operational issues

### 7. Min Delay (Delay Duration in Minutes)
- **Type**: Numeric (Integer)
- **Total Rows**: 25,716
- **Unique Values**: 106
- **Empty Cells**: 2
- **Sum**: 70,754 minutes (1,179.2 hours)
- **Mean**: 2.75 minutes
- **Median**: 0 minutes
- **Range**: 0 to 900 minutes
- **Distribution Highlights**:
  - 0 minutes: 16,619 incidents (64.6%)
  - 3 minutes: 2,351 incidents (9.1%)
  - 4 minutes: 1,799 incidents (7.0%)
  - 5 minutes: 1,411 incidents (5.5%)
  - 6 minutes: 820 incidents (3.2%)
- **Insight**: Majority of incidents result in no actual delay; maximum delay of 900 minutes (15 hours) indicates severe outlier

### 8. Min Gap (Gap Duration in Minutes)
- **Type**: Numeric (Integer)
- **Total Rows**: 25,716
- **Unique Values**: 114
- **Empty Cells**: 2
- **Sum**: 100,503 minutes (1,675.1 hours)
- **Mean**: 3.91 minutes
- **Median**: 0 minutes
- **Range**: 0 to 906 minutes
- **Distribution Highlights**:
  - 0 minutes: 17,125 incidents (66.6%)
  - 8 minutes: 1,445 incidents (5.6%)
  - 10 minutes: 1,056 incidents (4.1%)
  - 6 minutes: 1,003 incidents (3.9%)
  - 9 minutes: 961 incidents (3.7%)
- **Insight**: Gap represents service headway increase; majority show no gap impact

### 9. Bound (Direction/Bound)
- **Type**: Categorical
- **Total Rows**: 25,716
- **Unique Values**: 7
- **Empty Cells**: 2
- **Distribution**:
  - None: 9,462 incidents (36.8%)
  - S (South): 4,357 incidents (16.9%)
  - E (East): 4,126 incidents (16.0%)
  - W (West): 3,886 incidents (15.1%)
  - N (North): 3,857 incidents (15.0%)
  - Others: Minor categories
- **Note**: High proportion of "None" values indicates missing directional data

### 10. Line (Subway Line)
- **Type**: Categorical
- **Total Rows**: 25,716
- **Unique Values**: 20
- **Empty Cells**: 2
- **Distribution**:
  - YU (Yonge-University): 13,079 incidents (50.9%)
  - BD (Bloor-Danforth): 11,143 incidents (43.3%)
  - SHP (Sheppard): 1,065 incidents (4.1%)
  - YU/BD: 319 incidents (1.2%)
  - None: 67 incidents (0.3%)
  - Others: Various naming inconsistencies
- **Note**: Multiple naming variations (YU/BD, YUS/BD, etc.) require standardization

### 11. Vehicle (Vehicle Identifier)
- **Type**: Numeric Identifier
- **Total Rows**: 25,716
- **Unique Values**: 743
- **Empty Cells**: 2
- **Sum**: 82,311,819
- **Mean**: 3,201.18
- **Median**: 5,110
- **Range**: 0 to 9,463
- **Distribution Highlights**:
  - 0: 10,774 incidents (41.9%) - Dominant value
  - 6181: 72 incidents
  - 5896: 68 incidents
  - 5746: 67 incidents
  - 5876: 66 incidents
- **Note**: High frequency of "0" values likely indicates missing vehicle information

## Key Findings

### Data Quality Issues Identified
1. **Missing Data**: 2 rows with empty cells across all columns
2. **Duplicate IDs**: 2 duplicate entries in the _id column
3. **Direction Data**: 36.8% of records lack directional (Bound) information
4. **Vehicle Information**: 41.9% of records show vehicle ID as 0
5. **Line Naming**: Inconsistent naming conventions across 20 variations
6. **Station Names**: 476 unique station entries may include duplicates/variations

### Temporal Patterns
- **Weekday vs Weekend**: Weekdays account for 76% of delays
- **Peak Day**: Wednesday shows highest delay frequency
- **Time Distribution**: Average incident time is 13:17 (early afternoon)

### Operational Insights
- **Delay Impact**: 64.6% of incidents result in 0 minutes actual delay
- **Line Distribution**: YU line experiences 50.9% of all delays
- **Station Hotspots**: Top 5 stations account for 17% of all incidents
- **Extreme Cases**: Maximum delay of 900 minutes (15 hours) indicates critical incidents

## Data Processing Pipeline

1. **Raw Dataset** (`Raw_dataset/Data.csv`) - Original unprocessed data
2. **Cleaned Dataset** (`Cleaned_dataset/Cleaned.csv`) - Processed and validated data
3. **Calculations** (`Calculation_and_Pivot_Table/`) - Statistical analysis
4. **Dashboard** (`Dashboard/`) - Visualization-ready data

## Requirements

- Python 3.x
- pandas library

## Usage

Run the analysis script:
```bash
python analyze_data.py
```

## Data Integrity Notes

- Total data points: 282,876 (11 columns × 25,716 rows)
- Completeness: 99.99% (excluding intentional "None" values)
- Time span: 365 days continuous coverage
- Data collection: 2025 calendar year

## Next Steps

Refer to `Cleaned_dataset/README.md` for detailed information on data cleaning procedures and transformations applied to the raw dataset.