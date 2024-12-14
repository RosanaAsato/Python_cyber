# SOMA DE DOIS NUMEROS:  

# # programação estruturada 
# num1 = 4
# num2 = 10 
# soma = num1+num2
# print(soma)

# ------------------------
#utilizando funcoes 
numero1 = 4
numero2 = 10 
#definição
def somar_numeros():
    print(numero1+numero2)
#utilização    
somar_numeros()
#----------------------------

#parametros 
def somar_numeros(numero1,numero2):
    print(numero1 + numero2)

#posicionais - keyword
somar_numeros(4,10)
somar_numeros(numero2=10, numero1=4)