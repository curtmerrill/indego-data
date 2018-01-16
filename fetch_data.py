from datetime import datetime
import requests

now = datetime.now()

filename = datetime.strftime(now, "%Y-%m-%d-%H-%M.json")
filepath = '/home/cmerrill/bike-kiosk/data/'
headers = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17',
}

r = requests.get('http://api.phila.gov/bike-share-stations/v1', headers=headers)

with open(filepath+filename, 'w') as file:
    file.write(r.text)
