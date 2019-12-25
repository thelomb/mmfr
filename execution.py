from app.mmfr_report import mmfr

output = 'app/output/test.xml'
static_data = {'file': 'app/input/20191205 SA MMFR Foundational Data Report v3.xlsx'}
position_data =  {'file': 'app/input/20191220 Position Report Citi SS.xlsx', 'sheet': 'Position Data Citi SS final'}
stress_test_data =  {'file': 'app/input/20191220 Position Report Citi SS.xlsx', 'sheet': 'Position Data Citi SS final'}
performance_data =  {'file': 'app/input/20191220 Position Report Citi SS.xlsx', 'sheet': 'Position Data Citi SS final'}
liability_data =  {'file': 'app/input/20191220 Position Report Citi SS.xlsx', 'sheet': 'Position Data Citi SS final'}
volatility_data =  {'file': 'app/input/20191220 Position Report Citi SS.xlsx', 'sheet': 'Position Data Citi SS final'}
mmfr(output=output, static_date_file=static_data, position_data_file=position_data)