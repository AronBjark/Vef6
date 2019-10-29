from flask import Flask, render_template, session
from requests import get
app = Flask(__name__)
app.config['SECRET_KEY'] = 'danni'

with get('https://apis.is/petrol') as response:
    if response:
        print(' * API Succesfully loaded', response)
        data = response.json()['results']
        timestamp = response.json()['timestampPriceChanges']
    else:
        print(' * API error', response)
        exit()

stations = []
for station in data:
    if station['company'] not in stations:
        stations.append(station['company'])

@app.route('/')
def index():
	return render_template("index.tpl",stations = stations) 

@app.route('/company/<name>')
def company(name):
	return render_template("company.html", x = name, data = data)

@app.route('/station/<key>')
def station(key):
	for x in data:
		if x['key'] == key:
			station = x
			break
	return render_template("station.html", key = key, data = data, station = station)

if __name__ == "__main__":
	app.run(debug=True)
