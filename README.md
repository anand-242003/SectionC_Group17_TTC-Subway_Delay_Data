# TTC Subway Delay Data Analysis

## Project Overview

![TTC Subway Analysis](image.png)

This project contains a comprehensive analysis of Toronto Transit Commission (TTC) subway delay data for the year 2025. The dataset includes detailed information about delay incidents across the TTC subway network, providing insights into operational patterns, peak delay periods, and affected stations.

## Dataset Information

- **Total Records**: 25,716 delay incidents
- **Time Period**: January 1, 2025 to December 31, 2025 (Full year coverage)
- **Lines Covered**: Yonge-University (YU), Bloor-Danforth (BD), Sheppard (SHP)
- **Number of Stations**: 476 unique station entries
- **Delay Codes**: 132 distinct delay classification codes

## Directory Structure

```
├── Raw_dataset/          # Original unprocessed data (frozen/locked)
├── Cleaned_dataset/      # Cleaned and processed data via Google Sheets
├── Calculation_and_Pivot_Table/  # Statistical calculations and pivot tables
├── Dashboard/            # Dashboard-ready data
├── Documentation/        # Project documentation
└── Presentation/         # Presentation materials
```

## Column Specifications and Statistical Analysis

| Column | Type | Unique Values | Range/Top Values | Mean/Median | Key Issues |
|--------|------|--------------|------------------|-------------|------------|
| **_id** | Numeric | 25,714 | 1 to 25,713 | 12,857 | 2 duplicates, 2 empty |
| **Date** | Date | 366 | 2025-01-01 to 2025-12-31 | 2025-07-02 | 2 empty cells |
| **Time** | Time | 1,427 | 00:00 to 23:59 | 13:17 | Full 24-hour coverage |
| **Day** | Categorical | 8 | Wed (15.7%), Thu (15.2%), Fri (15.1%) | Wednesday | Weekday bias (76%) |
| **Station** | Categorical | 476 | Kennedy (991), Bloor (924), Finch (898) | - | Naming inconsistencies |
| **Code** | Categorical | 132 | SUDP (11.5%), MUIS (9.1%), SUO (6.5%) | - | 132 delay types |
| **Min Delay** | Numeric | 106 | 0 to 900 min | 0 | 64.6% have 0 delay |
| **Min Gap** | Numeric | 114 | 0 to 906 min | 0 | 66.6% have 0 gap |
| **Bound** | Categorical | 7 | None (36.8%), S (16.9%), E (16.0%) | - | 36.8% missing data |
| **Line** | Categorical | 20 | YU (50.9%), BD (43.3%), SHP (4.1%) | - | 20 naming variations |
| **Vehicle** | Numeric | 743 | 0 to 9,463 | 5,110 | 41.9% are 0 (missing) |

## Data Dictionary

| Column Name | Description | Data Type | Example Values | Business Relevance |
|------------|-------------|-----------|----------------|-------------------|
| **_id** | Unique incident identifier | Integer | 1, 2, 3, ... | Record tracking and deduplication |
| **Date** | Date of delay incident | Date | 2025-01-01, 2025-12-31 | Temporal trend analysis |
| **Time** | Time of delay incident | Time | 08:15:00, 17:30:00 | Peak hour identification |
| **Day** | Day of week | Text | Monday, Tuesday, Wednesday | Weekly pattern analysis |
| **Station** | Station where delay occurred | Text | BLOOR STATION, KENNEDY BD | Hotspot identification |
| **Code** | TTC internal delay classification | Text | SUDP, MUIS, SUO | Root cause categorization |
| **Min Delay** | Duration of delay (minutes) | Integer | 0, 3, 5, 15, 900 | Service impact measurement |
| **Min Gap** | Service gap caused (minutes) | Integer | 0, 8, 10, 15 | Headway disruption analysis |
| **Bound** | Train direction | Text | N, S, E, W, None | Directional pattern analysis |
| **Line** | Subway line identifier | Text | YU, BD, SHP, YU/BD | Line performance comparison |
| **Vehicle** | Train vehicle ID | Integer | 5227, 6181, 0 | Vehicle reliability tracking |

### Derived Columns (Cleaned Dataset)

