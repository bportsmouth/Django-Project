from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
	"january"   : "The first month of the year.",
	"february"  : "The second month of the year.",
	"march"     : "The third month of the year.",
	"april"     : "The fourth month of the year.",
	"may"       : "The fifth month of the year.",
	"june"      : "The sixth month of the year.",
	"july"      : "The seventh month of the year.",
	"august"    : "The eighth month of the year.",
	"september" : "The ninth month of the year.",
	"october"   : "The tenth month of the year.",
	"november"  : "The eleventh month of the year.",
	"december"  : "The twelfth month of the year."
}

# Create your views here.

def index(request):

	months = list(monthly_challenges.keys())

	list_items = "".join(
		
		f'<li><a href="{reverse("month-challenge", args=[month])}">{month.capitalize()}</a></li>'
		for month in months)

	response_data = f"<ul>{list_items}</ul>"

	return HttpResponse(response_data)




def monthly_challenge_by_number(request, month):

	redirect_month = None
	months = list(monthly_challenges.keys())

	try:
		redirect_month = months[month-1]

		redirect_path = reverse("month-challenge", args=[redirect_month])
		return HttpResponseRedirect(redirect_path)

	except:
		return HttpResponseNotFound(f"<h1> Month {month} doesn't exist!</h1>")



def monthly_challenge(request, month):


	challenge_text = monthly_challenges.get(month)

	if challenge_text:
		response_data = f"<h1>{challenge_text}</h1>"
		return HttpResponse(response_data)

	else:
		return HttpResponseNotFound("<h1>Month not supported</h1>")

	

	
