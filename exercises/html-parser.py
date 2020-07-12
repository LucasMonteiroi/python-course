import requests as req, bs4

economyPage = req.get('https://www.dolarhoje.com')
soup = bs4.BeautifulSoup(economyPage.text, 'html.parser') # Using flag 'html-parser' will be parse the entire html and beutify
elems = soup.select('#nacional')
print(elems)