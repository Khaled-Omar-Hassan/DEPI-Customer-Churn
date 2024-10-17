import streamlit as st
import Model
import sys
sys.path.append('../')

st.title('Customer Churn Prediction')
st.write('Enter the details to predict')

# Add a selectbox to the sidebar:
Payment_Method = st.selectbox('Payment Method', ["Credit Card", "PayPal", "Cash", "Crypto"])
Product_Category = st.selectbox('Product Category', ["Clothing", "Books", "Electronics", "Home"])
Gender = st.selectbox('Gender', ['Male', 'Female'])  # Updated to list gender options
Product_Price = st.number_input('Product Price', min_value=1)
Quantity = st.number_input('Quantity', min_value=1)
Total_Purchase_Amount = st.number_input('Total Purchase Amount', min_value=1)
Customer_Age = st.number_input('Customer Age', step=1, min_value=0)  # Ensure min_value is set to 0
Returns = st.number_input('Returns', min_value=0)

# Create boolean variables based on user input
Gender_Male = 1 if Gender == 'Male' else 0
Payment_Method_Credit_Card = 1 if Payment_Method == 'Credit Card' else 0
Payment_Method_Crypto = 1 if Payment_Method == 'Crypto' else 0
Payment_Method_PayPal = 1 if Payment_Method == 'PayPal' else 0
Product_Category_Clothing = 1 if Product_Category == 'Clothing' else 0
Product_Category_Electronics = 1 if Product_Category == 'Electronics' else 0
Product_Category_Home = 1 if Product_Category == 'Home' else 0

if st.button('Predict'):
    # Call the prediction function
    result = Model.predict_delay(
        Product_Price, Quantity, Total_Purchase_Amount, Customer_Age,
        Returns, Gender_Male, Payment_Method_Credit_Card, 
        Payment_Method_Crypto, Payment_Method_PayPal,
        Product_Category_Clothing, Product_Category_Electronics,
        Product_Category_Home
    )
    print(result)
    st.success('The predicted churn likelihood is {}'.format(result[0]))
