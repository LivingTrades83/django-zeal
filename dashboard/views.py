from django.http import JsonResponse
from django.shortcuts import render
from random import randint

def dashboard(request):
	template = "dashboard.html"

	return render(request, template, {})

def get_data(request, *args, **kwargs):

	rand_1 = randint(0,10)
	rand_2 = randint(0,10)
	rand_3 = randint(0,10)
	rand_4 = randint(0,10)
	rand_5 = randint(0,10)
	rand_6 = randint(0,10)

	temp_1 = randint(0,10)
	temp_2 = randint(0,10)
	temp_3 = randint(0,10)
	temp_4 = randint(0,10)
	temp_5 = randint(0,10)
	temp_6 = randint(0,10)

	labels = ["Temperature", "Salinity", "Turbidity", "pH", "TDS", "ORP"]
	elementData = [rand_1, rand_2, rand_3, rand_4, rand_5, rand_6]
	phData = [temp_1, temp_2, temp_3, temp_4, temp_5, temp_6]
	days = ["Saturday","Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

	data = {
		"labels" : labels,
		"elementData" : elementData,
		"phData" : phData,
		"days" : days,
	}

	return JsonResponse(data)