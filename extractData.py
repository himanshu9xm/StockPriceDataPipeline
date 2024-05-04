import csv
import requests

# Make API call and get JSON response
url = "https://financial-modeling-prep.p.rapidapi.com/v3/historical-price-full/MSFT"

headers = {
	"X-RapidAPI-Key": "f0d77cd17bmshb342bb95b648db2p1e6864jsnbb923876c0c1",
	"X-RapidAPI-Host": "financial-modeling-prep.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
	print("API Call Successfull")
	data = response.json()
	# Define CSV file path and headers
	csv_file_name = "historical_prices.csv"
	csv_headers = ['symbol', 'date', 'open', 'high', 'low', 'close', 'change', 'changePercent', 'label']

	# Extract required data and write to CSV
	with open(csv_file_name, 'w', newline='') as csv_file:
		writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
		writer.writeheader()
		for item in data['historical']:
			row = {
				'symbol': data['symbol'],
				'date': item['date'],
				'open': item['open'],
				'high': item['high'],
				'low': item['low'],
				'close': item['close'],
				'change': item['change'],
				'changePercent': item['changePercent'],
				'label': item['label']
			}
			writer.writerow(row)

else:
	print("API Call Failed: ", response.status_code)
	print("Error Message: ", response.text)
