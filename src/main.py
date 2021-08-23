

print("""Bem vindo ao nosso chatbot! 
        Estamos aqui para ajudar você a encontrar um hotel.
        Para fazer isso iremos precisar coletar algumas informações suas!""")

while(True):
    min_price = float(input('Digite o preço minimo: '))
    while(not validate_field(min_price)):
        min_price = float(input('Digite o preço minimo: '))

    max_price = float(input('Digite o preço máximo: '))
    while(not validate_field(max_price)):
        max_price = float(input('Digite o preço máximo: '))

    number_bedrooms = float(input('Digite o número de quartos: '))
    while(not validate_field(number_bedrooms)):
        number_bedrooms = float(input('Digite o número de quartos: '))

    number_kids = float(input('Digite o número de quartos de crianças: '))
    while(not validate_field(number_kids)):
        number_kids = float(input('Digite o número de quartos de crianças: '))

    number_adult = float(input('Digite o número de quartos de adultos: '))
    while(not validate_field(number_adult)):
        number_adult = float(input('Digite o número de quartos de adultos: '))

    number_beds = float(input('Digite o número de camas: '))
    while(not validate_field(number_beds)):
        number_beds = float(input('Digite o número de camas: '))

    city = input('Digite a cidade: ')
    while(not validate_field(city, True)):
        city = input('Digite a cidade: ')

    