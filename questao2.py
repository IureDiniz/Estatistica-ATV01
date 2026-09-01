import matplotlib.pyplot as plt
import random
import timeit

def insertionSort(lista):
    for i in range(1, len(lista)):
        x = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > x:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = x

def media(l):
  soma = 0
  for i in range(len(l)):
    soma += l[i]
  return soma / len(l)

def mediana(l):
  insertionSort(l)

  if(len(l) % 2 == 0):
    return (l[(int) (len(l) / 2)] + l[(int) ((len(l) / 2) - 1)]) / 2
  else:
    return l[len(l) / 2]


def moda(l):
  maiorValor = 0
  maiorCont = 0
  for i in range(l):
    cont = 1
    for l in range(l):
      if l == i:
        cont += 1

    if cont > maiorCont:
      maiorCont = cont
      maiorValor = i

def amplitude(l):
  maior = l[0]
  menor = l[0]

  for i in range(len(l)):
    if l[i] > maior:
      maior = l[i]
    if l[i] < menor:
      menor = l[i]

  return maior - menor

def variancia(l):
  med = media(l)
  soma = 0

  for i in range(len(l)):
    soma += (l[i] - med) ** 2

  return soma / len(l)

def desvioPadrao(l):
  return variancia(l) ** 0.5

def coeficienteVariacao(l):
  return 100 * desvioPadrao(l) / media(l)

def contaQuantidades(l):
    quantidades = []

    for numero in set(l):
        quantidade = l.count(numero)
        quantidades.append((numero, quantidade))

    return quantidades

# PARTE PRINCIPAL

servA = [98, 102, 100, 101, 99, 103, 97, 100, 102, 98, 101, 99, 104, 100, 98, 102, 101, 99, 100, 103]
servB = [94, 105, 97, 108, 92, 110, 96, 104, 99, 107, 93, 109, 95, 106, 98, 111, 91, 103, 100, 112]

servA_quantidades = contaQuantidades(servA)
servB_quantidades = contaQuantidades(servB)

libraryA = []
chosen_byA = []

for numero, quantidade in servA_quantidades:
    libraryA.append(numero)
    chosen_byA.append(quantidade)


libraryB = []
chosen_byB = []

for numero, quantidade in servB_quantidades:
    libraryB.append(numero)
    chosen_byB.append(quantidade)




plt.figure()

plt.bar(libraryA, chosen_byA, color='skyblue')

plt.xlabel('Valor')
plt.ylabel('Quantidade de repetições')
plt.title('Quantidade de repetições - ServA')

plt.show()



plt.figure()

plt.bar(libraryB, chosen_byB, color='lightgreen')

plt.xlabel('Valor')
plt.ylabel('Quantidade de repetições')
plt.title('Quantidade de repetições - ServB')

plt.show()