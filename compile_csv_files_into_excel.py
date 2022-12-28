import glob
import pandas as pd
import re
# Get a list of all CSV files in the directory and its subdirectories.
csv_files = glob.glob('/Users/your files address, following asterisk "*" should be include, don`t remove it /**/**/*.csv', recursive=True)
# Create an ExcelWriter
excel_writer = pd.ExcelWriter('/Users/your destination for save single file/output.xlsx', engine='xlsxwriter')
# Looping CSV files

for csv_file in csv_files:
  # Read the CSV file into a DataFrame
  df = pd.read_csv(csv_file)
  # Split the file path into its individual components
  path_components = csv_file.split('/')

  #remove invalid characters from the file name, in below, before file_name there I added '_' cause every file which containg csv files to be seperated by underscore.
  file_name = path_components[-1]
  file_name = re.sub(r'[\[\]:*?/\\\']', '_', file_name)

  #the name of the folder containing the file, underscore have the previously described function.
  folder_name = path_components[-2]
  folder_name = re.sub(r'[\[\]:*?/\\\']|\.csv', '_', folder_name)

  #sheet name by combining the folder name and file name which follows asterstisk rule
  sheet_name = f"{folder_name}_{file_name}"
  df.to_excel(excel_writer, sheet_name=sheet_name)
# Save the result
excel_writer.save()
