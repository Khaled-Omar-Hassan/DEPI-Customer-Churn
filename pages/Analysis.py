import sys
sys.path.append("../")

import streamlit as st
import EDA
from EDA import df

# Create the tabs
churn_analysis, product_pricing, seasonal_trends = st.tabs([
    'Churn Analysis', 'Product & Pricing', 'Seasonal Trends'
])

# Churn Analysis Tab
with churn_analysis:
    st.title("Churn Analysis")

    st.header("1- What is the average Churn rate by Age?")
    st.plotly_chart(EDA.churn_rate_by_age_group(df))

    st.header("2- What is the average Churn rate by Product Category?")
    st.plotly_chart(EDA.churn_rate_by_product_category(df))

    st.header("3- What is the average Churn rate by Payment Method?")
    st.plotly_chart(EDA.churn_rate_by_payment_method(df))

    st.header("4- Returns vs Customer Churn")
    st.plotly_chart(EDA.returns_vs_churn(df))

    st.header("5- Returning vs Churned Customers by Product Category")
    st.plotly_chart(EDA.returning_vs_churned(df))


# Product & Pricing Tab
with product_pricing:
    st.title("Product & Pricing Analysis")

    st.header("1- What is the average price per Product Category?")
    st.plotly_chart(EDA.avg_price_per_category(df))

    st.header("2- Which product categories generate the highest revenue?")
    st.plotly_chart(EDA.highest_revenue_product_category(df))

# Seasonal Trends Tab
with seasonal_trends:
    st.title("Seasonal Trends in Purchase Behavior")

    st.header("1- What are the seasonal trends in purchase behavior?")
    st.plotly_chart(EDA.seasonal_trends(df))

    st.header("2- What is the distribution of total purchase amounts?")
    st.plotly_chart(EDA.distribution_of_purchase_amounts(df))
