from django.contrib import admin
from models import *
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'matrikel', "stu_mail", 'points')
    
class AbgabeAdmin(admin.ModelAdmin):
    list_display = ('gruppe',)

class ExtrapunkteInline(admin.TabularInline):
    model = Extrapunkte
    
class UebungAdmin(admin.ModelAdmin):
    fields = ('date', 'anwesenheit')
    filter_horizontal = ('anwesenheit',)
    inlines = [
        ExtrapunkteInline,
    ]
    

    
admin.site.register(Student, StudentAdmin)
admin.site.register(Abgabe, AbgabeAdmin)
admin.site.register(Kolloquium)
admin.site.register(Uebung, UebungAdmin)
admin.site.register(Extrapunkte)
