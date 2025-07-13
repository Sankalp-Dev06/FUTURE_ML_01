# 📊 Sales Forecasting Dashboard Project

## 🎯 Project Overview

This project is a comprehensive **AI-powered Sales Forecasting Dashboard** that analyzes historical sales data from a Superstore dataset and provides accurate sales predictions using advanced machine learning techniques. The dashboard offers interactive visualizations and insights for strategic business decision-making.

## 🚀 Project Structure

```
sales_forecasting_dashboard/
├── Data/
│   ├── Raw/                    # Original Superstore dataset
│   ├── Processed/              # Cleaned and processed data
│   └── Forecast/               # Generated forecasts by region
├── notebooks/                  # Jupyter notebooks for analysis
│   ├── 01_exploration.ipynb   # Data exploration and analysis
│   ├── 02_forecast.ipynb      # Forecasting model development
│   └── 03_dashboard_data_preparation.ipynb # Data preparation for dashboard
├── dashboard.py                # Main Streamlit dashboard application
├── .streamlit/config.toml     # Dashboard configuration
└── requirements.txt           # Project dependencies
```

## 📈 Data Processing Pipeline

### 1. **Data Exploration** (`01_exploration.ipynb`)
- **Purpose**: Initial analysis of the Superstore dataset
- **Activities**: 
  - Data quality assessment
  - Sales trend analysis
  - Regional performance evaluation
  - Seasonal pattern identification
  - Statistical summary generation

### 2. **Forecasting Model Development** (`02_forecast.ipynb`)
- **Purpose**: Building and training the sales forecasting model
- **Techniques Used**:
  - **Prophet Model**: Facebook's time series forecasting algorithm
  - **Seasonal Decomposition**: Identifying trends, seasonality, and residuals
  - **Regional Analysis**: Separate forecasting for each region (Central, East, South, West)
  - **Confidence Intervals**: Providing uncertainty estimates for predictions

### 3. **Dashboard Data Preparation** (`03_dashboard_data_preparation.ipynb`)
- **Purpose**: Preparing processed data for dashboard visualization
- **Outputs**:
  - `pbi_forecast_national.csv`: National-level forecasts
  - `pbi_forecast_by_region.csv`: Regional forecasts
  - `monthly_sales_national.csv`: Historical national sales
  - `monthly_sales_by_region.csv`: Historical regional sales

## 🎨 Dashboard Sections Explained

### 🏠 **Overview Page**
**What it represents**: Executive summary and key performance indicators

**Components**:
- **Key Metrics Row**: 
  - Latest Forecast: Most recent sales prediction
  - Average Forecast: Mean of all forecasted values
  - Regions Analyzed: Number of geographic regions (4: Central, East, South, West)
  - Forecast Periods: Total number of time periods analyzed

- **National Sales Forecast Trend**: 
  - Shows the complete forecast timeline with confidence intervals
  - Blue line represents predicted sales
  - Shaded area shows the range of likely values (confidence interval)

- **Regional Forecast Comparison**: 
  - Bar chart comparing latest forecasts across all regions
  - Helps identify which regions are performing best/worst

**Business Value**: Quick overview for executives to understand current forecasting status and regional performance.

### 📈 **National Forecast Page**
**What it represents**: Detailed analysis of national sales forecasting with interactive controls

**Components**:
- **Date Range Selector**: 
  - Interactive date pickers to focus on specific time periods
  - Allows zooming into particular months or years

- **Main Forecast Chart**: 
  - Interactive line chart with confidence intervals
  - Shows predicted sales with upper/lower bounds
  - Hover for detailed values

- **Statistics Panel**: 
  - Average, Maximum, and Minimum forecasts for selected period
  - Quick numerical insights

- **Monthly Breakdown**: 
  - Bar chart showing average sales by month
  - Identifies seasonal patterns (e.g., December peaks, February lows)

**Business Value**: Detailed planning tool for national sales strategies and resource allocation.

### 🗺️ **Regional Analysis Page**
**What it represents**: Comparative analysis of sales performance across different geographic regions

**Components**:
- **Region Selector**: 
  - Multi-select dropdown to choose which regions to compare
  - Default shows all regions (Central, East, South, West)

- **Regional Comparison Chart**: 
  - Line chart showing forecast trends for selected regions
  - Different colors for each region
  - Helps identify regional patterns and differences

- **Regional Performance Summary**: 
  - Data table with statistics for each region:
    - Average: Mean sales per region
    - Maximum: Peak sales achieved
    - Minimum: Lowest sales recorded
    - Std Dev: Sales volatility/consistency

- **Top Performing Regions**: 
  - Bar chart ranking regions by latest forecast
  - Color-coded by performance level

**Business Value**: Strategic planning for regional resource allocation, identifying growth opportunities, and understanding geographic market differences.

### 📊 **Performance Metrics Page**
**What it represents**: Historical vs forecast comparison and growth analysis

