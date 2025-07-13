import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import warnings
import os
warnings.filterwarnings('ignore')

# Disable Streamlit onboarding
os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
os.environ['STREAMLIT_SERVER_RUN_ON_SAVE'] = 'false'

# Page configuration
st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(90deg, #1f77b4, #ff7f0e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    .stSelectbox > div > div {
        background-color: white;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    
    .stButton > button:hover {
        background: linear-gradient(90deg, #764ba2, #667eea);
        transform: translateY(-2px);
        transition: all 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    """Load and cache the forecasting data"""
    try:
        # Load national forecast data
        national_forecast = pd.read_csv('Data/Processed/pbi_forecast_national.csv')
        national_forecast['ds'] = pd.to_datetime(national_forecast['ds'])
        
        # Load regional forecast data
        regional_forecast = pd.read_csv('Data/Processed/pbi_forecast_by_region.csv')
        regional_forecast['ds'] = pd.to_datetime(regional_forecast['ds'])
        
        # Load historical sales data - handle correct column names
        monthly_sales_national = pd.read_csv('Data/Processed/monthly_sales_national.csv')
        monthly_sales_national['Date'] = pd.to_datetime(monthly_sales_national['ds'])
        monthly_sales_national['Sales'] = monthly_sales_national['y']
        
        monthly_sales_by_region = pd.read_csv('Data/Processed/monthly_sales_by_region.csv')
        monthly_sales_by_region['Date'] = pd.to_datetime(monthly_sales_by_region['ds'])
        monthly_sales_by_region['Sales'] = monthly_sales_by_region['y']
        
        return national_forecast, regional_forecast, monthly_sales_national, monthly_sales_by_region
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None, None, None

# Load data
national_forecast, regional_forecast, monthly_sales_national, monthly_sales_by_region = load_data()

# Sidebar navigation
st.sidebar.markdown("## 📊 Navigation")
page = st.sidebar.selectbox(
    "Choose a page:",
    ["🏠 Overview", "📈 National Forecast", "🗺️ Regional Analysis", "📊 Performance Metrics"]
)

# Helper functions
def format_currency(value):
    """Format number as currency"""
    return f"${value:,.0f}"

def calculate_growth_rate(current, previous):
    """Calculate growth rate percentage"""
    if previous == 0:
        return 0
    return ((current - previous) / previous) * 100

# Main dashboard logic
if page == "🏠 Overview":
    st.markdown('<h1 class="main-header">Sales Forecasting Dashboard</h1>', unsafe_allow_html=True)
    
    # Key metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if national_forecast is not None:
            latest_forecast = national_forecast['yhat'].iloc[-1]
            st.metric(
                label="Latest Forecast",
                value=format_currency(latest_forecast),
                delta=f"{latest_forecast - national_forecast['yhat'].iloc[-2]:,.0f}"
            )
    
    with col2:
        if national_forecast is not None:
            avg_forecast = national_forecast['yhat'].mean()
            st.metric(
                label="Average Forecast",
                value=format_currency(avg_forecast)
            )
    
    with col3:
        if regional_forecast is not None:
            total_regions = regional_forecast['Region'].nunique()
            st.metric(
                label="Regions Analyzed",
                value=total_regions
            )
    
    with col4:
        if national_forecast is not None:
            forecast_periods = len(national_forecast)
            st.metric(
                label="Forecast Periods",
                value=forecast_periods
            )
    
    # Overview charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 National Sales Forecast Trend")
        if national_forecast is not None:
            fig = go.Figure()
            
            # Add forecast line
            fig.add_trace(go.Scatter(
                x=national_forecast['ds'],
                y=national_forecast['yhat'],
                mode='lines+markers',
                name='Forecast',
                line=dict(color='#1f77b4', width=3),
                marker=dict(size=6)
            ))
            
            # Add confidence interval
            fig.add_trace(go.Scatter(
                x=national_forecast['ds'].tolist() + national_forecast['ds'].tolist()[::-1],
                y=national_forecast['yhat_upper'].tolist() + national_forecast['yhat_lower'].tolist()[::-1],
                fill='toself',
                fillcolor='rgba(31, 119, 180, 0.2)',
                line=dict(color='rgba(255,255,255,0)'),
                name='Confidence Interval'
            ))
            
            fig.update_layout(
                title="National Sales Forecast with Confidence Intervals",
                xaxis_title="Date",
                yaxis_title="Sales ($)",
                hovermode='x unified',
                showlegend=True,
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🗺️ Regional Forecast Comparison")
        if regional_forecast is not None:
            # Get latest forecast for each region
            latest_by_region = regional_forecast.groupby('Region')['yhat'].last().reset_index()
            
            fig = px.bar(
                latest_by_region,
                x='Region',
                y='yhat',
                color='Region',
                title="Latest Forecast by Region",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            
            fig.update_layout(
                xaxis_title="Region",
                yaxis_title="Sales ($)",
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)

elif page == "📈 National Forecast":
    st.markdown('<h1 class="main-header">National Sales Forecast</h1>', unsafe_allow_html=True)
    
    if national_forecast is not None:
        # Date range selector
        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input(
                "Start Date",
                value=national_forecast['ds'].min(),
                min_value=national_forecast['ds'].min(),
                max_value=national_forecast['ds'].max()
            )
        
        with col2:
            end_date = st.date_input(
                "End Date",
                value=national_forecast['ds'].max(),
                min_value=national_forecast['ds'].min(),
                max_value=national_forecast['ds'].max()
            )
        
        # Filter data based on date range
        filtered_data = national_forecast[
            (national_forecast['ds'] >= pd.Timestamp(start_date)) &
            (national_forecast['ds'] <= pd.Timestamp(end_date))
        ]
        
        # Main forecast chart
        fig = go.Figure()
        
        # Add forecast line
        fig.add_trace(go.Scatter(
            x=filtered_data['ds'],
            y=filtered_data['yhat'],
            mode='lines+markers',
            name='Forecast',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=8)
        ))
        
        # Add confidence intervals
        fig.add_trace(go.Scatter(
            x=filtered_data['ds'].tolist() + filtered_data['ds'].tolist()[::-1],
            y=filtered_data['yhat_upper'].tolist() + filtered_data['yhat_lower'].tolist()[::-1],
            fill='toself',
            fillcolor='rgba(31, 119, 180, 0.2)',
            line=dict(color='rgba(255,255,255,0)'),
            name='Confidence Interval'
        ))
        
        fig.update_layout(
            title="National Sales Forecast with Confidence Intervals",
            xaxis_title="Date",
            yaxis_title="Sales ($)",
            hovermode='x unified',
            showlegend=True,
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Statistics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Average Forecast",
                format_currency(filtered_data['yhat'].mean())
            )
        
        with col2:
            st.metric(
                "Maximum Forecast",
                format_currency(filtered_data['yhat'].max())
            )
        
        with col3:
            st.metric(
                "Minimum Forecast",
                format_currency(filtered_data['yhat'].min())
            )
        
        # Monthly breakdown
        st.subheader("📅 Monthly Forecast Breakdown")
        monthly_avg = filtered_data.groupby('Month')['yhat'].mean().reset_index()
        
        fig = px.bar(
            monthly_avg,
            x='Month',
            y='yhat',
            title="Average Monthly Forecast",
            color='yhat',
            color_continuous_scale='viridis'
        )
        
        fig.update_layout(
            xaxis_title="Month",
            yaxis_title="Average Sales ($)",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

elif page == "🗺️ Regional Analysis":
    st.markdown('<h1 class="main-header">Regional Sales Analysis</h1>', unsafe_allow_html=True)
    
    if regional_forecast is not None:
        # Region selector
        selected_regions = st.multiselect(
            "Select Regions to Compare:",
            options=regional_forecast['Region'].unique(),
            default=regional_forecast['Region'].unique()
        )
        
        if selected_regions:
            filtered_regional = regional_forecast[regional_forecast['Region'].isin(selected_regions)]
            
            # Regional comparison chart
            fig = px.line(
                filtered_regional,
                x='ds',
                y='yhat',
                color='Region',
                title="Regional Sales Forecast Comparison",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            
            fig.update_layout(
                xaxis_title="Date",
                yaxis_title="Sales ($)",
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Regional statistics
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📊 Regional Performance Summary")
                regional_stats = filtered_regional.groupby('Region').agg({
                    'yhat': ['mean', 'max', 'min', 'std']
                }).round(2)
                regional_stats.columns = ['Average', 'Maximum', 'Minimum', 'Std Dev']
                st.dataframe(regional_stats, use_container_width=True)
            
            with col2:
                st.subheader("🏆 Top Performing Regions")
                latest_by_region = filtered_regional.groupby('Region')['yhat'].last().sort_values(ascending=False)
                
                fig = px.bar(
                    x=latest_by_region.index,
                    y=latest_by_region.values,
                    title="Latest Forecast by Region",
                    color=latest_by_region.values,
                    color_continuous_scale='viridis'
                )
                
                fig.update_layout(
                    xaxis_title="Region",
                    yaxis_title="Sales ($)",
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)

elif page == "📊 Performance Metrics":
    st.markdown('<h1 class="main-header">Performance Metrics</h1>', unsafe_allow_html=True)
    
    if national_forecast is not None and monthly_sales_national is not None:
        # Merge historical and forecast data
        historical_data = monthly_sales_national.copy()
        historical_data['Type'] = 'Historical'
        
        forecast_data = national_forecast[['ds', 'yhat']].copy()
        forecast_data.columns = ['Date', 'Sales']
        forecast_data['Type'] = 'Forecast'
        
        # Combine data for analysis
        combined_data = pd.concat([
            historical_data[['Date', 'Sales', 'Type']],
            forecast_data[['Date', 'Sales', 'Type']]
        ]).sort_values('Date')
        
        # Performance metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            historical_avg = historical_data['Sales'].mean()
            st.metric(
                "Historical Average",
                format_currency(historical_avg)
            )
        
        with col2:
            forecast_avg = forecast_data['Sales'].mean()
            st.metric(
                "Forecast Average",
                format_currency(forecast_avg)
            )
        
        with col3:
            growth_rate = calculate_growth_rate(forecast_avg, historical_avg)
            st.metric(
                "Growth Rate",
                f"{growth_rate:.1f}%",
                delta=f"{growth_rate:.1f}%"
            )
        
        with col4:
            volatility = combined_data['Sales'].std()
            st.metric(
                "Volatility (Std Dev)",
                format_currency(volatility)
            )
        
        # Performance comparison chart
        fig = go.Figure()
        
        # Historical data
        fig.add_trace(go.Scatter(
            x=historical_data['Date'],
            y=historical_data['Sales'],
            mode='lines+markers',
            name='Historical',
            line=dict(color='#ff7f0e', width=2),
            marker=dict(size=6)
        ))
        
        # Forecast data
        fig.add_trace(go.Scatter(
            x=forecast_data['Date'],
            y=forecast_data['Sales'],
            mode='lines+markers',
            name='Forecast',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title="Historical vs Forecast Performance",
            xaxis_title="Date",
            yaxis_title="Sales ($)",
            hovermode='x unified',
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Seasonal analysis
        st.subheader("📅 Seasonal Analysis")
        
        # Monthly averages
        monthly_historical = historical_data.groupby(historical_data['Date'].dt.month)['Sales'].mean()
        monthly_forecast = forecast_data.groupby(forecast_data['Date'].dt.month)['Sales'].mean()
        
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=months,
            y=monthly_historical.values,
            name='Historical',
            marker_color='#ff7f0e'
        ))
        
        fig.add_trace(go.Bar(
            x=months,
            y=monthly_forecast.values,
            name='Forecast',
            marker_color='#1f77b4'
        ))
        
        fig.update_layout(
            title="Monthly Average Sales Comparison",
            xaxis_title="Month",
            yaxis_title="Average Sales ($)",
            barmode='group',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        <p>📊 Sales Forecasting Dashboard | Built with Streamlit and Plotly</p>
        <p>Data-driven insights for strategic decision making</p>
    </div>
    """,
    unsafe_allow_html=True
) 