import tkinter as tk
import nltk
from nltk.chat.util import Chat, reflections
from tkinter import *

pairs = [
    [
        r"meu nome é (.*)",
        ["Oi %1, Como você está hoje ?",]
    ],
    [
        r"oi|ola|olá",
        ["Olá", "Oiii",]
    ], 
    [
        r"Qual é seu nome ?",
        ["Eu sou um bot criado por Kelly Silva e Jackson, para ajudar você a encontrar um hotel!",]
    ],
    [
        r"como você está ?|Como você esta ?|como vc está ?|como você esta ?|tudo bem ?",
        ["Eu estou bem e como você está ?",]
    ],
    [
        r"desculpe (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"Estou bem|Bem|indo|tranquilo",
        ["Que bom ouvir isso, como posso ajudar você?",]
    ],
    [
        r"Triste",
        ["Como eu posso ajudar você?",]
    ],
    [
        r"O que (.*) quer ?",
        ["Faça-me uma oferta que não posso recusar",]
    ],
    [
        r"(.*) criado ?|(.*) criou",
        ["Kelly e Jackson me criaram usando Python NLTK library ","É segredo ;)",]
    ],
    [
        r"(.*) (localização|cidade) ?",
        ['Maceió, Alagoas - Brasil',]
    ],
    [
        r"(.*) viajar",
        ['No momento só temos viagens para Maceió']
    ],
    
    [
        r"sair",
        ["Até mais ! ","Foi muito bom conversar com vocês, até mais :)"]

    ],
]

def chat():
    print("Oi! Eu sou um chatbot creado por Kelly e Jackson para ajudar você !")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chat()