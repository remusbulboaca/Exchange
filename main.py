import requests
import bs4

def exchange(currency):
    # Request catre BNR pentru pagina de curs valutar
    res = requests.get('https://www.bnr.ro/Cursul-de-schimb-524.aspx')
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    data = {}
    table_body = soup.find('tbody')
    rows = table_body.find_all('tr')
    #Contruim un Dict "data" folosing ca key coloana a doua de pe fiecare rand iar ca value ultima valoare din tabela
    for row in rows:
        cols = row.find_all('td')
        data[cols[1].text] = cols[6].text.replace(',','.')
    return data[currency]

print(float(exchange('EUR'))*3)