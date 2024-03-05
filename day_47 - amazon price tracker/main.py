import requests
from bs4 import BeautifulSoup


AMAZON_URL = "https://www.amazon.pl/BRUBECK-Wygodne-merynosów-Barefoot-jasnoniebieski/dp/B0C5G9L8J8/ref=is_sr_s_dp_2?__mk_pl_PL=%EF%BF%BDM%EF%BF%BD%7D%EF%BF%BD%EF%BF%BD&crid=2OB1ZXI229C43&dib=eyJ2IjoiMSJ9.RpP8WI27QxPXIgDhTJ4yDNwRbeBll2K_j_EA165cayw329_kzdyRV4KxAm-TdtP69KEy1rQ-PLiOSkE6Cw0-UdgfZO2cIHFOq_F4ObyG2Zr0wSqEvI-DYoEOJ8NoVdXPZOKjJae0TjvkfsBlpdcLlrj0p64vzybGEXlmslE83GFX7KBAk7M6YRl3ujsdHnUB5ax9npyu4vRg4ZRr2i-NobtXA8JuBRoCHWe2f_mZmL4MAoJI9jMnqi1gu1Sv1vtCAzl6TSZaHdtLsw40A8up3bJjkDQCMKBNn0nklo5qWL8.o41sBSgssLxRNbID-jUjhOiXSdaaSNovBX3---zG4O0&dib_tag=se&keywords=barefoot&qid=1709647736&refinements=p_n_size_browse-vebin%3A20923142031%2Cp_123%3A237926%7C242500%7C304993%7C71113&rnid=91049082031&s=fashion&sprefix=barefoot%2Caps%2C103&sr=1-4&th=1&psc=1"

header = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15",
    "Accept-Language":"pl-PL,pl;q=0.9"
}

r = requests.get(url=AMAZON_URL, headers=header).text


soup = BeautifulSoup(r, 'html.parser')

print(soup.prettify())