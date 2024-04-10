# Change the format of the last column to just year

# It's commented cuz it destroys years if used when it's not meant to be
    # This code turns the dd-mm-yyyy into "yyyy" to be used by main.py
"""
path = "Property_Sales.csv"

with open(path, 'r') as file:
    lines = file.readlines()

with open(path, 'w') as file:
    for line in lines:
        data = line.split(',')
        #data[-1] = data[-1][-4:]
        year = "\"" + data[-1][-5:-1] + "\""
        print(year)
        data[-1] =  str(year)
        file.write(','.join(data) + '\n')
        #file.write(','.join(data))
"""