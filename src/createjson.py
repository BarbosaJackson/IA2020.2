from model.Hotel import Hotel
from model.JSON import JSON

def main():
	data = {'hotels': []}
	can = True
	myjson = JSON('hotels.json')
	data = myjson.read()
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
		cur_hotel = Hotel(name, price, number_bedrooms, number_kids, number_adult, number_beds, city)
		myjson.write_value(data, 'hotels', cur_hotel.to_json())
		if(stop == 0):
			can = False

main()