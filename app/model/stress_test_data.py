from app.model.fund_calc import StressTestResult
from app.model import pmmfr

class StressTest:

    def __init__(self):
        self.details = ''

    def from_dict(self, record):
        print('in class:', record)
        self.details = StressTestResult(test_date=record['test_date'],
                                        net_asset_value_basis=record['net_asset_value_basis'],
                                        code=record['code'],
                                        impact=record['impact'],
                                        input_factor=record['input_factor'],
                                        comment=record['comment'])


class ActionPlan(pmmfr.ActionPlan1Choice__1):
    def __init__(self, action_plan=None):
        super().__init__()
        if action_plan:
            self.PropsdActnPlan = pmmfr.Max2000Text(action_plan)
        else:
            self.NoVlnrblty = pmmfr.NoVulnerability1Code_fixed('NOVN')