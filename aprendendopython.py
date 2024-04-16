#Função Print
print("Hello World!")

#Variaveis

olamundo = "Hello World"
print(olamundo)

#Funções Strings
print(olamundo.upper()) # Deixa tudo Maiusculo.
print(olamundo.lower()) # Deixa tudo Minusculo.
print(olamundo.title()) # Deixa a Primeira Letra da Palavra Maiusculo.

#Teste Falso na String - is + função
print(olamundo.upper().isupper()) # Testa Verdadeiro de Maiusculo
print(olamundo.lower().islower()) # Testa Verdadeiro de Minusculo
print(olamundo.title().istitle()) # Testa Verdadeiro de Titulo
print(olamundo.isupper())

# Selecionar Listas/Letras - Variavel + [0]

print(olamundo[1])
print(olamundo[1: ])

# Medir o tamanho Comando : len
print(len(olamundo))

# Substituir Palavra Função replace
olamundobr = olamundo.replace("Hello World", "Olá Mundo")
print("Agora Mudou para " + olamundobr + "!")

# Para colocar numeros em Strings - Inserir f no inicio
idade = 200
print(f"{olamundobr} eu tenho {idade} anos! ")

# Convertendo Texto para Numeros
convertendo_text_para_inteiro = int("50")
print(convertendo_text_para_inteiro)
convertendo_text_para_float = float("50.655")
print(convertendo_text_para_float)
