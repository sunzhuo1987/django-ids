import unittest
from djangoids.core import ids, settings


class IdsTestCase(unittest.TestCase):
	
	def testRuleLoader(self):
		"""docstring for testRuleLoader"""
		loader = ids.RuleLoader(settings.RULES_LOCATION)
		rules = loader.loadRules()
		self.assertEquals(len(rules),68)
	