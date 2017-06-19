import csv
import matplotlib.pyplot as plt

x_indonesia = []
y_indonesia = []
x_thailand = []
y_thailand = []
x_vietnam = []
y_vietnam = []




#https://pythonprogramming.net/legends-titles-labels-matplotlib-tutorial/?completed=/matplotlib-intro-tutorial/
#https://www.quandl.com/data/WPOV-World-Bank-Poverty-Statistics?keyword=thailand


with open('indonesia.csv','r') as csvfile_indonesia:
    plots = csv.reader(csvfile_indonesia, delimiter=',')
    next(plots, None) #skip header in file
    dot = []
    for row in plots:
        x_indonesia.append(row[0][0:4])
        for i, character in enumerate(row[1]):
            if character == '.':
                million = row[1][0:i]
                dot.append(i)
        if int(row[1][int(dot[0])+1]) >= 5:
                million = int(million) +1
        y_indonesia.append(million)

with open('thailand.csv','r') as csvfile_thailand:
    plots = csv.reader(csvfile_thailand, delimiter=',')
    next(plots, None) #skip header in file
    dot = []
    for row in plots:
        x_thailand.append(row[0][0:4])
        for i, character in enumerate(row[1]):
            if character == '.':
                million2 = row[1][0:i]
                dot.append(i)
        if int(row[1][int(dot[0])+1]) >= 5:
                million = int(million2) +1
        y_thailand.append(million2)

with open('vietnam.csv','r') as csvfile_vietnam:
    plots = csv.reader(csvfile_vietnam, delimiter=',')
    next(plots, None) #skip header in file
    dot = []
    for row in plots:
        x_vietnam.append(row[0][0:4])
        for i, character in enumerate(row[1]):
            if character == '.':
                million = row[1][0:i]
                dot.append(i)
        if int(row[1][int(dot[0])+1]) >= 5:
                million = int(million) +1
        y_vietnam.append(million)




plt.plot(x_indonesia,y_indonesia, label="Indonesia")
plt.plot(x_thailand, y_thailand, label="Thailand" )
plt.plot(x_vietnam, y_vietnam, label="Vietnam")


plt.xlabel('Year')
plt.ylabel('Million people')
plt.title('Number of poor at $4 a day')
plt.legend()
plt.show()


'''df = pd.read_csv('WPOV-IDN_SI_POV_NOP4.csv')
for line in df:
    print(line
    states = f.read().splitlines()
    return states'''


'''df.set_index('Date', inplace = True)

df.columns = ['House_Prices']
print(df.head())
df.to_html('example.html')'''
