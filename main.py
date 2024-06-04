#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import json
from rich.console import Console
from rich.table import Table
page = requests.get("https://results.eci.gov.in/PcResultGenJune2024/index.htm")

soup = BeautifulSoup(page.text, 'html.parser')

data = {}
for table_row in soup.table.find_all("tr")[1:]:
    k = list(filter(lambda x: len(x) > 0, map(lambda x: x.strip(), table_row.text.split("\n"))))
    party_name = k[0]
    won = k[1]
    leading = k[2]
    total = k[3]
    data[party_name] = {"won": won, "leading": leading}


table = Table(title="Election India")

table.add_column("Party", justify='center', style='cyan', no_wrap=True)
table.add_column("Won", style="green")
table.add_column("Leading", style="magenta")


for key in data:
    l = data[key]
    table.add_row(key, l['won'], l['leading'])
console = Console()


console.print(table)
