class HotelInformation(object):
# 	filterDict = {
#     'min_price': '350', 
#     'max_price': '400', 
#     'number_bedrooms': '1', 
#     'number_kids': '0', 
#     'number_adult': '1',
#     'number_beds': '1',
#     'city': 'Maceió'
# }
	def __init__(self):
		self.min_price = 0
		self.max_price = 0
		self.number_bedrooms = 0
		self.number_kids = 0
		self.number_adult = 0
		self.number_bed = 0
		self.city = ''

	def set_min_price(self, price_value):
		try:
			self.min_price = float(price_value)
			return True
		except ValueError:
			print('Você deve informar um valor númerico')
			return False
	
	def set_max_price(self, price_value):
		try: 
			self.max_price = float(price_value)
			return True
		except ValueError:
			print('Você deve informar um valor númerico')
			return False

	def set_number_bedrooms(self, number_bed):
		try:
			self.number_bed = int(number_bed)
			return True
		except ValueError:
			print('Você deve informar um valor númerico')
			return False

	def set_number_kids(self, number_kids):
		try:
			self.number_kids = int(number_kids)
			return True
		except ValueError:
			print('Você deve informar um valor númerico')
			return False

	def set_number_adult(self, number_adult):
		try:
			self.number_adult = int(number_adult)
			return True
		except ValueError:
			print('Você deve informar um valor númerico')
			return False

	def set_number_bed(self, number_bed):
		try:
			self.number_bed = int(number_bed)
			return True
		except ValueError:
			print('Você deve informar um valor númerico')
			return False

	def set_city(self, city, valid_cities):
		if(city in valid_cities):
			self.city = city
			return True
		else:
			print('Cidade não encontrada no nosso banco de dados')
			return False

	def to_dict(self):
		return  {
    		'min_price': self.min_price, 
    		'max_price': self.max_price, 
    		'number_bedrooms': self.number_bedrooms, 
    		'number_kids': self.number_kids, 
	    	'number_adult': self.number_adult,
	    	'number_beds': self.number_bed,
	    	'city': self.city
		}