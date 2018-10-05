"""
Listing sheets in Excel files:
Use pandas to import Excel spreadsheets and list the names of the sheets in any loaded .xlsx file.

Recall from the video that, given an Excel file imported into a variable spreadsheet, you can retrieve a list of the
sheet names using the attribute spreadsheet.sheet_names.

Specifically, you'll be loading and checking out the spreadsheet 'battledeath.xlsx', modified from the Peace Research
Institute Oslo's (PRIO) dataset. This data contains age-adjusted mortality rates due to war in various countries over
several years. (https://www.prio.org/Data/Armed-Conflict/Battle-Deaths/The-Battle-Deaths-Dataset-version-30/)

INSTRUCTIONS
* Assign the filename to the variable file.
* Pass the correct argument to pd.ExcelFile() to load the file using pandas.
* Print the sheetnames of the Excel spreadsheet by passing the necessary argument to the print() function.
"""


# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = r'../_datasets/battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xl.parse(0)

# Print the head of the DataFrame df2
print(df2.head())
