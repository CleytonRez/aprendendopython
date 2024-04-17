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

# Listas
lista_de_nomes = ["Jorge", "Carlos", "Vagner"]
print(lista_de_nomes)

# Adicionar novo dado no final da lista - .append
lista_de_nomes.append("Cleber")
print(lista_de_nomes)

# Adicionar novo dado em posição especifca - .insert
lista_de_nomes.insert(0, "Geraldinho")
print(lista_de_nomes)

# Remover dado em posição especifca - .remove
lista_de_nomes.remove("Vagner")
print(lista_de_nomes)

# Ordenar Lista de numeros.
idades = [20,30,32,22]
idades.sort()
print(idades)

# Repetiçao / Loop
# While / For 
# While geralmente usado em listas que não sabe quando termina
meta_vendas = 10
vendas = 0

while vendas < meta_vendas:
    print (f"Vende mais! Só foi {vendas}")
    vendas = vendas + 1

# For usado para percorrer a lista toda quando sabe que tem fim.

nomes = ["Carlos", "Priscila" , "Robson"]
for nome in nomes:
    print(nome)

