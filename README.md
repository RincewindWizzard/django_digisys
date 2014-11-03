django_digisys
==============

Eine kleines Datenbanksystem zur Verwaltung meiner Übungsgruppe.

Mit django_digisys ist es möglich Studenten, Anwesenheitslisten, Übungen, Hausaufgaben und Extrapunkte zu verwalten.
Es bezieht sich auf die Vorlesung Digitale Systeme an der Uni Kiel.

Installation
============

django_digisys benötigt folgende Bibliotheken:

django (1.7), django-suit, unicodecsv

Wenn pip und python vorhanden sind, werden diese automatisch mit make installiert.


Folgende Befehle müssen im django_digisys/ Hauptordner ausgeführt werden:
Installation der Umgebung:
	
	make


Starten
=======
Es wird ein virtenv Ordner erstellt, in dem alle Bibliotheken installiert sind. Um ihn zu benutzen muss

	source virtenv/bin/activate

ausgeführt werden.

Danach kann man django_digisys im Developer-Modus starten:

	python manage.py runserver
