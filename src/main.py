from model.HotelInformation import HotelInformation
from model.JSON import JSON

print("""Bem vindo ao nosso chatbot! 
        Estamos aqui para ajudar você a encontrar um hotel.
        Para fazer isso iremos precisar coletar algumas informações suas!""")

flag = True
hotelInformation = HotelInformation()
myjson = JSON('hotels.json')
valid_cities = myjson.getCities()
while(flag):
    min_price = input('Digite o preço minimo: ')
    while(not hotelInformation.set_min_price(min_price)):
        min_price = input('Digite o preço minimo: ')

    max_price = input('Digite o preço máximo: ')
    while(not hotelInformation.set_max_price(max_price)):
        max_price = input('Digite o preço máximo: ')

    number_bedrooms = input('Digite o número de quartos: ')
    while(not hotelInformation.set_number_bedrooms(number_bedrooms)):
        number_bedrooms = input('Digite o número de quartos: ')

    number_kids = input('Digite o número de quartos de crianças: ')
    while(not hotelInformation.set_number_kids(number_kids)):
        number_kids = input('Digite o número de quartos de crianças: ')

    number_adult = input('Digite o número de quartos de adultos: ')
    while(not hotelInformation.set_number_adult(number_adult)):
        number_adult = input('Digite o número de quartos de adultos: ')

    number_beds = input('Digite o número de camas: ')
    while(not hotelInformation.set_number_bed(number_beds)):
        number_beds = input('Digite o número de camas: ')

    city = input('Digite a cidade: ')
    while(not hotelInformation.set_city(city, valid_cities)):
        city = input('Digite a cidade: ')

    valid_hotels = myjson.filter(hotelInformation.to_dict())

    print('\n===============================\n')
    for i in valid_hotels:
        print(i)
    print('\n===============================\n')
    option = int(input("Deseja continuar? 1 - sim, 2 - não\n"))
    
    if option == 1:
        flag = True
    else:
        flag = False