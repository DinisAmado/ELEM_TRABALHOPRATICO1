# Take out the /n

"""
with open('all_perth.csv', 'r') as file:
    lines = file.readlines()

with open('all_perth.csv', 'w') as file:
    for i, line in enumerate(lines):
        if i == 0:
            file.write(line)
        if i % 2 == 0:
            file.write(line.rstrip('\n'))
        else:
            file.write(line)
"""

# Add the " at the end of each line exept the first

"""
with open('all_perth.csv', 'r') as file:
    lines = file.readlines()

with open('all_perth.csv', 'w') as file:
    file.write(lines[0])
    for line in lines[1:]:
        file.write('"' + line.rstrip('\n') + '"\n')
"""



# Take out the "
"""
with open('all_perth.csv', 'r') as file:
    lines = file.readlines()

with open('all_perth.csv', 'w') as file:
    for line in lines:
        if line.startswith('"'):
            file.write(line[1:])
        else:
            file.write(line)

"""

"""
# Change the format of the last column to just year

with open('all_perth.csv', 'r') as file:
    lines = file.readlines()

with open('all_perth.csv', 'w') as file:
    for line in lines:
        data = line.split(',')
        #data[-1] = data[-1][-4:]
        year = "\"" + data[-1][4:-2] + "\""
        print(year)
        data[-1] =  int(year)
        file.write(','.join(data) + '\n')
        #file.write(','.join(data))

"""

# Media de tempo de Venda (DateSold - Yearbuilt)
    # Skip nos NULLS



# Falta a soma do tempo de venda ==Done==
    # Falta a Media do tempo de venda das casas ==Done==
        # Soma do tempo de venda / numero de casas sem serem NULL

# Juntamos tambem as duas Databases all_perth e Property_Sales
    # Verificamos os Dups (checkdDups.py)
        # Retiramos os Dups (together.csv)

# Utilizamos o main.py para calcular a media do together.csv ==Done==
    # Erro pois no Property_Sales nao tem o ano de construcao, é void nem sequer é NULL ==Done==
        # Temos que tar a espera de voids ==Done==

# Transformar o as datas do Property_Sales em ano apenas ==Done==


# Comparar preco com o numero de quartos
    # 

import matplotlib.pyplot as plt

