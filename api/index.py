import requests
from urllib import parse 
from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        query_params = dict(parse.urlencode(self.headers.get("query_params")))
        country = query_params.get("country")
        capital = query_params.get("capital")
        response_text = ""

        if country:
            url = f"https://restcountries.com/v2/name/{country}"
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200 and data:
                capital = data[0]["capital"]
                response_text = f"The capital of {country} is {capital}"
        
        if capital:
            url = f"https://restcountries.com/v2/capital/{capital}"
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200 and data:
                country = data[0]["name"]["common"]
                response_text = f"{capital} is the capital of {country}"
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response_text.encode('utf-8'))
        return