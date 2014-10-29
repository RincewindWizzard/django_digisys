# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Sum, Q
# Create your models here.



class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    matrikel = models.IntegerField()
    stu_mail = models.EmailField()
    mail = models.EmailField(null=True, blank=True)
    klausur_points = models.IntegerField(default=None, null=True, blank=True, verbose_name = u'Klausurpunkte')
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Studenten"
        ordering = ['first_name', 'last_name']
    
    def name(self):
        return unicode(self.first_name + " " + self.last_name)
    
    def extra_points(self):
        extra_points = Extrapunkte.objects.filter(student=self).all().aggregate(Sum('points'))['points__sum']
        return extra_points if extra_points else 0
    extra_points.short_description = "Mitarbeit"
    
    def kolloquium_points(self):
        kolloquium_points = Kolloquium.objects.filter(student=self).all().aggregate(Sum('points'))['points__sum']
        return kolloquium_points if kolloquium_points else 0
    kolloquium_points.short_description = "Kolloquien"
        
    def abgabe_points(self):
        abgabe_points = Abgabe.objects.filter(Q(student_A=self) | Q(student_B=self)).all().aggregate(Sum('points'))['points__sum']
        return abgabe_points if abgabe_points else 0
    abgabe_points.short_description = "Serien"    
        
    """ Gibt die Punkte zurueck, die dieser Student erreicht hat """
    def points(self):
        return self.extra_points() + self.kolloquium_points() + self.abgabe_points()
    points.short_description = "Punkte"   
      
    def email(self):
        return self.mail if self.mail else self.stu_mail
        
    def fehltermine(self):
        return Uebung.objects.count() - Uebung.objects.filter(anwesenheit__in=[self]).count()
    
    def __unicode__(self):
        return self.name()
       
class Abgabe(models.Model):
    student_A = models.ForeignKey('Student', related_name='abgabe_a')
    student_B = models.ForeignKey('Student', related_name='abgabe_b')
    SERIEN = tuple(map(lambda x: (x, "Serie " + str(x)), range(1,13)))
    serie = models.IntegerField(choices=SERIEN)
    points = models.IntegerField(verbose_name = u'Punkte')
    
    def gruppe(self):
        return unicode(self.student_A) + " & " + unicode(self.student_B)
        
    class Meta:
        verbose_name = "Abgabe"
        verbose_name_plural = "Abgaben"

    def __unicode__(self):
        return "Serie " + unicode(self.serie) + ": " + self.gruppe()
    
class Kolloquium(models.Model):
    student = models.ForeignKey('Student')
    date = models.DateField()
    points = models.IntegerField()
    
    class Meta:
        verbose_name = "Kolloquium"
        verbose_name_plural = "Kolloquien"
    
    def __unicode__(self):
        return "Kolloquium: " + unicode(self.student) + " (" + unicode(self.points) + " LP)"
    
class Uebung(models.Model):
    date = models.DateField()
    anwesenheit = models.ManyToManyField("Student", verbose_name = u'Anwesenheit')
    
    class Meta:
        verbose_name = u'Übung'
        verbose_name_plural = u'Übungen'
        
    def __unicode__(self):
        return unicode(self.date)        
    
class Extrapunkte(models.Model):
    student = models.ForeignKey('Student')
    uebung = models.ForeignKey('Uebung')
    points = models.IntegerField(verbose_name = u'Punkte')
    
    class Meta:
        verbose_name = "Extrapunkte"
        verbose_name_plural = "Extrapunkte"

