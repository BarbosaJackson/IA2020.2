import json

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

data = {'hotels': []}

def create_json_file(filename, new_hotel):
	filename = filename + '.json'
	global data
	data['hotels'].append(new_hotel.to_json())
	with open(filename, 'w') as outfile:
		json.dump(data, outfile)

def read(filename):
	filename = filename + '.json'
	global data
	try:
		with open(filename) as json_file:
			data = json.load(json_file)
	except FileNotFoundError:
		print('não abriu')

def main():
	can = True
	read('hotels')
	while(can) :
		print("============================")
		print("|  quantidade cadastrados  |")
		print("|         " + str(len(data['hotels'])) + "               |")
		print("============================")
		city = input("Onde?\n=> ")
		name = input("nome\n=> ")
		price = input("preço\n=> ")
		number_bedrooms = input("Quantos quartos?\n=> ")
		number_kids = input("Quantas crianças?\n=> ")
		number_adult = input("Quantos adultos?\n=> ")
		number_beds = input("Quantas camas?\n=> ")
		stop = int(input("0 - parar\n=> "))
		create_json_file('hotels', Hotel(name, price, number_bedrooms, number_kids, number_adult, number_beds, city))
		if(stop == 0):
			can = False

main()