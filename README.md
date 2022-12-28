#compile_csv_files_into_excel_with_path_sheetnames
This code helps you to merge all CSV files inside a directory and its subdirectories into a single Excel file, which can be useful for statistical analysis. The sheet names in the Excel file will be the names of the folders containing the files, providing an easy way to identify the source of the data.
If you run the code on this directory, the Excel file will have four sheets, one for each CSV file. The sheet names will be the names of the folders containing the files, followed by the names of the files. For example, the sheet names will be:
/Users/your directory which gets the csv files/
├── folder1
│   ├── file1.csv
│   └── file2.csv
└── folder2
    ├── file3.csv
    └── file4.csv
result of the recorded sheet names in output excell file would be: 
folder1_file1.csv
folder1_file2.csv
folder2_file3.csv
folder2_file4.csv
Just be careful to consider this issue that in the sheets most of the times you can not save more than 31 characters, you if you got this massage: Excel worksheet name 'something_in_your_path_names.csv' must be <= 31 chars, so you should correct the folders name into smaller names. Good luck
