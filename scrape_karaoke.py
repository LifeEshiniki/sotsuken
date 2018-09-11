import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

user = input("input username.")

# table= pd.read_html("https://clubdam.info/user/" + user)

#print(table[0])

html = urlopen("https://clubdam.info/user/" + user)
bsObj = BeautifulSoup(html, "html.parser")

table = bsObj.find_all("table",attrs={"id": "raw_data_table"})

print(table)

