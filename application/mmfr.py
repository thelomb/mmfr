from xmlschema import XMLSchema
from config import Config


mmfr_schema = XMLSchema(Config.SCHEMA_NAME_PATH)
print(mmfr_schema.is_valid(Config.TEST_FILE_NAME_PATH))