def operations(option,path):

    csv_path = path

    # Option 1
    somaNumCasas   = 0
    somaSkippedHouses = 0
    somaTempoVendaTotal = 0
    somaTempoVendaMedia = 0

    # Option 2
    #roomsList = []
    #priceList = []


    precosMedios = {
        # NroQuartos: [TotalOcorrencias, Soma dos Precos]
        # EX:
        #   1:  [0,0],
    }


    # Media de tempo de Venda (DateSold - Yearbuilt)
    if(option == "1"):
        with open(csv_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('Address'):
                    # Estamos no cabecalho, passamos a frente
                    continue
                data = line.split(',')
                
                # Rows Data // Not used is commented
                #adress      =  data[0]
                #suburb      =  data[1]
                #price       =  data[2]
                #rooms       =  data[3]
                #bathroom    =  data[4]
                yBuilt      =  data[5]
                ySold       =  data[6]

                if yBuilt != 'NULL' and ySold != 'NULL' and yBuilt != '' and ySold != '':
                    yearBuilt = int(yBuilt)
                    yearSold = int(ySold[1:-2])
                    timeToSell = yearSold - yearBuilt
                    print("Built: " + str(yearBuilt) + 
                        "; Sold: " + str(yearSold) + 
                        "; Time: " + str(timeToSell))
                    somaTempoVendaTotal += timeToSell
                    somaNumCasas += 1
                else:
                    print("Skipping: " + line)
                    somaSkippedHouses+=1



        print("-----------------------------------------")
        print("somaTempoVendaTotal: " + str(somaTempoVendaTotal))
        print("SomaNumHouses: " + str(somaNumCasas))
        print("SomaSkippedHouses: " + str(somaSkippedHouses))

        print("-----------------------------------------")
        somaTempoVendaMedia = somaTempoVendaTotal/somaNumCasas
        somaTempoVendaMedia = round(somaTempoVendaMedia, 2)
        print("Media: " + str(somaTempoVendaMedia) + " anos.")


    # 2 Preco - Número Quartos
    # 3 Preco- Número casas de banho
    # 4 Preco - Suburbios
    # 5 Preco - Ano de Venda
    elif(option == "2" or option == "3" or option == "4" or option == "5"):
        with open(csv_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('Address'):
                    # Estamos no cabecalho, passamos a frente
                    continue
                data = line.split(',')
                
                # Rows Data // Not used is commented
                adress      =  data[0]
                #suburb      =  data[1]
                price       =  data[2]
                #rooms       =  data[3]
                #bathroom    =  data[4]
                #yBuilt      =  data[5]
                #ySold       =  data[6]

                # We don't use those variables as we don't want to save more data than required
                # So we use a variable named "OptionData" that will grab the specific data required for a certain option
                # Those variables are there for visualization purposes

                # Option 2 OptionData = Rooms
                if option == "2":
                    OptionData = data[3]
                # Option 3 OptionData = Bathrooms
                if option == "3":
                    OptionData = data[4]
                # Option 4 OptionData = Suburb
                elif option == "4":
                    OptionData = data[1]
                # Option 5 OptionData = YearSold
                elif option == "5":
                    OptionData = int(data[6][1:-2])

                # Checks if the OptionData is not Null nor void, Or else there will be an error to calculate anything with that data
                if price != 'NULL' and OptionData != 'NULL' and price != '' and OptionData != '':

                    numPrice = int(price)
                    
                    # Na option 4 (suburb), os suburbs são strings
                    if option == "4":
                        numOptionData = OptionData
                    # Nos outros é para transformar em inteiros
                    else:
                        numOptionData = int(OptionData)

                    # Debug depending on OptionData
                    if option == "2":
                        print("Adress: " + str(adress) + 
                        "; Rooms: " + str(numOptionData) + 
                        "; Price: " + str(numPrice))

                    elif option == "3":
                        print("Adress: " + str(adress) + 
                        "; Bathrooms: " + str(numOptionData) + 
                        "; Price: " + str(numPrice))

                    elif option == "4":
                        print("Adress: " + str(adress) + 
                        "; Suburb: " + str(numOptionData) + 
                        "; Price: " + str(numPrice))

                    elif option == "5":
                        print("Adress: " + str(adress) + 
                        "; Year Sold: " + str(numOptionData) + 
                        "; Price: " + str(numPrice))


                    #roomsList.append(numOptionData)
                    #priceList.append(numPrice)

                    # Caso não haja ainda no dicionario este numero de quartos, inicia-se
                    if numOptionData not in precosMedios:
                        precosMedios[numOptionData] = [0,0]
                    
                    #Adicionar +1 nas ocorrencias
                    precosMedios[numOptionData][0] += 1
                    #Adicionar o preco a soma
                    precosMedios[numOptionData][1] += numPrice

                    somaNumCasas += 1
                    
                else:
                    somaSkippedHouses+=1
                    print("Skipping house: " + adress)



        print("-----------------------------------------")
        print("SomaNumHouses: " + str(somaNumCasas))
        print("SomaSkippedHouses: " + str(somaSkippedHouses))
        print("-----------------------------------------")
        print("Printing Graph...")
        

        #"""
        # set the xlim
        #plt.xlim(1, 24)
        # Numero de Quartos || Precos medios por Numero de Quartos (Soma de Precos em cada numero de quartos / Total de ocorrencias desse numero de quartos)
        # Na option 4 é para mostrar o nome do Suburbio, logo é preciso utilizar string e não numeros
        if option == "4":
            plt.bar([str(i) for i in precosMedios.keys()], [int(precosMedios[i][1]/precosMedios[i][0]) for i in precosMedios.keys()])
        else:
            plt.bar([int(i) for i in precosMedios.keys()], [int(precosMedios[i][1]/precosMedios[i][0]) for i in precosMedios.keys()])

        if option == "2":
            plt.title("Preco por Número Quartos")
            plt.xlabel("Numero de Quartos")
        elif option == "3":
            plt.title("Preco por Número Casas de Banho")
            plt.xlabel("Numero de Casas de Banho")
        elif option == "4":
            plt.title("Preco por Suburbios")
            plt.xlabel("Nome do Suburbio")
        elif option == "5":
            plt.title("Preco por Ano de Venda")
            plt.xlabel("Ano de Venda")

        plt.ylabel("Preco")
        plt.show()

        #"""
        


    else:
        print("Option unavailable\n")
        UI()

#tempoVenda("1",'together.csv')

def UI():
    print("----------------- MAIN MENU -----------------")
    print("1. Media de tempo de Venda")
    print("2. Preco - Número de Quartos")
    print("3. Preco - Número de Casas de Banho")
    print("4. Preco - Suburbios")
    print("5. Preco - Ano de Venda")
    print("0. Exit")
    option = str(input("\nChoose an option: "))
    if option != "0":
        operations(option,'together.csv')
        UI()
    else:
        print("Exiting...")
        return


UI()