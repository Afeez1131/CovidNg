from django.core.management.base import BaseCommand

from bs4 import BeautifulSoup
import requests
import json


from total.models import Total, TotalDate

class Command(BaseCommand):
	help = 'Refresh Database item'

	def handle(self, *args, **options):
		url = requests.get('https://covid19.ncdc.gov.ng/')
		soup = BeautifulSoup(url.content, 'html.parser')
		#soup = BeautifulSoup(open(url), 'html.parser')
		custom1 = soup.find(class_ = 'text-right text-white')
		# tr = custom1.find_all('tr')
		# print(tr.text)

		#confirmed_cases = custom1.text
		active_cases = soup.find_all('h2')
		
		sample = active_cases[0].text[1:]
		confirmed = active_cases[1].text 
		active = active_cases[2].text
		discharged = active_cases[3].text
		death = active_cases[4].text 

		#deleting the data from the previous day
		Total.objects.all().delete()
		try:
			
			Total.objects.create(
			sample = sample,
			confirmed = confirmed,
			active = active,
			discharged = discharged,
			death = death)
			#saving the days data in a model
			
			TotalDate.objects.create(
				sample=sample,
				confirmed=confirmed,
				active=active,
				discharged=discharged,
				death=death)

		except Exception as e:
			print(e)
		print(Total.objects.all())
		print(TotalDate.objects.all())

		self.stdout.write('latest data fetched')