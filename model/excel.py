from openpyxl import Workbook, load_workbook

class Reader():
    def __init__(self):
        self.data = {}

    def parse(self, path):
        wb = load_workbook(path, read_only=True)
        sheet = wb['Sheet1']
        for i in range(1, 2):
            line = dict()
            x = 0
            for header in list(sheet.iter_rows())[0]:
                line[header.value] = list(sheet.iter_rows())[i][x].value
                x += 1
        print(line)
        sc_type = line['A.3.6_a_Shareclass_Name_MMF'].split(';') #A-2;I-2;I-3;J-3;K-1;K-3;L-1;L-3;X-2;Y-2;Z-1;Z-2;Z-3'.split(";")
        sc_isin = line['A.3.6_b_Shareclass_ISINS_MMF'].split(';') #LU0049015760;LU0108940692;LU0966092727;LU0966092990;LU0643933087;LU0966093022;LU0779217453;LU0966093295;LU1914336968;LU2027372429;LU0643933160;LU0147471253;LU0966093378'.split(
        sc_ccy = line['A.3.7_a_Shareclass_Currencies_MMF'].split(';') # GBP;GBP;GBP;GBP;GBP;GBP;GBP;GBP;GBP;GBP;GBP;GBP;GBP'.split(";")
        if len(sc_ccy) == len(sc_isin) and len(sc_type) == len(sc_ccy):
            share_classes = []
            for i in range(len(sc_isin) - 1):
                sc = {'isin': sc_isin[i],
                      'ccy': sc_ccy[i],
                      'type': sc_type[i]}
                share_classes.append(sc)
        line['share_classes'] = share_classes
        line['dist_countries'] = line['A.1.10_Member_State_Marketing_MMF'].split(sep=';')
        self.data = line

