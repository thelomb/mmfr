class Error(Exception):
    pass

class FundStaticDataError(Error):
    pass

class ReportingDateError(FundStaticDataError):
    pass

class EmptyDate(ReportingDateError):
    pass
