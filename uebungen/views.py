from django.shortcuts import render
import unicodecsv
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q

from models import *

#@login_required

def export():
    table = []
    for student in Student.objects.all():
        row = [
            student.matrikel, 
            student.first_name, 
            student.last_name,
            student.email(), 
            student.fehltermine(),
        ]
        for serie in range(1,13):
            abgabe = Abgabe.objects.filter(Q(serie=serie) & (Q(student_A=student) | Q(student_B=student))).first()
            row.append(abgabe.points if abgabe else "")

        kolloquien = Kolloquium.objects.filter(student=student)
        for kolloquium in kolloquien:
            row.append(kolloquium.points)
        
        for i in range(2-len(kolloquien)):
            row.append("")
            
        row.append(student.extra_points())         
        row.append(student.klausur_points)
        table.append(row)
    return table

def export_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="studenten.csv"'


    writer = unicodecsv.writer(response)
    writer.writerow(['Matrikelnr', 'Vorname', 'Name', 'Email', 'Abwesend', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'Kolloq1', 'Kolloq2', 'Extrapunkte', 'Klausurpunkte'])

    for row in export():
        writer.writerow(row)
    

    return response


