import unittest
from core import ids, settings


class IdsTestCase(unittest.TestCase):
	
	def testRuleLoader(self):
		"""docstring for testRuleLoader"""
		loader = ids.RuleLoader(settings.RULES_LOCATION)
		rules = loader.loadRules()
		self.assertEquals(len(rules),67)

	def testCentrifuge(self):
                centrifuge = ids.Centrifuge()
                self.assertEquals(centrifuge.doCentrifuge('SR'),False)
                self.assertEquals(centrifuge.doCentrifuge('">XXXXXXXX'),True)
	
