# 1 - crie um variável mensagem e exiba uma mensagem na tela
# 2 - crie uma variável número e exiba esse número na tela
# 3 - crie duas variáveis numéricas e faça as 4 operações matemáticas com esses números. Faça também a exponenciação e o resto da divisão
# 4 - crie duas variáveis d texto e faç a onatenação dessas mensagens
# 5 - faça um programa que receba um texto e faça-o repetir 5 vezes
# 6 - crie uma variável de teto em minúsculo deixe-o com todasas letras maiúsculas
# 7 - crie um programa que recebe um texto do usuário e exiba na tela
# 8 - crie um programa que receba do úsuario nome, idade, altura, cidade e estado e exiba a seguinte frase na tela: "Olá, meu nome é ______, tenho _____ anos de idade. Moro na cidade de __________/____".  use printf
# 9 - crie um programa om uma variável númro qualquer. Depois, crie uma variávl chute pedindo para o usúario digitar um número. Na sequência, crie uma condição para saber se o hute é igual a variável. caso seja igual exiba uma mensagem "Você acertou", se for diferente exiba a mensagem "Você errou".
mensagem = ' meu nome é Maria'
print(mensagem)

numero = 7
print(numero)

numero2 = 2
soma = numero + numero2
print(soma)

numero3 = 10
numero4 = 20
soma = numero3 + numero4
div = numero3 / numero4
sub = numero3 - numero4
multi = numero3 * numero4
print(soma)
print(div)
print(sub)
print(multi)

expo = numero3 ** numero4
Resto_dive = numero4 % numero3
Divi_Inteira = numero // numero2
print(expo)
print(Resto_dive)
print(Divi_Inteira)

texto1 = "batata"
texto2 = "banana"
c = texto1 + " " + texto2
print(c)

text = "aula"
repeticao = text * 5
print (repeticao)

text2 = 'bom dia'
#text2.upper()
print(text2.upper())

texto = input("Coloque sua mensagem")
print(texto)

nome2 = input (" digite seu nome") 
idade = int (input("digite sua idade"))
altura = float (input("digite sua altura"))
cidade = input(" digite sua cidade")
estado = input ("digite seu estado")

print (f'meu nome é {nome2}, tenho {idade} anos de idade. Moro na cidade de {cidade} do estado de {estado}. minha altura é {altura}') 