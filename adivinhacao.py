print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 42

# input sempre devolve str / a função int() converte
chute = int(input("Digite o seu número: "))

print("Você digitou", chute)

# não usa {} e sim :, precisa estar indentado pra identificar como parte do bloco
if(numero_secreto == chute):
    print("Você acertou")
else:
    print("Você errou")

print("Fim do jogo")