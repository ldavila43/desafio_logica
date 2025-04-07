def escadaPalavras(data):
    inicio = data[0]
    fim = data[1]
    palavras = data[2][:]
    if fim not in palavras:
        return 0

    fila = [[inicio, 1]]
    while fila:
        palavra_atual, length = fila.pop(0)
        if palavra_atual == fim:
            return length
        for i in range(len(palavra_atual)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                proxima_palavra = palavra_atual[:i] + c + palavra_atual[i+1:]
                if proxima_palavra in palavras:
                    fila.append((proxima_palavra, length + 1))
                    palavras.remove(proxima_palavra)
    return 0


print(escadaPalavras(["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]]))
print(escadaPalavras(["hit", "cog", ["hot", "dot", "dog", "lot", "log"]]))

palavras = input("Digite as palavras: ")
while palavras != "":
    print(escadaPalavras(palavras))
    palavras = input("Digite as palavras: ")

