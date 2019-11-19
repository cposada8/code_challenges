import requests
from bs4 import BeautifulSoup
url = "https://es.aliexpress.com/item/4000098592980.html?spm=a2g0o.productlist.0.0.1fc64194Wc1VbF&algo_pvid=7f4c8cc4-4656-4daa-bc37-e75ed6fab56b&algo_expid=7f4c8cc4-4656-4daa-bc37-e75ed6fab56b-0&btsid=b7284fb0-bdf1-4645-a643-5bb1e4ae0368&ws_ab_test=searchweb0_0,searchweb201602_10,searchweb201603_52"
url = "https://www.amazon.com/OnePlus-Factory-GM1917-Verizon-Tmobile/dp/B07RP2T469/ref=sr_1_15?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=oneplus&qid=1574121297&refinements=p_89%3AOnePlus&rnid=2941120011&s=mobile&sr=1-15"
my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"


headers = {"User-Agent": my_user_agent}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

print(type(soup))
# title = soup.find(id="productTitle")
title = soup.find('span', attrs={'id':'productTitle'})
print(len(soup.prettify()))

print(title)
