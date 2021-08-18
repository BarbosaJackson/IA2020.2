import json

class JSON(object):
	def __init__(self, filename):
		self.filename = filename
	
	def read(self):
		data = {}
		with open(self.filename) as json_file:
			data = json.load(json_file)
		return data

	def write_value(self, data, field, value):
		data[field].append(value)
		print(field, value, self.filename)
		with open(self.filename, 'w') as outfile:
			json.dump(data, outfile)

	def filter(self, filterDict):
		data = self.read()
		possible_hotels = []
		for hotel in data['hotels']:
			if(filterDict['min_price'] <= hotel['price'] and hotel['price'] <= filterDict['max_price']
				and hotel['number_bedrooms'] == filterDict['number_bedrooms'] and
				hotel['number_beds'] >= filterDict['number_beds'] and hotel['city'] == filterDict['city'] and
				hotel['number_kids'] >= filterDict['number_kids'] and 
				hotel['number_adult'] >= filterDict['number_adult']):
				possible_hotels.append(hotel)
		return possible_hotels

filterDict = {
	'min_price': '350', 
	'max_price': '400', 
	'number_bedrooms': '1', 
	'number_kids': '0', 
	'number_adult': '1',
	'number_beds': '1',
	'city': 'Maceió'
}

myjson = JSON('../hotels.json')
print(myjson.filter(filterDict))

