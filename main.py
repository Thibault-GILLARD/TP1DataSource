from flask import Flask, request, render_template
import requests

import os
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)
import pytrends

import os
import pandas as pd
import itertools
from flask import jsonify


#import strimlit as st

# TP3
# --------------------------------- #
property_id = "407435764"
starting_date = "30daysAgo"
ending_date = "yesterday"

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/thibaultgillard/Documents/EPF/5A/Data_Source/TP1/key.json'

client = BetaAnalyticsDataClient()

request_api = RunReportRequest(
    property=f"properties/{property_id}",
    dimensions=[Dimension(name="sessionSource")],
    metrics=[
             Metric(name="totalUsers"),
             ],
    date_ranges=[DateRange(start_date=starting_date, end_date=ending_date)],
)
try:
    response = client.run_report(request_api)
    print("Data access successful.")
except Exception as e:
    print("Error accessing Google Analytics data:", str(e))
# --------------------------------- #


# TP4
# --------------------------------- #
from pytrends.request import TrendReq
import time

def get_interest(pytrend, kw_list, geo):
    max_retries = 5
    retries = 0
    df = None
     
    while retries < max_retries:
        try:
            pytrend.build_payload(kw_list=kw_list, timeframe='today 5-y', geo=geo)
            df = pytrend.interest_over_time()
            break  # Success, exit the loop
        except Exception as e:
            print(f"Error: {e}")
            retries += 1
            time.sleep(2)
    
    return df
 
pytrend = TrendReq(hl='en-US', tz=360)
kw_list = ["Israel"]
geo = 'US'
df = get_interest(pytrend, kw_list, geo)
print(df)
# --------------------------------- #


app = Flask(__name__, template_folder='templatesTP')

@app.route("/", methods=['GET', 'POST'])
def main():
    cookies = None
    row_count = None
    logged_text = None  # Initialize for logging text

    if request.method == 'POST':
        if 'get_cookies' in request.form:
            try:
                req = requests.get("https://analytics.google.com/analytics/web/#/p407435764/reports/dashboard?r=reporting-hub")
                cookies = req.cookies
            except:
                return "Error"

        if 'fetch_data' in request.form:
            try:
                # Execute the report request to fetch the data
                response = client.run_report(request_api)
                row_count = response.row_count
            except Exception as e:
                return f"Error: {str(e)}"

        # Check for logged text
        logged_text = request.form.get('textarea')  # Get text from the textarea

    return render_template('main.html', cookies=cookies, row_count=row_count, logged_text=logged_text)

# TP4
# --------------------------------- #
@app.route("/trend", methods=['GET', 'POST'])
def trend_form():
    title = "why not"
    keywords = ["yes", "no", "maybe"]
    data = []  # Initialize data as an empty list

    if request.method == "POST":
        title = request.form.get("title")
        keywords_text = request.form.get("keywords")

        # Split the user input into a list of keywords
        keywords = [keyword.strip() for keyword in keywords_text.split('\n')]

        # Initialize a PyTrends client
        pytrend = TrendReq(hl='en-US', tz=360)
        print("PyTrend object initialized:", pytrend)  # Add this line for debugging

        # Get interest data for the provided keywords
        for keyword in keywords:
            df = get_interest(pytrend, [keyword], geo='')
            data.append({
                "keyword": keyword,
                "interest_data": df.to_json(orient='split')  # Serialize the DataFrame
            })

    print("Data:", data)  # Add this line to print the data for debugging

    return render_template("trend.html", data=data, title=title, keywords=keywords)

def get_interest(pytrend, keywords, geo):
    pytrend.build_payload(keywords, cat=0, timeframe='today 5-y', geo=geo, gprop='')
    df = pytrend.interest_over_time()
    return df

@app.route("/trend2", methods=['GET', 'POST'])
def trend_form2():
    data = {}  # Initialize data as an empty dictionary

    if request.method == 'POST':
        # Make a request to Google
        try:
            pytrend = TrendReq(hl='en-US', tz=360)
            kw_list = ["Israel"]
            geo = 'US'
            df = get_interest(pytrend, kw_list, geo)

            # Extract the required data
            labels = df.index.strftime('%Y-%m-%d').tolist()
            values = df['Israel'].tolist()

            data = dict(zip(labels, values))
            print(data)

            # Format data for Chart.js
            chart_labels = labels
            chart_data = values
            print(chart_labels)
            print(chart_data)
        except Exception as e:
            return f"Error: {str(e)}"

        return render_template('trend.html', labels=chart_labels, data=chart_data)

    return render_template('trend.html', labels=[], data=[])



# --------------------------------- #

@app.route("/root")
def root():
    prefix_google = """
    <!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-WVM9JHZGF4"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-WVM9JHZGF4');
</script>"""

    # This is the button that we will be displayed on the page
    button_html = """
    <button onclick="sendEventToGA()">Click Me</button>"""
    
    # This is the code that will be executed when the button is clicked
    button_click_tracking = """ 
    <script>
        function sendEventToGA() {
            gtag('event', 'button_click', {
                'event_category': 'Custom Event Category',
                'event_label': 'Button Clicked'
            });
        }
    </script>
    """
  
    return prefix_google + "Hello from Space!" + button_html + button_click_tracking


@app.route("/logger",methods=['GET', 'POST'])
def logger():

    if request.method == 'POST':
        text = request.form.get('textarea')
        print(text)
        
        return render_template('logger.html', text=text)

    return render_template('logger.html')

@app.route("/cookies",methods=['GET', 'POST'])
def cookies():
    if request.method == 'POST':
        # Make a request to Google
        try:
            req = requests.get("https://analytics.google.com/analytics/web/#/p407435764/reports/dashboard?r=reporting-hub")
            # Get the cookies in cookies.html
            cookies = req.cookies
            # Return the cookies
            
            eq2 = requests.get("https://www.googletagmanager.com/gtag/js?id=G-WVM9JHZGF4")
            return render_template('cookies.html', cookies=cookies)
        except:
            return "Error"
         
    return render_template('cookies.html')

@app.route("/ana", methods=['GET', 'POST'])
def ana():
    if request.method == 'POST':
        try:
            # Execute the report request to fetch the data
            response = client.run_report(request_api)

            # Extract the row count because it corresponds to the number of users
            row_count = response.row_count

            return render_template('ana.html', row_count=row_count)
        except Exception as e:
            return f"Error: {str(e)}"

    return render_template('ana.html')




if __name__ == "__main__":
    app.debug = True
    app.run()
