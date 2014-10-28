# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.



class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    matrikel = models.IntegerField()
    stu_mail = models.EmailField()
    mail = models.EmailField(null=True)
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Studenten"
    
    def name(self):
        return unicode(self.first_name + " " + self.last_name)
    
    """ Gibt die Punkte zurueck, die dieser Student erreicht hat """
    def points(self):
        return 0
        
    def __unicode__(self):
        return self.name()
       
class Abgabe(models.Model):
    student_A = models.ForeignKey('Student', related_name='abgabe_a')
    student_B = models.ForeignKey('Student', related_name='abgabe_b')
    SERIEN = tuple(map(lambda x: (x, "Serie " + str(x)), range(1,13)))
    serie = models.IntegerField(choices=SERIEN)
    points = models.IntegerField()
    
    def gruppe(self):
        return unicode(self.student_A) + " & " + unicode(self.student_B)
        
    class Meta:
        verbose_name = "Abgabe"
        verbose_name_plural = "Abgaben"
    
class Kolloquium(models.Model):
    student = models.ForeignKey('Student')
    date = models.DateField(auto_now=True)
    points = models.IntegerField()
    
    class Meta:
        verbose_name = "Kolloquium"
        verbose_name_plural = "Kolloquien"
    
class Uebung(models.Model):
    date = models.DateField()
    anwesenheit = models.ManyToManyField("Student", verbose_name = u'Anwesenheit')
    
    class Meta:
        verbose_name = u'Übung'
        verbose_name_plural = u'Übungen'
        
    def __unicode__(self):
        return unicode(self.date.strftime("%d. %B %Y"))        
    
class Extrapunkte(models.Model):
    student = models.ForeignKey('Student')
    uebung = models.ForeignKey('Uebung')
    points = models.IntegerField()
    
    class Meta:
        verbose_name = "Extrapunkte"
        verbose_name_plural = "Extrapunkte"

