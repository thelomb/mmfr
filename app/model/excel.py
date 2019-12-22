from openpyxl import Workbook, load_workbook
import sys

class Reader():
    def __init__(self, sheetname='Sheet1'):
        self.data = {}
        self.range = []
        self.sheetname = sheetname

    def parse(self, path):
        wb = load_workbook(path, read_only=True)
        sheet = wb[self.sheetname]
        for i in range(1, sheet.max_row):
            line = dict()
            x = 0
            for header in list(sheet.iter_rows())[0]:
                line[header.value] = list(sheet.iter_rows())[i][x].value
                x += 1
            self.range.append(line)
        return self.range

class XLType():
    def __init__(self, cls):
        self.cls = cls

    def clean(self, v):
        return getattr(sys.modules[__name__], self.cls)().clean(v)

class XLString():
    @staticmethod
    def clean(v):
        if v:
            return str(v).strip()
        return v

class XLDate():
    @staticmethod
    def clean(v):
        if v:
            return v.date().isoformat()
        return v

class XLBool:
    @staticmethod
    def clean(v):
        return v in ['Yes', 'YES']

class XLEnum:
    mapping = {}
    @classmethod
    def clean(cls, value):
        if isinstance(value, str):
            space = str.maketrans(dict.fromkeys(' '))
            value = value.translate(space)
            return cls.mapping[value.lower()]
        return value

class MMFMasterFeedType(XLEnum):
    mapping = { 'fder': 'FDER',
                'mstr': 'MSTR',
                'none': 'NONE',
                'feeder': 'FDER',
                'master': 'MSTR'
    }

class MMFType(XLEnum):
    mapping = { 'shorttermlvnavmoneymarketfund': 'STLV',
                'shorttermpublicdebtcnavmoneymarketfund': 'STCN',
                'shorttermvnavmoneymarketfund': 'STVN',
                'standardvnavmoneymarketfund': 'SDVN',
                'ShortTermLVNAVMoneyMarketFund': 'STLV',
                'ShortTermPublicDebtCNAVMoneyMarketFund': 'STCN',
                'ShortTermVNAVMoneyMarketFund': 'STVN',
                'StandardVNAVMoneyMarketFund': 'SDVN',
                'shorttermlvnavmmf': 'STLV',
                'shorttermpublicdebtcnavmmf': 'STCN',
                'shorttermvnavmmf': 'STVN',
                'standardvnavmmf': 'SDVN'
    }


class MMFLegalFramework(XLEnum):
    mapping = { 'UCITS': 'UCIT',
                'AIFD': 'AIFD',
                'UCIT': 'UCIT',
                'ucit': 'UCIT',
                'aifd': 'AIFD',
                'UndertakingsForCollectiveInvestmentInTransferableSecurities': 'UCIT',
                'AlternativeInvestmentFund': 'AIFD'
    }

class XLList:
    @staticmethod
    def clean(v):
        return v.split(';')

class XLNumeric:
    @staticmethod
    def clean(v):
        return v