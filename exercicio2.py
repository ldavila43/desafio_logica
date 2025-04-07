def primeiro_item(x):
    return x[0] # função para pegar o primeiro elemento do intervalo


def mesclaIntervalos(intervalos):
    intervalos.sort(key=primeiro_item) #utilizando o primeiro elemento do intervalo como key
    for i in range(len(intervalos) - 1):
        if intervalos[i][1] >= intervalos[i + 1][0]:
            intervalos[i] = (intervalos[i][0], max(intervalos[i][1], intervalos[i + 1][1]))
            del intervalos[i + 1]
            return mesclaIntervalos(intervalos)
    return intervalos


# Testes
print(mesclaIntervalos([(1, 3), (2, 6), (8, 10), (15, 18)]))
print(mesclaIntervalos([(1, 4), (4, 5)]))
print(mesclaIntervalos([(1, 4), (2, 3), (5, 7), (6, 8)]))

intervalos = input("Digite os intervalos: ")
while intervalos != "":
    print(mesclaIntervalos(intervalos))
    intervalos = input("Digite os intervalos: ")
