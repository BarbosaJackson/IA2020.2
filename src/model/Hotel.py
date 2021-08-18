class Hotel(object):
	def __init__(self, name, price, number_bedrooms, number_kids, number_adult, number_beds, city):
		self.name = name
		self.price = price
		self.number_bedrooms = number_bedrooms
		self.number_kids = number_kids
		self.number_adult = number_adult
		self.number_beds = number_beds
		self.city = city
	def __str__(self):
		return self.name + "\n" + self.price + "\n" + self.number_bedrooms + "\n" + self.number_kids + "\n" + self.number_adult + "\n" + self.number_beds + "\n" + self.city
	def to_json(self):
		return {
			'name': self.name,
			'price': self.price,
			'number_bedrooms': self.number_bedrooms,
			'number_kids': self.number_kids,
			'number_adult': self.number_adult,
			'number_beds': self.number_beds,
			'city': self.city
		}