from django.contrib import admin

# Register your models here.
from testapp.models  import Report,Alpha



class ReportAdmin(admin.ModelAdmin):
    list_display = ['sheet_name','column','file']


class AlphAdmin(admin.ModelAdmin):
    list_display = ['letter','number']


admin.site.register(Report,ReportAdmin)
admin.site.register(Alpha,AlphAdmin)