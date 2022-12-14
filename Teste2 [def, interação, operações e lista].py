#Códigos de teste, função "def"
import time
#criando funções simples.
def calculadora(a,b): #calcular números criando uma função.
    return a+b, a-b, a*b, a/b
print('números informados pelo usuário farão parte de operações simples, como soma, subtração, multiplicação e divisão. depois do recolhimento dos númmeros, o resultado será informado na forma "(+, -, *, /)".'.upper())
a = int(input('digite um número inteiro:\n'.capitalize()))
b = int(input('digite outro número inteiro:\n'.capitalize()))
print(calculadora(a,b))
#adicionar dados em uma lista vazia por meio da função "def".
print('perguntas serão feitas, e alguns de seus dados serão armazenados em uma lista.'.capitalize())
lista_vazia = []
perg_1 = str(input('informe seu nome:\n'.capitalize()))
perg_2 = int(input('informe a sua idade:\n'.capitalize()))
def dados(perg_1, perg_2):
    lista_vazia = [perg_1, perg_2] #a  função "append" daria certo. Porém, é sempre bom poupar linhas.
    print(lista_vazia)
print('aguarde...'.capitalize())
time.sleep(2)
print('armazenamento de dados realizado.'.upper())
dados(perg_1, perg_2)