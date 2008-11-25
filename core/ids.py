from xml.sax.handler import ContentHandler 
from xml.sax import parse
import logging
import re
class IdsRule(object):
	"""Model class for an ids rule"""
	def __init__(self):
		"""docstring for __init__"""
		self.rule = ""
		self.description = ""
		self.tags = []
		self.impact = 1
		
	def __str__(self):
		return self.description
	
class RuleHandler(ContentHandler):
	"""ContentHandler for xml rule files"""
	rules = []
	def __init__(self): 
		ContentHandler.__init__(self)
		self.data = []
		self.actualRule = IdsRule()
	def endElement(self, name):#REFACTORING!!!!!
		if name == 'rule':
			self.actualRule.rule = ''.join(self.data).strip() 
		if name == 'description':
			self.actualRule.description = ''.join(self.data).strip() 
		if name == 'impact':
			self.actualRule.impact = int(''.join(self.data))
		if name == 'tag':
			self.actualRule.tags.append(''.join(self.data).strip())
			logging.debug(len(self.actualRule.tags))
		if name == 'filter':
			self.rules.append(self.actualRule)
			logging.debug(self.actualRule)
			self.actualRule = IdsRule()
		if name != "tags":
			self.data = []

	def characters(self, string): 
		self.data.append(string)
			
	
		

class RuleLoader(object):
	"""simple loader for fules from standard xml file see https://svn.php-ids.org/svn/trunk/lib/IDS/default_filter.xml"""
	
	def __init__(self, filename):
		super(RuleLoader, self).__init__()
		self.filename = filename
		print(self.filename)
	
	def loadRules(self):
		"""return the list of IdsRules in the rules file"""
		handler = RuleHandler()
		parse(self.filename,handler)
		return handler.rules

class Centrifuge(object):
	"""The mithical centrifuge used to enhance regular expression execution"""
	def __init__(self):
		super(Centrifuge, self).__init__()
	
	def preg_replace(self,strPattern, place, stringdata):
		"""equivalent of PHP function"""
		pattern = re.compile(strPattern)
		return pattern.sub(place, stringdata)
	
	def doCentrifuge(self,stringToProbe):
		"""alfa implementation"""
		if len(stringToProbe) > 5:
		    #Check for the attack char ratio 
			result = self.preg_replace('/[\w\s\p{L}.,\/]*/ms', '', stringToProbe)
			stripped_length = len(result)
			overall_length  = len(self.preg_replace('/\w{3,}/', '123', self.preg_replace('/\s{2,}/ms', '', stringToProbe))) 
			if stripped_length != 0 and overall_length/stripped_length <= 3.5:
				return True
			else:
				return False
		else:
			return False
		

	
	
		
	
		