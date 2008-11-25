import logging
import re
from core import ids, settings, models

class IdsMiddleware(object):
	"""Middleware for ids actions"""
	def __init__(self):
		super(IdsMiddleware, self).__init__()
		self.rules = ids.RuleLoader(settings.RULES_LOCATION).loadRules()
		logging.debug(len(self.rules))
		self.centrifuge = ids.Centrifuge()
		logging.debug("IDS WATCHING FOR BAD THINGS TO HAPPEN...")
	
	def	process_request(self, request):
		""" basic method to analize the request"""
		logging.debug("ids start checking")
		fields = request.REQUEST.items()
		for field in fields:
                        logging.debug("Checking " + field[1] + " " + str(self.centrifuge.doCentrifuge(field[1])) )
			if self.centrifuge.doCentrifuge(field[1]):
				self.applyRules(field, request)

	def doCounterStrike(self, request, field, rule):
		header ,is_new = models.HeaderData.objects.get_or_create(remote_adress= request.META["REMOTE_ADDR"],
																	http_encoding=request.META["HTTP_ACCEPT_ENCODING"],
																	http_language = request.META["HTTP_ACCEPT_LANGUAGE"],
																	request_method = request.META["REQUEST_METHOD"],
																	content_length = request.META["CONTENT_LENGTH"])
    
		logging.warn("%s contains %s " % (field[0],rule.description ))
		record = models.IdsRecord()
		record.description = rule.description
		record.user = request.user
		record.requested_path = request.path
		record.impact = rule.impact
		record.affected_field = field[0]
		record.payload = field[1]
		record.header_data = header
		record.save()
    	
		for tag in rule.tags:
			logging.debug(tag)
			persistentTag, is_new = models.AttackTag.objects.get_or_create(label = tag)
			record.tags.add(persistentTag)
		record.save()

	def applyRules(self, field, request):
		for rule in self.rules:
			try:
				p = re.compile(rule.rule)
				result = p.search(field[1])
				#logging.debug(result != None)
				if result :
					self.doCounterStrike(request, field, rule)
			except Exception, e:
                                print("error in urle" + rule.id)
				logging.error(e) #death trap due lookbehind
				
			
				
		
