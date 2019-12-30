from xmlschema import XMLSchema
from lxml import etree
from app.model.excel import Reader
from app.model.report import Report

def mmfr(output, static_date_file, position_data_file = None):
    static_data = Reader().parse(static_date_file.get('file'), static_date_file.get('sheet') or None)
    print('static data read')
    position_data = Reader().parse(position_data_file.get('file'), position_data_file.get('sheet') or None)
    print('position data read')
    r = Report()
    r.static_data(static_data)
    r.position_data(position_data)
    r.stress_test_data()
    r.dynamic_data()
    xsd = XMLSchema('app/data/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd')
    if xsd.is_valid(r.to_xml(output)):
        print('🥳😜')
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(output, parser)
        beautiful_output = output.replace('.xml', '_beautiful.xml')
        tree.write(beautiful_output, pretty_print=True)
    else:
        print('🧐🤨')