def recurcao(numero):
    if(numero <= 0):
        return
    print(numero)
    recurcao(numero-1) # 5, 4, 3, 2, 1, 0(return)

recurcao(5)