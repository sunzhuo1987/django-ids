from django.contrib import admin
from core import models

class IdsRecordAdmin(admin.ModelAdmin):
        list_display = ('eventTimestamp','description','impact','tag_list','header_data')
	search_fields = ('description','header_data__remote_adress')
	list_filter = ['eventTimestamp','description','tags','impact']


admin.site.register(models.IdsRecord, IdsRecordAdmin)
admin.site.register(models.HeaderData, admin.ModelAdmin)
