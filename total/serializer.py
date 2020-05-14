from rest_framework import serializers
from .models import Total


class TotalConfirmedSerializer(serializers.ModelSerializer):
	class Meta:
		model = Total
		fields = ('confirmed',)

class TotalActiveSerializer(serializers.ModelSerializer):
	class Meta:
		model = Total 
		fields = ('active',)

class TotalDischargedSerializer(serializers.ModelSerializer):
	class Meta:
		model = Total 
		fields = ('discharged',)

class TotalDeathSerializer(serializers.ModelSerializer):
	class Meta:
		model = Total 
		fields = ('death',)


class TotalSampleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Total 
		fields = ('sample',)

class TotalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Total 
		fields = ('sample', 'confirmed', 'active', 'discharged', 'death')

# class TotalDateSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = TotalDate
# 		fields = ('sample', 'confirmed', 'active', 'discharged', 'death',)
# 		extra_kwargs = {'url': {'lookup_field': 'date'}}