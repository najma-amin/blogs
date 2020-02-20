from .models import Quote
import urllib.request, json

def get_quote():
    """
    Function to consume http request and return a Quote class instance
    """
    url = "http://quotes.stormconsultancy.co.uk/random.json"
    
    with urllib.request.urlopen(url) as url:
        response = url.read()
        random_quote=json.loads(response)
    
    return random_quote
