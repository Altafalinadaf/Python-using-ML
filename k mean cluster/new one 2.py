import tkinter as tk
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

# Load and preprocess dataset
dataset = pd.read_csv('C:/Users/altaf/OneDrive/Documents/loan_train11.csv')  # Replace with your dataset path

# Fill missing values
dataset['Gender'].fillna(dataset['Gender'].mode()[0], inplace=True)
dataset['Married'].fillna(dataset['Married'].mode()[0], inplace=True)
dataset['Education'].fillna(dataset['Education'].mode()[0], inplace=True)
dataset['Self_Employed'].fillna(dataset['Self_Employed'].mode()[0], inplace=True)
dataset['Loan_Amount'].fillna(dataset['Loan_Amount'].mean(), inplace=True)
dataset['Loan_Amount_Term'].fillna(dataset['Loan_Amount_Term'].mode()[0], inplace=True)
dataset['Credit_History'].fillna(dataset['Credit_History'].mode()[0], inplace=True)

# Encode categorical variables
dataset['Gender'] = dataset['Gender'].map({'Male': 1, 'Female': 0})
dataset['Married'] = dataset['Married'].map({'Yes': 1, 'No': 0})
dataset['Education'] = dataset['Education'].map({'Graduate': 1, 'Not Graduate': 0})
dataset['Self_Employed'] = dataset['Self_Employed'].map({'Yes': 1, 'No': 0})
dataset['Property_Area'] = dataset['Property_Area'].map({'Urban': 2, 'Semiurban': 1, 'Rural': 0})
dataset['Loan_Status'] = dataset['Loan_Status'].map({'Y': 1, 'N': 0}).astype(int)

# Define features and target
x = dataset[['Gender', 'Married', 'Education', 'Self_Employed', 'Loan_Amount',
             'Loan_Amount_Term', 'Credit_History', 'Property_Area']]
y = dataset['Loan_Status']

# Split data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Scale the data
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Train the model
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(x_train, y_train)

# Create the GUI
window = tk.Tk()
window.title("Loan Prediction")
window.geometry("600x600")

# Input labels and text boxes
tk.Label(window, text="Enter Gender (1=Male, 0=Female):").place(x=100, y=50)
txt1 = tk.Entry(window, width=20)
txt1.place(x=300, y=50)

tk.Label(window, text="Enter Married (1=Yes, 0=No):").place(x=100, y=90)
txt2 = tk.Entry(window, width=20)
txt2.place(x=300, y=90)

tk.Label(window, text="Enter Education (1=Graduate, 0=Not Graduate):").place(x=100, y=130)
txt3 = tk.Entry(window, width=20)
txt3.place(x=300, y=130)

tk.Label(window, text="Enter Self Employed (1=Yes, 0=No):").place(x=100, y=170)
txt4 = tk.Entry(window, width=20)
txt4.place(x=300, y=170)

tk.Label(window, text="Enter Loan Amount:").place(x=100, y=210)
txt5 = tk.Entry(window, width=20)
txt5.place(x=300, y=210)

tk.Label(window, text="Enter Loan Amount Term:").place(x=100, y=250)
txt6 = tk.Entry(window, width=20)
txt6.place(x=300, y=250)

tk.Label(window, text="Enter Credit History (1=Yes, 0=No):").place(x=100, y=290)
txt7 = tk.Entry(window, width=20)
txt7.place(x=300, y=290)

tk.Label(window, text="Enter Property Area (2=Urban, 1=Semiurban, 0=Rural):").place(x=100, y=330)
txt8 = tk.Entry(window, width=20)
txt8.place(x=300, y=330)

# Prediction function
def output():
    global l12, l13

    # Get inputs from the user
    Gender = int(txt1.get())
    Married = int(txt2.get())
    Education = int(txt3.get())
    Self_Employed = int(txt4.get())
    LoanAmount = float(txt5.get())
    Loan_Amount_Term = float(txt6.get())
    Credit_History = int(txt7.get())
    Property_Area = int(txt8.get())

    # Prepare input for the model
    newEmp = sc.transform([[Gender, Married, Education, Self_Employed, 
                            LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]])
    result = model.predict(newEmp)

    # Calculate accuracy
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred) * 100

    l13 = tk.Label(window, text=f"Accuracy of the Model: {accuracy:.2f}%", width=40, height=2, bg='pink')
    l13.place(x=160, y=460)

    if result[0] == 0:
        l12 = tk.Label(window, text="Person is NOT Applicable for Loan", width=40, height=2, bg='pink')
    else:
        l12 = tk.Label(window, text="Person is Applicable for Loan", width=40, height=2, bg='pink')

    l12.place(x=160, y=420)

# Predict button
btn = tk.Button(window, text="Predict", command=output, bg='green', fg='white')
btn.place(x=250, y=370)

window.mainloop()
