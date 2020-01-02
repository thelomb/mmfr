from app.input import mock
from app.report import ReportData

output = 'app/output/new.xml'
static_data = {'type': 'file',
               'path': 'app/input/20191205 SA MMFR Foundational Data Report v3.xlsx',
               'bindings': 'static_fund_data.json'}
position_data = {'type': 'file',
                 'path': 'app/input/20191220 Position Report Citi SS.xlsx', 'sheet': 'Position Data Citi SS final',
                 'bindings': 'position_fund_data_type.json'}
liability_data = {'type': 'mock',
                  'data': mock.MockLiability,
                  'bindings': 'liability_data_type.json'}
stress_test_data = {'type': 'mock',
                    'data': mock.MockStressTest,
                    'bindings': 'stress_test_data_type.json'}
performance_data = {'type': 'mock',
                    'data': mock.MockPerf,
                    'bindings': 'performance_data_type.json'}

report_data = ReportData(static_data=static_data,
                         position_data=position_data,
                         liability_data=liability_data,
                         stress_test_data=stress_test_data,
                         performance_data=performance_data)

report_data.generate_xml(output_path=output)
report_data.validate()