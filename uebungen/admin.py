from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.forms import SelectMultiple
from models import *

from django.forms import ModelForm

# Register your models here.



    
class AbgabeAdmin(admin.ModelAdmin):
    list_display = ('serie', 'student_A', 'student_B', 'points',)
    
class KolloquiumAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'points')

class KolloquiumInline(admin.TabularInline):
    model = Kolloquium
    extra = 1

class ExtrapunkteInline(admin.TabularInline):
    model = Extrapunkte
    extra = 1
    
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'matrikel', "stu_mail", 'points', 'abgaben_points', 'kolloquien_points', 'extra_points', )

    inlines = [
        ExtrapunkteInline,
        KolloquiumInline,
    ]
   
class StudentDetailAdmin(admin.ModelAdmin):
    # Mit dieser Funktion  umgeht man die beschraenkung dass django keine Parameter uebergibt
    # serie_num(1) gibt eine function, die die Punkte fuer Serie 1 liefert
    def serie_num(num):
        def fun(self):
            return self.abgabe_points(num)
        fun.short_description = u'Serie ' + unicode(num)
        return fun
    
    def kolloquium_num(num):
        def fun(self):
            return self.kolloquium_points(num)
        fun.short_description = u'Kolloquium ' + unicode(num+1)
        return fun
        
    #list_display = ('name', 'matrikel', "stu_mail", 'points', 'abgabe_points', 'kolloquium_points', 'extra_points', )
    list_display = ['matrikel', 'first_name', 'last_name', 'email', 'fehltermine',]
    for i in range(1,13):
        list_display.append(serie_num(i))
    list_display.extend([kolloquium_num(0), kolloquium_num(1), 'extra_points', 'klausur_points'])
    
    inlines = [
        ExtrapunkteInline,
        KolloquiumInline,
    ]

    
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

class AnwesenheitslisteAdmin(admin.ModelAdmin):
    def uebung_num(num):
        def fun(self):
            return self.kolloquium_points(num)
        fun.short_description = u'Kolloquium ' + unicode(num+1)
        return fun

"""
class NotizForm(ModelForm):
    class Meta:
        widgets = {
            'name': RedactorWidget(editor_options={'lang': 'de'})
        }

class NotizAdmin(admin.ModelAdmin):
    form = NotizForm
    fieldsets = [
      ('Text', {'classes': ('full-width',), 'fields': ('text',)})
    ]
"""
    
admin.site.register(Student, StudentAdmin)
admin.site.register(DetailStudent, StudentDetailAdmin)
admin.site.register(Abgabe, AbgabeAdmin)
admin.site.register(Kolloquium, KolloquiumAdmin)
admin.site.register(Uebung, UebungAdmin)
#admin.site.register(Notiz, NotizAdmin)
#admin.site.register(Anwesenheitsliste, AnwesenheitslisteAdmin)



