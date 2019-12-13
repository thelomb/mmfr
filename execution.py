from xmlschema import XMLSchema
from lxml import etree
from model.excel import Reader
from model.report import Report

def mmfr(output, static_date_file, position_data_file = None):
    xl_static_data = Reader()
    static_data = xl_static_data.parse(static_date_file)
    r = Report()
    r.static_data(static_data)
    r.dynamic_data()
    xsd = XMLSchema('data/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd')
    if xsd.is_valid(r.to_xml(output)):
        print('🥳😜')
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(output, parser)
        beautiful_output = output.replace('.xml', '_beautiful.xml')
        tree.write(beautiful_output, pretty_print=True)
    else:
        print('🧐🤨')

output = 'output/test.xml'
static_data = 'input/20191205 SA MMFR Foundational Data Report v3.xlsx'
mmfr(output=output, static_date_file=static_data)