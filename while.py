# imprimir um numero para cada andar de um hotel de 20 andares 

def imprimir_hotel ():
    andar_hotel = 1 

    while andar_hotel <= 20 :
        print (f"Andar {andar_hotel}")
        andar_hotel += 1

imprimir_hotel()


# imprimir um numero para cada andar de um hotel de 20 andares pulando o numero 13 

def imprimir_hotel_pulandon():
    andar_hotel = 1 

    while andar_hotel <= 20 :
        if (andar_hotel == 13):
            andar_hotel  += 1
            continue
        print (f"Andar {andar_hotel}")
        andar_hotel  += 1

imprimir_hotel_pulandon()


# imprimir um numero para cada andar de um hotel de 20 andares pulando o numero 13 e ordem decrescente 

def imprimir_hotel_decrecente ():
    andar_hotel = 20

    while andar_hotel >= 1 :
        if (andar_hotel == 13):
            andar_hotel  -= 1
            continue
        print (f"Andar {andar_hotel}")
        andar_hotel  -= 1

imprimir_hotel_decrecente()
    