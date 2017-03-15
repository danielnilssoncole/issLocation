import requests
import json
import datetime

response_now = requests.get('http://api.open-notify.org/iss-now.json')

parameters = {'lat': 27.9506, 'lon': -82.4572} #tampa
response_pass = requests.get('http://api.open-notify.org/iss-pass.json', params=parameters)

# print(response_pass.content)

datanow = response_now.json()
lat = datanow['iss_position']['latitude']
lon = datanow['iss_position']['longitude']
print('\nThe current location of the ISS is: {}, {}\n'.format(lat, lon))
print('It will pass {}, {} at the following times:\n'.format(parameters['lat'], parameters['lon']))

data = response_pass.json()
for response in data['response']:
    duration = response['duration']/60.0
    risetime = response['risetime']
    risetimeval = datetime.datetime.fromtimestamp(risetime)
    risetimeread = risetimeval.strftime('%H:%M:%S %m-%d-%Y')
    print('{} for {:.2f} seconds'.format(risetimeread, duration))

print('\n')
