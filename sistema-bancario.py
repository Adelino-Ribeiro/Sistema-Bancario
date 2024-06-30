LIMIT_SAQUES = 3
limitSaldo = 500
numeroSaques = 0
saldo = 1000
controller = True
extracto = ""

while (controller) :
    
    while (True) :
        
        opcao = int(input("1 - Sacar \n2 - Depositar \n3 - Consultar \n4 - Extracto \n5 - Sair \nInforme um valor: "))

        if (opcao > 0) :

            break
    

    if (opcao == 1) :
        
        valor = float(input("Qual é o valor a sacar: R$ "))

        if (valor > saldo) :

            print("Saldo insuficiente!")
        
        elif (limitSaldo != 0) :

            if ((limitSaldo - valor) < 0) :

                print("Passou o limite (R$ 500)")

            elif (numeroSaques == LIMIT_SAQUES) :

                print("Limite diario atinguido (3x).")              
            
            else :

                saldo -= valor

                limitSaldo -= valor
                
                numeroSaques += 1

                extracto += f"Saque: R$ {valor} \n"
                
                print("------------------------")
                
                print("Saque feito com sucesso!!!")
                
                print("Saque: R$", valor)
                
                print("Saldo: R$", saldo)
                
                print("Limite diario actual = ", (LIMIT_SAQUES - numeroSaques))
                
                print("------------------------")
                
                
         
        else :
            
            print("Limite diario atinguido (R$ 500)")

    elif (opcao == 2) :

        valor = float(input("Qual é o valor a depositar: R$ "))

        saldo += valor

        print("------------------------")

        extracto += f"Depositado: R$ {valor}\n" 
        
        print("Deposito feito com sucesso!!!")
        
        print("Depositado: R$", valor)
        
        print("Saldo: R$", saldo)
        
        print("------------------------")


    elif (opcao == 3) :

        print("------------------------")
        
        print("Saldo: R$", saldo)
        
        print("------------------------")

    elif (opcao == 4) :

        print("------------------------------------------------")
        print("|                    EXTRACTO                  |")
        print("------------------------------------------------")
        print("Nao foi realizado nenhum movimento!!!" if  not extracto else extracto)
        print("------------------------------------------------")

    elif (opcao == 5) :

        controller = False