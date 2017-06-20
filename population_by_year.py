import csv
import re
import sys

#Prints the population numbers by year for the chosen country, rounded to the full million,
#based on a csv file by the Worldbank.
#shttp://data.worldbank.org/indicator/SP.POP.TOTL?locations=ID&view=chart

country = input("Enter a country: ")
country_alt = country[0].upper() + country[1:]

##reading in the csv with the population data

with open('pop.csv', newline='', encoding='utf_8') as csvfile_population:
    reader = csv.reader(csvfile_population)
    content = list(reader)

#extracting, slicing and preparing the population data

year_list = []
population_list = []
pop_dict = {}

for number, lists in enumerate(content):
    for item in lists:
        if item == "Country Name":
            year_list.append(content[number])

years = [item for sublist in year_list for item in sublist[4:-1]]

for number, lists in enumerate(content):
    for item in lists:
        if item == country or item == country_alt:
            population_list.append(content[number])

if not population_list:
    print("There is no data for this country available, or it is spelled differently.")
    sys.exit()


population = [item for sublist in population_list for item in sublist[4:-2]]

#rounding the population numbers to millions, appending them to a new list'''

pop_rounded = []
for item in population:
    x = str(item)
    b = x[:-6]
    c = int(b)
    if int(x[-6]) >= 5:
        c += 1
    pop_rounded.append(c)

for number in range(56):
    print("%s: %s million" % (years[number],pop_rounded[number]))
