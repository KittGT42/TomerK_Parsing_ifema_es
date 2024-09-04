import pandas as pd

read_file = pd.read_csv('detailed_info_company.csv')
read_file.to_excel('detailed_info_company_ex.xlsx', index=None, header=True)