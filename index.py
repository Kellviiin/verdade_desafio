import secrets

participantes =[]

print("BEM VINDOS AO JOGO VERDADE E DESAFIO!!!")
print("Para começar aperte: S")
print("Para sair aperte: E")
menu = input().lower()

num_participantes = int(input("N° Participantes: "))
for i in range(1, num_participantes + 1 ):
        nome_participantes = input(f'Jogador N° {i}: ')
        participantes.append(nome_participantes) #Cola o nome dos participantes dentro do array



while menu == "s":
    pergunta = secrets.choice(participantes)
    responde = secrets.choice(participantes)

    while pergunta == responde:
        pergunta = secrets.choice(participantes)
        responde = secrets.choice(participantes)

    print(f"Pergunta: {pergunta}")
    print(f"Responde: {responde}")
    menu = input("Se quiser jogar de novo aperte S | Se não aperte E: ").lower()

    
