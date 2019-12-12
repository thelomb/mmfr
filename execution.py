from model.document import Document
from xmlschema import XMLSchema
from lxml import etree
from model.interface import Data

data = Data()
data.from_itself()
d = Document()
d.static_block(data)
d.dynamic_block()

xsd = XMLSchema('data/PLO_MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd')
if xsd.is_valid(d.to_xml('output/test.xml')):
    print('🥳😜')
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse('output/test.xml', parser)
    tree.write('output/test_beautiful.xml', pretty_print=True)
else:
    print('🧐🤨')


