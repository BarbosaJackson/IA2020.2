from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('TravelBot')
conversa = ChatterBotCorpusTrainer(bot)
conversa.train('chatterbot.corpus.portuguese')

conversa = ListTrainer(bot)
conversa.train([
    'Oi?', 
    'Eae, tudo certo?',
    'Qual o seu nome?', 
    'Travelbot, seu amigo bot',
    ])

conversa.train(['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 
			'Você gosta de programar?', 'Sim, eu programo em Python'])

while True:
    try:
        resposta = bot.get_response(input("Usuário: "))
        if float(resposta.confidence) > 0.2:
            print("TravelBot: ", resposta)
        else:
            print("Ainda não sei como te ajudar :/")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break