django_digisys
==============

Eine kleines Datenbanksystem zur Verwaltung meiner Übungsgruppe.

Mit django_digisys ist es möglich Studenten, Anwesenheitslisten, Übungen, Hausaufgaben und Extrapunkte zu verwalten.
Es bezieht sich auf die Vorlesung Digitale Systeme an der Uni Kiel.

Installation
============

django_digisys benötigt folgende Bibliotheken:

django (1.7), django-suit, unicodecsv

Am einfachsten installiert man alles über pip:

	pip install Django django-suit unicodecsv


Starten
=======

Um django_digisys im Developer-Modus zu starten führt man folgenden Befehl im django_digisys/ Orderner aus:

	python manage.py runserver
