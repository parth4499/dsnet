import pandas as pd

excel_file_path = "path/to/your/excel_file.xlsx"

# Read the Excel file into a Pandas DataFrame
df = pd.read_excel(excel_file_path)

# Now, 'df' contains the data from the Excel file
print(df)