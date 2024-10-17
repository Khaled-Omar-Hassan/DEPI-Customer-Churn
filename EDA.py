import pandas as pd
import plotly.express as px

df = pd.read_csv('sources/data/ecommerce_customer_data_custom_ratios.csv')


# 1. Churn Rate by Age Group
def churn_rate_by_age_group(df):
    age_groups = pd.cut(df['Customer Age'], bins=[0, 20, 30, 40, 50, 60], labels=['0-20', '21-30', '31-40', '41-50', '51-60'])
    df['Age Group'] = age_groups
    churn_rate_age = df.groupby('Age Group')['Churn'].mean().reset_index()

    fig1 = px.bar(churn_rate_age, 
                  x='Age Group', 
                  y='Churn', 
                  title='Churn Rate by Age Group',
                  labels={'Churn': 'Churn Rate'},
                  color='Churn',  
                  color_continuous_scale='Blues')

    fig1.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12),
        xaxis_title='Age Group',
        yaxis_title='Churn Rate',
        yaxis_tickformat='.2%'  # Show churn rate as percentage
    )
    return fig1

# 2. Churn Rate by Product Category
def churn_rate_by_product_category(df):
    churn_rate_category = df.groupby('Product Category')['Churn'].mean().reset_index()

    fig2 = px.bar(churn_rate_category, 
                  x='Product Category', 
                  y='Churn', 
                  title='Churn Rate by Product Category',
                  labels={'Churn': 'Churn Rate'},
                  color_discrete_sequence=px.colors.sequential.Blues_r)  # Custom blue tones

    fig2.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12),
        xaxis_title='Product Category',
        yaxis_title='Churn Rate',
        yaxis_tickformat='.2%'
    )
    return fig2

# 3. Churn Rate by Payment Method
def churn_rate_by_payment_method(df):
    churn_rate_payment = df.groupby('Payment Method')['Churn'].mean().reset_index()

    fig3 = px.bar(churn_rate_payment, 
                  x='Payment Method', 
                  y='Churn', 
                  title='Churn Rate by Payment Method',
                  labels={'Churn': 'Churn Rate'},
                  color_discrete_sequence=px.colors.sequential.Blues)  # Custom blue tones

    fig3.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12),
        xaxis_title='Payment Method',
        yaxis_title='Churn Rate',
        yaxis_tickformat='.2%'
    )
    return fig3

# 6. Distribution of Total Purchase Amounts
def distribution_of_purchase_amounts(df):
    fig = px.histogram(df, 
                       x='Total Purchase Amount', 
                       nbins=50, 
                       title='Distribution of Total Purchase Amounts',
                       color_discrete_sequence=px.colors.sequential.Aggrnyl)  # Aqua/blue tones

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12),
        xaxis_title='Total Purchase Amount',
        yaxis_title='Frequency'
    )
    return fig

# 7. Seasonal Trends in Purchase Behavior
def seasonal_trends(df):
    df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])
    df['Month'] = df['Purchase Date'].dt.month
    purchases_by_month = df.groupby('Month')['Total Purchase Amount'].sum().reset_index()

    fig = px.line(purchases_by_month, 
                  x='Month', 
                  y='Total Purchase Amount', 
                  title='Seasonal Trends in Purchase Behavior',
                  color_discrete_sequence=px.colors.sequential.Blues)

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12),
        xaxis_title='Month',
        yaxis_title='Total Purchase Amount'
    )
    return fig

# 8. Returning vs Churned Customers by Product Category
def returning_vs_churned(df):
    churned_vs_returning = df.groupby(['Churn', 'Product Category'])['Total Purchase Amount'].sum().reset_index()

    fig = px.bar(churned_vs_returning, 
                 x='Product Category', 
                 y='Total Purchase Amount', 
                 color='Churn',
                 title='Returning vs Churned Customers by Product Category',
                 color_discrete_sequence=px.colors.sequential.Blues)

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12),
        xaxis_title='Product Category',
        yaxis_title='Total Purchase Amount'
    )
    return fig

# 9. Returns vs Customer Churn
def returns_vs_churn(df):
    returns_churn = df.groupby('Churn')['Returns'].mean().reset_index()

    fig = px.bar(returns_churn, 
                 x='Churn', 
                 y='Returns', 
                 title='Returns vs Customer Churn',
                 color_discrete_sequence=px.colors.sequential.Aggrnyl)  # Aqua tones

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12),
        xaxis_title='Churn',
        yaxis_title='Average Returns'
    )
    return fig

# 10. Average Price per Product Category
def avg_price_per_category(df):
    avg_price = df.groupby('Product Category')['Product Price'].mean().reset_index()

    fig = px.bar(avg_price, 
                 x='Product Category', 
                 y='Product Price', 
                 title='Average Price per Product Category',
                 color_discrete_sequence=px.colors.sequential.Aggrnyl)  # Aqua tones

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12),
        xaxis_title='Product Category',
        yaxis_title='Average Price'
    )
    return fig

# 11. Highest Revenue by Product Category
def highest_revenue_product_category(df):
    revenue_per_category = df.groupby('Product Category')['Total Purchase Amount'].sum().reset_index()

    fig = px.bar(revenue_per_category, 
                 x='Product Category', 
                 y='Total Purchase Amount', 
                 title='Highest Revenue by Product Category',
                 color_discrete_sequence=px.colors.sequential.Blues)  # Blue tones

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12),
        xaxis_title='Product Category',
        yaxis_title='Total Revenue'
    )
    return fig

# 12. Gender vs Product Category Preferences
def gender_vs_product_category(df):
    fig = px.histogram(df, 
                       x='Product Category', 
                       color='Gender', 
                       barmode='group', 
                       title='Gender vs Product Category Preferences',
                       color_discrete_sequence=px.colors.sequential.Blues)

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12),
        xaxis_title='Product Category',
        yaxis_title='Count'
    )
    return fig

# 13. Customer Age vs Payment Method Preferences
def age_vs_payment_method(df):
    fig = px.histogram(df, 
                       x='Customer Age', 
                       color='Payment Method', 
                       title='Customer Age vs Payment Method Preferences',
                       barmode='group',  # Grouped bars
                       color_discrete_sequence=px.colors.sequential.Aggrnyl)  # Aqua tones

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12),
        xaxis_title='Customer Age',
        yaxis_title='Count'
    )
    return fig
