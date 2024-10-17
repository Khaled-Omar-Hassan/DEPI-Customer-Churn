import joblib
import pandas as pd

# Load necessary models and lists
inputs = joblib.load('models/input.h5')
random_forest = joblib.load('models/random_forest.h5')

def predict_delay(
        Product_Price, Quantity, Total_Purchase_Amount, Customer_Age,
        Returns, Gender_Male, Payment_Method_Credit_Card, Payment_Method_Crypto,
        Payment_Method_PayPal, Product_Category_Clothing, Product_Category_Electronics,
        Product_Category_Home
):
    # Create DataFrame for the model input
    test_df = pd.DataFrame(columns=inputs)
    test_df.at[0, 'Product Price'] = Product_Price
    test_df.at[0, 'Quantity'] = Quantity
    test_df.at[0, 'Total Purchase Amount'] = Total_Purchase_Amount
    test_df.at[0, 'Customer Age'] = Customer_Age
    test_df.at[0, 'Returns'] = Returns
    test_df.at[0, 'Gender_Male'] = Gender_Male
    test_df.at[0, 'Payment Method_Credit Card'] = Payment_Method_Credit_Card
    test_df.at[0, 'Payment Method_Crypto'] = Payment_Method_Crypto
    test_df.at[0, 'Payment Method_PayPal'] = Payment_Method_PayPal
    test_df.at[0, 'Product Category_Clothing'] = Product_Category_Clothing
    test_df.at[0, 'Product Category_Electronics'] = Product_Category_Electronics
    test_df.at[0, 'Product Category_Home'] = Product_Category_Home

    try:
        result = random_forest.predict_proba(test_df) 
    except Exception as e:
        return f"Error during prediction: {str(e)}"
    return result

print(inputs)
