import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "XS4BXIXS4MR693E"
NEWS_API_KEY = "0c7a52f19f434b5cb5f943c2b31e2bbc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_SID = "AC10c0f590d3118a16821715aae2c053a5"
TWILIO_AUTH_TOKEN = "f26c367fe09f4a77f7c032987bb9b7ca"

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yesterday's closing stock price. 

# Get an API
parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

diff = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
percent_change = round((float(yesterday_closing_price) - float(day_before_yesterday_closing_price)) / float(day_before_yesterday_closing_price) * 100)
up_down = None

if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


if abs(percent_change) > 0.1:
    ## STEP 2: Use https://newsapi.org/docs/endpoints/everything
    # Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
    #HINT 1: Think about using the Python Slice Operator
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number. 
    #HINT 1: Consider using a List Comprehension.
    
    formatted_articles = {f"{STOCK}: {up_down}{percent_change}%\nHeadline: {article['title']}. \n Brief: {article['description']}" for article in three_articles}

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages \
                    .create(
                        body=article,
                        from_="+18059181349",
                        to="+66955429616"
                    )
        print(message.status)
    
# # Optional: Format the SMS message like this: 
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file 
# by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of 
# the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file 
# by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of 
# the coronavirus market crash.
# """


