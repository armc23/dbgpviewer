from django.contrib import admin
from .models import Record,Prefix,Site,Relist

admin.site.register(Record)
admin.site.register(Prefix)
admin.site.register(Site)
admin.site.register(Relist)