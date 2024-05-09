from exportHistoricStockPriceOperator import ExportHistoricStockPriceOperator

url = "https://financial-modeling-prep.p.rapidapi.com/v3/historical-price-full/{SYMBOL}"
csv_file_name = "{SYMBOL}_historical_prices.csv"

headers = {
    "X-RapidAPI-Key": "f0d77cd17bmshb342bb95b648db2p1e6864jsnbb923876c0c1",
    "X-RapidAPI-Host": "financial-modeling-prep.p.rapidapi.com"
}
csv_headers = ['symbol', 'name', 'date', 'open', 'high', 'low', 'close', 'change', 'changePercent', 'label']

executer = ExportHistoricStockPriceOperator(url,csv_file_name, headers, csv_headers)

executer.execute()