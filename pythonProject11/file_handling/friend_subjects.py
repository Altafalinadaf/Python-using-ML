import pandas as pd


# Create a DataFrame with friends and their favorite subjects

data = {

'Name': [],

'Favorite Subject': []

}


# Collect data from the user

for i in range(2):
    name = input(f"Enter the name of friend {i+1}: ")

    subject = input(f"Enter their favorite subject: ")

    data['Name'].append(name)

    data['Favorite Subject'].append(subject)


# Create a DataFrame

df = pd.DataFrame(data)


# Save the DataFrame to an Excel file

file_name = 'friends_subjects.xlsx'

df.to_excel(file_name, index=False)

print("The Excel file has been created and saved as", file_name)