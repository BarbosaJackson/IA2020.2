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
		counter = 0
		for hotel in data['hotels']:
			if(filterDict['min_price'] <= hotel['price'] and hotel['price'] <= filterDict['max_price']
				and hotel['number_bedrooms'] >= filterDict['number_bedrooms'] and
				hotel['number_beds'] >= filterDict['number_beds'] and hotel['city'] == filterDict['city'] and
				hotel['number_kids'] >= filterDict['number_kids'] and 
				hotel['number_adult'] >= filterDict['number_adult']):
				possible_hotels.append(hotel)
			counter += 1
			if(counter == 5):
				break
		return possible_hotels

	def update(self):
		data = self.read()
		for hotel in data['hotels']:
			print(hotel)
			# hotel['min_price'] = float(hotel['min_price'])
			hotel['price'] = float(hotel['price'])
			hotel['number_kids'] = int(hotel['number_kids'])
			hotel['number_adult'] = int(hotel['number_adult'])
			hotel['number_bedrooms'] = int(hotel['number_beds'])
			hotel['number_beds'] = int(hotel['number_beds'])
		with open(self.filename, 'w') as outfile:
			json.dump(data, outfile)
	def getCities(self):
		data = self.read()
		cities = []
		for hotel in data['hotels']:
			if(not (hotel['city'] in cities)):
				cities.append(hotel['city'])
		return cities

# filterDict = {
# 	'min_price': '350', 
# 	'max_price': '400', 
# 	'number_bedrooms': '1', 
# 	'number_kids': '0', 
# 	'number_adult': '1',
# 	'number_beds': '1',
# 	'city': 'Maceió'
# }

# myjson = JSON('../hotels2.json')
# myjson.update()
# print(myjson.getCities())

