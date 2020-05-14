from django.core.management.base import BaseCommand

from bs4 import BeautifulSoup
import requests
import json


from state.models import Covid

class Command(BaseCommand):
	help = 'Refresh Database item'

	def handle(self, *args, **options):
		tab = []
		Covid.objects.all().delete()
		#url = 'covid2.html'
		url = requests.get('https://covid19.ncdc.gov.ng/')
		soup = BeautifulSoup(url.content, 'html.parser')
		custom1 = soup.find(class_ = "table-responsive")
		data = custom1.find('tbody')
		d2 = data.find_all('td')
		count = 0

		Covid.objects.all().delete()
		for item in d2:
			tab.append(item.text.strip('\n').strip(' '))
		while count != len(tab):
			# try:
			states_affected = tab[count ]
			lab_confirmed = tab[count + 1]
			admitted = tab[count + 2]
			discharged = tab[count + 3]
			death = tab[count + 4]


			Covid.objects.create(
			states_affected = states_affected,
			lab_confirmed = lab_confirmed,
			admitted = admitted,
			discharged = discharged,
			death = death)

			count += 5

		self.stdout.write('Latest Data Fetched')

		