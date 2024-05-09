import csv
import requests
import logging
from configs.stock_price_config import stock_list

LOGGER = logging.getLogger()

# Make API call and get JSON response

class ExportHistoricStockPriceOperator:
	def __init__(self, url, csv_file_name, headers, csv_headers):
		

		self.url = url
		self.csv_file_name = csv_file_name
		self.headers = headers
		self.csv_headers = csv_headers
	
	def _make_api_call(self, updated_url):
		response = requests.get(updated_url, headers=self.headers)
		if response.status_code == 200:
			LOGGER.info("API Call Successfull")
			return response.json()
		else:
			LOGGER.error("API Call Failed with STATUS CODE: ", response.status_code)
			LOGGER.error("Error Message: ", response.text)
	
	def _generate_csv_file(self, data, csv_file_name, name):
		with open(csv_file_name, 'w', newline='') as csv_file:
			writer = csv.DictWriter(csv_file, fieldnames=self.csv_headers)
			writer.writeheader()
			for item in data['historical']:
				row = {
					'symbol': data['symbol'],
					'name': name,
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

	def execute(self):
		for stock in stock_list:
			symbol = stock[1]
			name = stock[0]
			updated_url = self.url.format(
				SYMBOL = symbol
			)

			updated_csv_file_name = self.csv_file_name.format(
				SYMBOL = symbol
			)

			data = self._make_api_call(updated_url)
			self._generate_csv_file(data, updated_csv_file_name, name)


		


