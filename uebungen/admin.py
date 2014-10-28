from django.contrib import admin
from django.forms import SelectMultiple
from models import *
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'matrikel', "stu_mail", 'points', 'abgabe_points', 'kolloquium_points', 'extra_points', )
    
class AbgabeAdmin(admin.ModelAdmin):
    list_display = ('serie', 'student_A', 'student_B', 'points',)
    
class KolloquiumAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'points')

class ExtrapunkteInline(admin.TabularInline):
    model = Extrapunkte
    
class UebungAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("uebungen/css/admin_custom.css",)
        }
    list_display = ('date', )
    fields = ('date', 'anwesenheit')
    filter_horizontal = ('anwesenheit',)
    inlines = [
        ExtrapunkteInline,
    ]
    

    
admin.site.register(Student, StudentAdmin)
admin.site.register(Abgabe, AbgabeAdmin)
admin.site.register(Kolloquium, KolloquiumAdmin)
admin.site.register(Uebung, UebungAdmin)

