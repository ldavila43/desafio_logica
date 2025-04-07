def primeiroNaoRepete(texto):
    contagem = {}
    tam = len(texto)
    if tam == 0:
        return "vazio"
    for caractere in texto:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1
    for i in range(tam):
        if contagem[texto[i]] == 1:
            return i
    return -1


# Testes
print(primeiroNaoRepete("abacabad"))
print(primeiroNaoRepete("aabbcc"))
print(primeiroNaoRepete(""))

texto = input("Digite um texto: ")
while texto != "":
    print(primeiroNaoRepete(texto))
    texto = input("Digite um texto: ")
