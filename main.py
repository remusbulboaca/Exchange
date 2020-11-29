import requests
import bs4
from tkinter import *

def getDataFromBNR():
    # Request catre BNR pentru pagina de curs valutar
    res = requests.get('https://www.bnr.ro/Cursul-de-schimb-524.aspx')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    data = {}
    table_body = soup.find('tbody')
    rows = table_body.find_all('tr')
    # Contruim un Dict "data" folosing ca key coloana a doua de pe fiecare rand iar ca value ultima valoare din tabela
    for row in rows:
        cols = row.find_all('td')
        data[cols[1].text] = cols[6].text.replace(',', '.')
    return data

def getAllCurency():
    lista = list()
    data = getDataFromBNR()
    for x in data.keys():
        lista.append(x)
    return lista

def exchange(currency):
    data = getDataFromBNR()
    return data[currency]

def fromCurrencyToCurrency(value,currency1, currency2):
    firstCurrency = float(exchange(currency1))
    secondCurrency = float(exchange(currency2))
    rate = firstCurrency / secondCurrency
    moneyReceived = value * rate
    return float(moneyReceived)

def click(selection):
    print(selection)

program = Tk()
program.title("Schimb valutar")
program.minsize(700,400)
program.resizable(None,None)
program.maxsize(701,401)
label1 = Label(program,text="Introdu suma:",pady=15)
label1.pack()
e = Entry(program, width=25)
e.pack()
clicked = StringVar()
dropdown1 = OptionMenu(program,clicked,*getAllCurency())
dropdown1.pack()
label2 = Label(program,text=" ",pady=7)
label2.pack()
myButton = Button(program,text="Converteste",padx=30,pady=15, fg="green", command=click(dropdown1.selection_get()))
myButton.pack()
program.mainloop()