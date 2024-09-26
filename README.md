# Climate Data Analysis Project

## Overview
This project focuses on analyzing climate data using **PySpark** to process large-scale datasets. The goal of the project is to identify trends such as temperature variations and rainfall patterns across different regions of New Zealand. The analysis involves multiple steps including data extraction, transformation, and visualization.

The dataset consists of climate observations such as daily maximum and minimum temperatures, rainfall, and other relevant meteorological metrics from various weather stations.

## Project Structure
The project is organized into several key components, as detailed below:

### Notebooks
- **01_processing_stations_notebook.ipynb**: Processes and cleans the data from weather stations.
- **02_daily_pyspark_notebook.ipynb**: Handles the daily-level climate data, focusing on data transformation using PySpark.
- **03_analysis_pyspark_notebook.ipynb**: Performs the analysis of temperature trends, rainfall patterns, and other climate metrics.
- **04_visualizations_pyspark_notebook.ipynb**: Generates visualizations such as temperature trends and average rainfall charts.

### Python Scripts
- **average_rainfall_2023.py**: Script to calculate and visualize average rainfall across different regions for the year 2023.
- **closest_station_map.py**: Script to identify the closest weather stations based on geographical data.

### Data
- **data_2023.csv**: Example of climate data for the year 2023, including temperature, rainfall, and other relevant measurements.
- **tmax_tmin_nz.csv**: A sample dataset used for analyzing maximum and minimum temperatures in New Zealand.

### Plots
- **average_rainfall_2023.png**: Visual representation of average rainfall for 2023.
- **average_tmin_tmax_nz_country.png**: A graph showing the average minimum and maximum temperatures across New Zealand.
- Several station-specific temperature plots, such as `temperature_station_NZ000093417.png`, show temperature variations at specific weather stations.

## Key Insights
1. **Temperature Trends**: The analysis reveals how temperatures vary across New Zealand's regions and how different weather stations compare.
2. **Rainfall Patterns**: Visualizing rainfall data helps identify areas with high or low rainfall and how these trends change over time.
3. **Station-Based Analysis**: Individual weather stations' data allow for localized climate assessments, showing variability in weather across different parts of the country.

## Purpose
This project is part of a broader effort to showcase data engineering and data analysis skills using PySpark and large datasets. It highlights abilities in:
- Handling and cleaning real-world climate data.
- Using PySpark for distributed data processing.
- Creating meaningful visualizations that convey insights from the data.
