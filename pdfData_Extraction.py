import os
import pandas as pd
from pdfrw import PdfReader


def extract_pdf_data_to_csv(folder_path, csv_path):
    # Initialize a list to store all data across files
    all_data = []

    # Iterate through each PDF file in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, file_name)
            pdf = PdfReader(pdf_path)

            # Extract form fields data
            for page in pdf.pages:
                if '/Annots' in page:
                    for field in page['/Annots']:
                        field_data = field['/T']  # Field name
                        field_value = field['/V']  # Field value
                        all_data.append({
                            'File Name': file_name,
                            'Field Name': field_data if field_data else 'Unknown',
                            'Field Value': field_value if field_value else ''
                        })

    # Convert the accumulated data into a DataFrame and save it to a CSV file
    df = pd.DataFrame(all_data)
    df.to_csv(csv_path, index=False)
    print(
        f"Data extracted from {len(all_data)} fields across {len(os.listdir(folder_path))} files and saved to {csv_path}")


# Usage example
folder_path = 'E:\\Parth Patel\\Temp PDF\\Fw9'
csv_path = 'E:\\Parth Patel\\Temp PDF\\output.csv'
extract_pdf_data_to_csv(folder_path, csv_path)
