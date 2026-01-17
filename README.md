# Industrial PV System Sizing and Solar Irradiance Analysis (Berlin Brewery)

**Python | pvlib | Data Driven Energy Modeling | Real Industrial Case**

## Project Overview
Developed a location specific solar irradiance and PV system sizing model for an **actual brewery in Berlin**. The project evaluates rooftop solar potential by modeling **usable sunlight hours** over the year 2024 and supports engineering decisions on **PV panel selection and system capacity** under real world constraints.

## System Modeling and Analysis

### 1. Solar Irradiance and Sunlight Hour Modeling
Data Source: Physics based clear sky model using **pvlib**  
Resolution: Hourly simulation over full year 2024  
Criterion: Sunlight hour defined as **GHI > 120 W/m²** to reflect practical PV generation conditions  
Output: Monthly, daily average, and annual effective sunlight hours  

### 2. Location and Rooftop Constraints
Location: Berlin, Germany (52.5204°N, 13.4050°E)  
Inputs: Available rooftop area, panel dimensions, and orientation assumptions  
Purpose: Translate solar availability into feasible system size  

### 3. PV System Support Calculations
Compared PV module options based on efficiency and area constraints  
Estimated annual energy yield using modeled sunlight availability  
Results used to assess whether rooftop PV can satisfy brewery energy demand  

## Visualization and Results
Monthly sunlight hour distribution  
Seasonal variation analysis for Berlin climate  
Provides clear basis for PV feasibility and system dimensioning  

## Technical Skills Demonstrated
**Solar Energy Modeling:** Clear sky irradiance and sunlight availability analysis  
**Applied Physics:** Translating irradiance into usable PV generation metrics  
**Data Analysis:** Time series processing and aggregation with pandas  
**Engineering Decision Support:** Linking environmental modeling to real industrial constraints  
