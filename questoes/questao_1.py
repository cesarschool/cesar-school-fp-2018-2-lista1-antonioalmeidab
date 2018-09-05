## QUESTÃO 1 ## 
# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o 
# valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do 
# novo salário. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    salario = int(input("Qual o valor do salário?"))
    porcentagemaumento = int(input("De quantos por cento foi o aumento?"))
    
    multiaumento = porcentagemaumento/100
    aumento = salario * multiaumento
    novosalario = salario + aumento

    print("O aumento será de", aumento, "e o novo salário será", novosalario)  
    


if __name__ == '__main__':
    main()