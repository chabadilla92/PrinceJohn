from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import finnhub

# Create your views here.
def index(request):

  # Get the ticker from request
  if "q" in request.GET.keys():
    ticker = request.GET["q"]
  else:
    ticker = "AAPL"

  ticker = ticker.upper()

  finnhub_client = finnhub.Client(settings.FINNHUB_API_KEY)
  response = finnhub_client.quote(ticker)
  response["ticker"] = ticker
  return render(request, 'quote.html', response)

