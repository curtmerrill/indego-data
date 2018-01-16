import json
from os import listdir
from os.path import isfile, join
from datetime import datetime

file_path = '/home/cmerrill/bike-kiosk/data'

files = [ f for f in listdir(file_path) if isfile(join(file_path,f)) ]

kiosk_data = []


for f in files:
	date = datetime.strptime(f, "%Y-%m-%d-%H-%M.json").isoformat()
	
	with open(join(file_path,f)) as file:
		try:
			data = json.load(file)

			for kiosk in data['features']:
				kiosk_data.append({
					"date": date,
					"name": kiosk['properties']['name'],
					"bikes": kiosk['properties']['bikesAvailable'],
					"docks": kiosk['properties']['docksAvailable'],
					"total_docks": kiosk['properties']['totalDocks'],
					"lat": kiosk['geometry']['coordinates'][1],
					"lon": kiosk['geometry']['coordinates'][0]
			})
		except ValueError:
			pass

with open('data.json','w') as output:
	output.write(json.dumps(kiosk_data))