| Column Name | Description | Values | Derivation Logic |
|------------|-------------|--------|-----------------|
| **Bound_Clean** | Standardized direction | N, S, E, W, B, Unknown | None → "Unknown" |
| **Line_Clean** | Standardized line code | YU, BD, SHP, SRT | VLOOKUP mapping (20→6 codes) |
| **Delay_Category** | Severity classification | No Delay, Minor, Moderate, Major | 0 min / 1-5 min / 6-15 min / 16+ min |
| **Time_Period** | Operational time segment | Night, AM Peak, Midday, PM Peak, Evening | Hour-based segmentation |
| **Is_Delayed** | Binary delay indicator | Yes, No | Min Delay > 0 |

## Key Findings

| Category | Finding | Impact |
|----------|---------|--------|
| **Data Quality** | 2 duplicate IDs, 2 empty rows, 36.8% missing direction, 41.9% missing vehicle | Limits directional & vehicle analysis |
| **Temporal Patterns** | Weekdays (76%), Wednesday peak, Avg time: 13:17 | Weekday-focused operations |
| **Operational** | 64.6% zero-delay incidents, YU line (50.9%), Top 5 stations (17%) | YU line & terminal stations are hotspots |
| **Extreme Cases** | Max delay: 900 min (15 hours) | Severe incident management needed |

## Analysis Suggestions

1. **Line Performance Analysis**
   - Compare YU vs BD delay rates and patterns
   - Identify why YU line has 50.9% of incidents
   - Benchmark best-performing lines

2. **Station Hotspot Investigation**
   - Deep-dive into top 10 worst-performing stations
   - Analyze terminal vs transfer station patterns
   - Correlation between station type and delay severity

3. **Temporal Pattern Analysis**
   - Peak hour analysis (AM/PM rush vs off-peak)
   - Day-of-week trends (Wednesday spike investigation)
   - Seasonal patterns across 2025

4. **Delay Code Classification**
   - Categorize 132 delay codes into themes (mechanical, operational, passenger-related)
   - Identify preventable vs unpreventable delays
   - Priority ranking for intervention

5. **Zero-Delay Investigation**
   - Understand why 64.6% of incidents result in 0 min delay
   - Define threshold for "incident" vs "delay"
   - Refine data collection methodology

6. **Predictive Modeling**
   - Build delay probability models by hour/day/station
   - Forecast high-risk periods for proactive management
   - Vehicle reliability scoring

## Data Processing Pipeline

**Google Sheets 4-Tab Architecture:**

1. **Tab 1 (Raw)** → Frozen source data (`Raw_dataset/Data.csv`)
2. **Tab 1.1 (Cleaned)** → Array formula transformations (`Cleaned_dataset/Cleaned.csv`)
3. **Tab 2 (Dictionary)** → Line mapping & metadata
4. **Tab 3 (Analysis)** → Pivot tables & calculations
5. **Dashboard** → Visualization exports

**Cleaning Methods:**
- VLOOKUP for line standardization
- UPPER(TRIM()) for text normalization
- IF statements for missing values
- ARRAYFORMULA for batch processing

## Cleaned Dataset Structure

**16 Total Columns** (11 original + 5 derived)

| Type | Columns |
|------|---------|
| **Original** | _id, Date, Time, Day, Station, Code, Min Delay, Min Gap, Bound, Line, Vehicle |
| **Derived** | Month, Hour, Bound_Clean, Line_Clean, Delay_Category, Time_Period, Is_Delayed |

## Data Integrity Summary

| Metric | Value |
|--------|-------|
| **Total Records** | 25,713 (after removing 2 empty rows) |
| **Total Columns** | 16 (11 original + 5 derived) |
| **Data Points** | 411,408 |
| **Completeness** | 100% after cleaning |
| **Time Coverage** | 365 days (Full year 2025) |
| **File Size** | Raw: 1.7 MB / Cleaned: 2.5 MB |

## Next Steps

Refer to `Cleaned_dataset/README.md` for detailed information on:
- Data cleaning procedures and transformations
- Google Sheets formulas used
- Before/after quality metrics
- Feature engineering logic

---

**Generated for Toronto Transit Intelligence Dashboard**
