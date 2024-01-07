import requests
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVENTAGE_API_KEY = "0PMP909CLEG52S9G"
NEWS_API_KEY = "c1111645082e459ebafad4ac416efef8"
TODAY = datetime.datetime.today().date()
YESTERDAY = TODAY - datetime.timedelta(days=1)
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

def get_news(topic):
    news_parameters = {
        "q":topic,
        "from":str(YESTERDAY- datetime.timedelta(days=1)),
        "to": str(TODAY),
        "sortBy":"popularity",
        "apiKey":NEWS_API_KEY,
        "language":"en",
        "pageSize":3,
    }
    response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    data = response.json()
    if data['status'] == 'ok':
        return data['articles']
    else:
        raise ValueError("News API error!")



# alphavantage API call for stock price 
stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "outputsize":"compact",
    "datatype":"json",
    "apikey":ALPHAVENTAGE_API_KEY
}

r = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
r.raise_for_status()
stock_data = r.json()
message = ""
print(stock_data)
last_refreshed = stock_data['Meta Data']['3. Last Refreshed']
stock_data_list = [value for (key,value) in stock_data['Time Series (Daily)'].items()]


if last_refreshed == str(YESTERDAY):
    
    yesterday_close_price = float(stock_data['Time Series (Daily)'][str(YESTERDAY)]['4. close'])
    before_yesterday_close_price = float(stock_data['Time Series (Daily)'][str(YESTERDAY - datetime.timedelta(days=1))]['4. close'])

    close_value_change = abs(yesterday_close_price - before_yesterday_close_price)
    percent_close_value_change = (close_value_change / yesterday_close_price * 100)

    message += f"{COMPANY_NAME} - {YESTERDAY} close value: {yesterday_close_price}$  - {YESTERDAY - datetime.timedelta(days=1)} close value: {before_yesterday_close_price}$, value change: {percent_close_value_change}% \n\n"
    
    # check if price increase/decreases by 5% between yesterday and the day before yesterday
    if percent_close_value_change > 5:
        news_articles = get_news(topic=COMPANY_NAME)
        articles_list = []
        for article in news_articles:
            message += f"{article['title']} - {article['description']} - {article['url']}\n\n"
        print(message)
    else:
        print(close_value_change)
        print(message)

