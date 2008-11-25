from django.db import models ,connection
from django.contrib.auth.models import User

class HeaderData(models.Model):
	"""HTTP header metadata"""

	http_encoding = models.CharField(blank=False, max_length=100)
	http_language = models.CharField(blank=False, max_length=100)
	request_method = models.CharField(blank=False, max_length=100)
	remote_adress = models.IPAddressField(blank=True)
	content_length = models.IntegerField(blank=True, null=True)
	request_encoding = models.CharField(blank=False, max_length=100)
	content_type =  models.CharField(blank=False, max_length=250)

	def __str__(self):
		return self.remote_adress

class AttackTag(models.Model):
	"""Model for tag to be applied to an attack"""
	
	label = models.CharField(blank=False, max_length=100)

	def __str__(self):
		return self.label

class ReportRow(object):
	"""docstring for ReportRow"""
	def __init__(self, value, label):
		super(ReportRow, self).__init__()
		self.value = value
		self.label = label
		print(self.label)
			
	

		
class IdsRecordManager(models.Manager):
	
	def top_attacks(self):
		query = """SELECT count(*) AS num_attacks, core_idsrecord.description AS description 
						FROM core_idsrecord 
						GROUP BY core_idsrecord.description order by num_attacks"""
		cursor = connection.cursor()
		cursor.execute(query,)
		return [ReportRow(item[0],item[1]) for item in cursor.fetchall()]
	
	def top_attacks_tag(self):
		query = """SELECT count(*) AS num_attacks, core_idsrecord.description AS description 
						FROM core_idsrecord 
						GROUP BY core_idsrecord.description order by num_attacks"""
		cursor = connection.cursor()
		cursor.execute(query,)
		return [ReportRow(item[0],item[1]) for item in cursor.fetchall()]
		
	def top_attacks_paths(self):
		query = """SELECT count(*) AS num_attacks, core_idsrecord.requested_path AS requested_path 
						FROM core_idsrecord 
						GROUP BY core_idsrecord.requested_path order by num_attacks"""
		cursor = connection.cursor()
		cursor.execute(query,)
		return [ReportRow(item[0],item[1]) for item in cursor.fetchall()]
	
	def attacks_trends(self):
		query = """SELECT count(*) AS num_attacks, core_idsrecord.eventTimestamp AS report_date 
						FROM core_idsrecord 
						GROUP BY report_date order by report_date"""
		cursor = connection.cursor()
		cursor.execute(query,)
		return [ReportRow(item[0],item[1]) for item in cursor.fetchall()]

	

class IdsRecord(models.Model):
	"""Basic record model for ids catchups"""
	eventTimestamp = models.DateTimeField(auto_now_add=True)
	description = models.CharField(blank=False, max_length=250)
	user = models.ForeignKey(User,null=True)
	requested_path = models.CharField(blank=False, max_length=250)
	affected_field = models.CharField(blank=False, max_length=100)
	payload = models.CharField(blank=False, max_length=100)
	impact = models.SmallIntegerField(blank=True, null=True)
	header_data = models.ForeignKey(HeaderData)
	tags = models.ManyToManyField(AttackTag)
	objects = IdsRecordManager()
	@property
	def tag_list(self):
		taglist = " "
		for tag in self.tags.all():
			print(tag.label)
			print(taglist)
			taglist = taglist + tag.label
			taglist = taglist + " "
		return taglist

	def __str__(self):
		return "IdsRecord"#" %s : %s" % [self.eventTimestamp,self.description]


	

	

