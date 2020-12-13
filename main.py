import requests
import bs4
from tkinter import *
from tkinter import messagebox


def getdatafrombnr():
    # Request catre BNR pentru pagina de curs valutar
    res = requests.get('https://www.bnr.ro/Cursul-de-schimb-524.aspx')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    data = {}
    data['RON'] = 1
    table_body = soup.find('tbody')
    rows = table_body.find_all('tr')
    # Contruim un Dict "data" folosing ca key coloana a doua de pe fiecare rand iar ca value ultima valoare din tabela
    for row in rows:
        cols = row.find_all('td')
        data[cols[1].text] = cols[6].text.replace(',', '.')
    return data

def get_all_curency():
    lista = list()
    data = getdatafrombnr()
    for x in data.keys():
        lista.append(x)
    return lista

def exchange(currency):
    data = getdatafrombnr()
    return data[currency]

def from_curency_to_curency(value, currency1, currency2):
    first_currency = float(exchange(currency1))
    second_currency = float(exchange(currency2))
    rate = first_currency / second_currency
    money_received = value * rate
    return float(money_received)

def click(selection):
    print(selection)

def dropdown_clicked(selection):
    global f_curency
    f_curency = selection
    print(f_curency)

def dropdown2_clicked(selection):
    global s_curency
    s_curency = selection
    print(s_curency)

def test():
    firstCurrency = float(exchange(f_curency))
    secondCurrency = float(exchange(s_curency))
    rate = firstCurrency / secondCurrency
    first_field = e.get()
    if first_field.isnumeric() == True:
        value_returned = rate * float(e.get())
        print(value_returned)
        label_result.config(text=("Primesti: " + str(value_returned) + " "+s_curency))
    else:
        messagebox.showerror("Eroare catastrofala","Doar valorile numerice sunt permise")



global f_curency
global s_curency

f_curency = "RON"
s_curency = "RON"
data = get_all_curency()
firstValue = get_all_curency()
program = Tk()
program.title("Schimb valutar")
program.minsize(700, 400)
program.resizable(None, None)
program.maxsize(701, 401)
label1 = Label(program, text="Introdu suma:", pady=15)
label1.pack()
e = Entry(program, width=25)
e.pack()
clicked = StringVar()
dropdown1 = OptionMenu(program, clicked, *get_all_curency(), command=dropdown_clicked)
dropdown1.pack()
label2 = Label(program, text="Selecteaza moneda in care vrei sa convertesti", pady=7)
label2.pack()
clicked2 = StringVar()
dropdown2 = OptionMenu(program, clicked2, *get_all_curency(), command=dropdown2_clicked)

dropdown2.pack()
myButton = Button(program, text="Converteste", padx=30, pady=15, fg="green", command=test)
myButton.pack()
label_result = Label(program,text=" ",pady=7)
label_result.pack()
program.mainloop()
