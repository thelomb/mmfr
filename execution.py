from model.document import Document
from xmlschema import XMLSchema
from lxml import etree
from model.interface import StaticData
from model.excel import Reader

xl_static_data = Reader()
xl_static_data.parse('input/20191205 SA MMFR Foundational Data Report v3.xlsx')
static_fund_data = StaticData()
static_fund_data.from_itself(data=xl_static_data.data)
d = Document()
d.Upd.RptgYr = static_fund_data.RptgYr
d.Upd.RptgPrdFrToQrtr = static_fund_data.RptgPrdFrToQrtr
d.Upd.RptgPrd = static_fund_data.RptgPrd
d.Upd.FndData = static_fund_data.FndData

d.dynamic_block()

xsd = XMLSchema('data/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd')
if xsd.is_valid(d.to_xml('output/test.xml')):
    print('🥳😜')
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse('output/test.xml', parser)
    tree.write('output/test_beautiful.xml', pretty_print=True)
else:
    print('🧐🤨')
