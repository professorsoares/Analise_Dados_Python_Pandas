# **Curso Python Para Análise de dados** - *Fernanda Santos*

# **Estrutura de dados**

## **Listas**

#Criando uma lista chamada animais

animais = [1,2,3]
print(animais)
print("-------------------------------------------------")

animais = ["cachorro", "gato", 12345, 6.5]
print(animais)
print("-------------------------------------------------")

#Imprimindo o primeiro elemento da lista
print(animais[0])
print("-------------------------------------------------")

#Imprimindo o 4 elemento da lista
print(animais[3])
print("-------------------------------------------------")

#Substituindo o primeiro elemento da lista
animais[0] = "papagaio"
print(animais)
print("-------------------------------------------------")

#Removendo gato da lista
animais.remove("gato")
print(animais)
print("-------------------------------------------------")

len(animais)
"gato" in animais
lista = [500, 30, 300, 80, 10]
print("MAX: " + str(max(lista)))
print(min(lista))
print("-------------------------------------------------")

animais.append(["leão", "Cachorro"])
print(animais)
print("-------------------------------------------------")

animais.extend(["cobra", 6])
print(animais)
print("-------------------------------------------------")

animais.count("leão")
lista.sort()
print(lista)
print("-------------------------------------------------")

# **Tuplas**

#As tuplas usam parênteses como sintaxe
tp = ("Banana", "Maçã", 10, 50)
#Retornando o primeiro elemento
print(tp[0])
print("-------------------------------------------------")

#Diferente das listas as tuplas são imutáveis, o que quer dizer que não podemos alterar os seus elementos
# tp[0] = "Laranja"  -> Dá erro se retirar o comentário.
tp.count("Maçã")
print(tp[0:2])
print("-------------------------------------------------")

# **Dicionários**

#Para criar um dicionário utilizamos as {}
dc = {"Maçã":20, "Banana":10, "Laranja":15, "Uva":5} #Dicionários trabalham com o condeito chave e valor
print(dc)
print("-------------------------------------------------")

#Acessando o valor de um dicionário através da chave
dc["Maçã"]
print("-------------------------------------------------")

#Atualizando o valor da Maçã
dc["Maçã"] = 25
dc
print("-------------------------------------------------")

#Retornando todas as chaves do dicionário
dc.keys()
print("-------------------------------------------------")

#Retornando os valores do dicionário
dc.values()
print("-------------------------------------------------")

#Verificando se já existe uma chave no dicionário e caso não exista inserir
dc.setdefault("Limão", 22)
dc
print("-------------------------------------------------")

