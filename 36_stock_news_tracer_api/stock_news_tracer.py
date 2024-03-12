import requests
import smtplib
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = "bc9320cb70264b54bd4610491649b032"
STOCK_API_KEY = "K4YIVF287H2H71CE"

MY_GMAIL = "pydeveloper102@Gmail.com"
PASSWORD = "mmtzummbeadzndpy"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data_stock = response.json()

data_list = [value for (key, value) in data_stock["Time Series (Daily)"].items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
before_yesterday_data = data_list[1]
before_yesterday_closing_price = before_yesterday_data["4. close"]
differ = float(yesterday_closing_price) - float(before_yesterday_closing_price)
up_down = None
if differ > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"
differ_percent = round((differ / float(yesterday_closing_price)) * 100)

if abs(differ_percent) > 1:
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    response_news = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response_news.raise_for_status()
    data_news = response_news.json()["articles"]
    three_articles = data_news[:3]
    formatted_articles = [(f"{STOCK_NAME}: {up_down}{differ_percent}% Headline: {article['title']}."
                           f"Brief: {article['description']}") for article in three_articles]
    for article in formatted_articles:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_GMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_GMAIL,
                                to_addrs=MY_GMAIL,
                                msg=f"Subject: Article!\n\n{article.encode('utf8')}"
                                )
