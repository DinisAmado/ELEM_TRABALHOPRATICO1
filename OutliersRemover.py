import pandas as pd

csv = pd.read_csv('together.csv')

#descobrir o adress que corresponde ao maior valor de bedroom
for i in range(len(csv['Bedroom'])):
    if csv['Bedroom'][i] == 20:
        print(csv['Address'][i])

#descobrir o adress que corresponde ao maior valor de bathroom
for i in range(len(csv['Bathroom'])):
    if csv['Bathroom'][i] > 10:
        print(csv['Address'][i])

#Se o código foi executado e não teve nenhum output é porque já foram apagados


