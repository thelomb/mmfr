import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    _SCHEMA_PATH = os.path.join(basedir, '..', 'data/mmfr')
    _SCHEMA_NAME = 'MMF_Regulatory_reporting_MoneyMarketFundReportV01_auth_093_001_01.xsd'
    _VALIDATED_TEST_FILE_NAME = 'test3.xml'
    SCHEMA_NAME_PATH = os.path.join(_SCHEMA_PATH, _SCHEMA_NAME)
    TEST_FILE_NAME_PATH = os.path.join(_SCHEMA_PATH, _VALIDATED_TEST_FILE_NAME)
