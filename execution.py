from app.mmfr_report import mmfr

output = 'app/output/test.xml'
static_data = 'app/input/20191205 SA MMFR Foundational Data Report v3.xlsx'
mmfr(output=output, static_date_file=static_data)