import requests
import csv
from bs4 import BeautifulSoup

csv_output_file = csv.writer(open('gastos_parlamentares_bolsonaros_2009_2018.csv', "w"))
fieldnames = ["Codigo do Reembolso", "Nome do Parlamentar", "Ano do Gasto", "Tipo da Cota", "Fornecedor", "Valor"]
csv_output_file.writerow(fieldnames)

link = "https://jarbas.serenata.ai/dashboard/chamber_of_deputies/reimbursement/?p=0&q=bolsonaro"
page = requests.get(link)
soup = BeautifulSoup(page.content,"html.parser")
numberOfPages = int(soup.find(class_="end").get_text())

for pageNumber in range(numberOfPages):
    print("Scrapping page number: " + str(pageNumber))
    link = "https://jarbas.serenata.ai/dashboard/chamber_of_deputies/reimbursement/?p=" + str(pageNumber) + "&q=bolsonaro"
    page = requests.get(link)

    soup = BeautifulSoup(page.content,"html.parser")

    table = soup.find("table")
    count = 0
    innerCount = 0

    for row in table.find_all("tr"):
        cells = row.find_all("td")
        count = 0
        csvRow = []

        for cell in cells:
            if count != 1 and count != 2:
                csvRow.append(str(cell.contents[0]))
            count += 1
        if innerCount != 0:
            csv_output_file.writerow(csvRow)
        innerCount += 1
    print("----")
