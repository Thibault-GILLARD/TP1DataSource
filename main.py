from flask import Flask, request, render_template
from logging.config import dictConfig
import requests

import os
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)

import os
import pandas as pd
import itertools

#import strimlit as st

property_id = "407435764"
starting_date = "30daysAgo"
ending_date = "yesterday"

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/thibaultgillard/Documents/EPF/5A/Data Source/TP1/My First Project IAM.json'

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
    
    
app = Flask(__name__, template_folder='templatesTP')

#port = 5001

#SCOPES = ['https://www.googleapis.com/auth/analytics.readonly'] # Liste des scopes que nous allons utiliser

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

@app.route("/", methods=['GET', 'POST'])
def main():
    cookies = None
    row_count = None

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

    return render_template('main.html', cookies=cookies, row_count=row_count)


if __name__ == "__main__":
    app.run()
