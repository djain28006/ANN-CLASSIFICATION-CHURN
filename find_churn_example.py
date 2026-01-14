import pandas as pd

# Load the dataset
df = pd.read_csv('Churn_Modelling.csv')

# Find rows where Exited is 1 (Churn)
churn_df = df[df['Exited'] == 1]

if not churn_df.empty:
    # Get the first matching row
    row = churn_df.iloc[0]
    
    print("Example Churn Input:")
    print(f"Geography: {row['Geography']}")
    print(f"Gender: {row['Gender']}")
    print(f"Age: {row['Age']}")
    print(f"Balance: {row['Balance']}")
    print(f"Credit Score: {row['CreditScore']}")
    print(f"Estimated Salary: {row['EstimatedSalary']}")
    print(f"Tenure: {row['Tenure']}")
    print(f"Number of Products: {row['NumOfProducts']}")
    print(f"Has Credit Card: {row['HasCrCard']}")
    print(f"Is Active Member: {row['IsActiveMember']}")
else:
    print("No churn examples found.")