**Components**:
- **Performance Metrics Row**: 
  - Historical Average: Mean of actual past sales
  - Forecast Average: Mean of predicted sales
  - Growth Rate: Percentage change from historical to forecast
  - Volatility: Standard deviation showing sales consistency

- **Historical vs Forecast Performance**: 
  - Dual-line chart comparing actual vs predicted sales
  - Orange line: Historical data
  - Blue line: Forecast data
  - Shows how well the model predicts actual trends

- **Seasonal Analysis**: 
  - Grouped bar chart comparing monthly averages
  - Historical vs forecast for each month
  - Identifies seasonal patterns and prediction accuracy

**Business Value**: Model validation, understanding prediction accuracy, and identifying seasonal business patterns for strategic planning.

## 🔧 Technical Implementation

### **Forecasting Model**
- **Algorithm**: Facebook Prophet
- **Features**: Handles seasonality, trends, and holidays automatically
- **Output**: Point forecasts with confidence intervals
- **Regional Approach**: Separate models for each region to capture local patterns

### **Dashboard Technology**
- **Framework**: Streamlit (Python web application)
- **Visualization**: Plotly (Interactive charts)
- **Data Processing**: Pandas (Data manipulation)
- **Styling**: Custom CSS for professional appearance

### **Data Flow**
1. **Raw Data** → Superstore sales dataset
2. **Processing** → Cleaned and aggregated by month/region
3. **Modeling** → Prophet forecasting for each region
4. **Dashboard** → Interactive visualization and analysis

## 🎯 Business Intelligence Insights

### **Strategic Planning**
- **Long-term projections**: 5-year sales forecasts
- **Seasonal planning**: Identify peak and low seasons
- **Resource allocation**: Regional performance insights

### **Risk Assessment**
- **Confidence intervals**: Understand forecast uncertainty
- **Volatility analysis**: Identify stable vs volatile regions
- **Model validation**: Compare predictions with actual performance

### **Performance Monitoring**
- **Growth tracking**: Historical vs forecast comparisons
- **Regional benchmarking**: Compare performance across regions
- **Trend analysis**: Identify upward/downward sales patterns

## 🚀 How to Run

### **Prerequisites**
- Python 3.8 or higher
- Required packages (see requirements.txt)

### **Quick Start**
```bash
# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run dashboard.py
```

### **Access Dashboard**
- URL: `http://localhost:8501`
- Opens automatically in your default browser

## 📊 Key Metrics Explained

### **Forecast Metrics**
- **yhat**: Predicted sales value
- **yhat_lower/yhat_upper**: Confidence interval bounds
- **Confidence Interval**: Range where actual sales are likely to fall

### **Performance Metrics**
- **Growth Rate**: Percentage change from historical to forecast
- **Volatility**: Standard deviation indicating sales consistency
- **Seasonal Patterns**: Monthly variations in sales performance

### **Regional Analysis**
- **Central Region**: Geographic area with specific sales patterns
- **East Region**: Different market characteristics and trends
- **South Region**: Unique regional performance factors
- **West Region**: Distinct sales patterns and opportunities

## 🎨 Dashboard Features

### **Interactive Elements**
- **Date Range Selectors**: Focus on specific time periods
- **Region Filters**: Compare selected geographic areas
- **Hover Tooltips**: Detailed information on chart elements
- **Responsive Design**: Works on different screen sizes

### **Professional Styling**
- **Modern Design**: Clean, professional appearance
- **Color Coding**: Consistent color scheme for easy interpretation
- **Gradient Headers**: Visual appeal with gradient text effects
- **Smooth Animations**: Enhanced user experience

## 📈 Data Sources

### **Superstore Dataset**
- **Product Categories**: Furniture, Office Supplies, Technology
- **Geographic Coverage**: 4 regions across the United States
- **Time Period**: Historical sales data with monthly aggregation
- **Variables**: Sales, Profit, Quantity, Region, Category

### **Forecast Outputs**
- **National Level**: Overall sales predictions
- **Regional Level**: Geographic-specific forecasts
- **Time Horizon**: Extended forecasting period
- **Confidence Bands**: Uncertainty quantification

## 🔍 Troubleshooting

### **Common Issues**
1. **Data Loading Errors**: Ensure CSV files are in correct directories
2. **Missing Dependencies**: Install requirements with `pip install -r requirements.txt`
3. **Display Issues**: Clear browser cache or try different browsers

### **Performance Tips**
- Use data caching for large datasets
- Optimize chart rendering with appropriate sampling
- Consider database connections for real-time updates


**Built using Streamlit, Plotly, and Facebook Prophet**

*This project demonstrates advanced time series forecasting techniques applied to real-world business data, providing actionable insights for strategic decision-making.*

## 👤 Author

**Developed by:**  
Sankalp Tiwari   
- [LinkedIn](www.linkedin.com/in/sankalp-tiwari-350545203) | [GitHub](https://github.com/Sankalp-Dev06)

