from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
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
	"december"  : None
}

# Create your views here.

def index(request):

	months = list(monthly_challenges.keys())

	return render(request, "challenges/index.html", {
		"months": months

		})


def monthly_challenge_by_number(request, month):

	redirect_month = None
	months = list(monthly_challenges.keys())

	try:
		redirect_month = months[month-1]

		redirect_path = reverse("month-challenge", args=[redirect_month])
		return HttpResponseRedirect(redirect_path)

	except:
		raise Http404()




def monthly_challenge(request, month):

	try:
		challenge_text = monthly_challenges[month]
		return render(request, "challenges/challenge.html", {
			"month": month,
			"display_text": challenge_text

			})

	except:
		raise Http404()

	

	
