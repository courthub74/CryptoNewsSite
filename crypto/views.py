from django.shortcuts import render

# Create your views here.

#HOME
def home(request):
	import requests
	import json

	#Grab Crypto Price Data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,LTC,XLM,ADA,VET&tsyms=USD")
	price = json.loads(price_request.content)
	

	#Grab Crypto News
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request, 'home.html', {'api': api, 'price': price})


#PRICES
def prices(request):
	if request.method == 'POST':
		import requests
		import json
		quote = request.POST['quote'] #'quote' From the 'name' from the input of the search form on the base page
		quote = quote.upper()
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")#Here its getting every single crypto
		crypto = json.loads(crypto_request.content)

		
		return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})

	else:
		notfound = "Enter a Crypto in our trusty search engine"
		return render(request, 'prices.html', {'notfound': notfound})
	


