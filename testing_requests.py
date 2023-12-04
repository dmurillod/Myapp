import requests 

api_url = 'https://api.kanye.rest/'

response = requests.get(api_url)
result = response.json()['quote']
print(f'The quote is: {result}')