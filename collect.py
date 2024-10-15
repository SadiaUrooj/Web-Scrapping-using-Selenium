#beautiful soup is used to parse the html to extract imformation from it
from bs4 import BeautifulSoup
import os
import re
import pandas as pd

d={'title':[], 'price':[], 'link':[]}
for file in os.listdir("data"):
    with open(f"data/{file}", encoding="utf-8") as f:
        html_doc = f.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    # t=soup.find("a", class_ ="ic-dynamic-badge ic-dynamic-badge-143722 ic-dynamic-group-3")
    # # t=soup.find(class_="aBrP0")
    # title=t.get_text()
    # print(title)
    # break
    # t=soup.find(class_="aBrP0")
    # t=soup.find_all("a")

    # Find title
    a_tag = soup.find("a", title=True)  # Example: <a title="...">
    if a_tag and 'title' in a_tag.attrs:
            title = a_tag['title']
    else:
            title = 'No title found'
    d['title'].append(title)

    # Find price (using a regex or a specific class)
    price_tag = soup.find("span", class_=re.compile(r'ooOxS'))  # Example price class
    price = price_tag.get_text() if price_tag else 'No price found'
    d['price'].append(price)

    # Find link (from <a> tag)
    link_tag = soup.find("a", href=True)  # Example: <a href="...">
    if link_tag and 'href' in link_tag.attrs:
            link = link_tag['href']
            
    else:
            link = 'No link found'
    d['link'].append(link)

    # Print the extracted data
for i in range(len(d['title'])):
    print(f"Title: {d['title'][i]}")
    print(f"Price: {d['price'][i]}")
    print(f"Link: {d['link'][i]}")
    print("\n")
df=pd.DataFrame(data=d)
df.to_csv("data.csv")
    # print(soup.prettify())