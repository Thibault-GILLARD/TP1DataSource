# TP1DataSource

Thibault Gillard

## TP2 Results

![yes](https://github.com/Thibault-GILLARD/TP1DataSource/blob/master/source/Video%20to%20GIF%202023-10-14%2017.28.43.gif?raw=true)

For the TP2 the stategie was to do the different tasks in different roots and when everything was working to merge them all together into the main root, with some css to make it look better.

First was to Manipulate cookies and logger:
    
```python
if request.method == 'POST':
        text = request.form.get('textarea')
        print(text)
        
        return render_template('logger.html', text=text)

    return render_template('logger.html')
````
```python
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
````

I used a render Template to display the cookies and the logger, and a request to get the cookies from the google analytics website.

Then for the Request with oauth i used this websit to help me :
https://www.lupagedigital.com/blog/google-analytics-api-python/

It was still hard...

And then I had to do specific request to get the data from the google analytics website:


```python
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
````

And finaly get the good information from 'response' and display it :

```python
# Execute the report request to fetch the data
response = client.run_report(request_api)

# Extract the row count because it corresponds to the number of users
row_count = response.row_count
```

At the end i could creat the main page with all the information and the css to make it look better using W3Schools.


## TP1 Results

Analytics Image

![Image Description](https://github.com/Thibault-GILLARD/TP1DataSource/blob/master/source/Capture%20d%E2%80%99%C3%A9cran%202023-09-25%20%C3%A0%2008.42.08.png?raw=true)

Dashboard Image

![Image Description](https://github.com/Thibault-GILLARD/TP1DataSource/blob/master/source/Capture%20d%E2%80%99%C3%A9cran%202023-09-19%20%C3%A0%2016.34.28.png?raw=true)

![Image Description](https://github.com/Thibault-GILLARD/TP1DataSource/blob/master/source/Capture%20d%E2%80%99%C3%A9cran%202023-09-25%20%C3%A0%2008.45.24.png?raw=true)

Bonus:

```html
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
```

![Image Description](https://github.com/Thibault-GILLARD/TP1DataSource/blob/master/source/Capture%20d%E2%80%99%C3%A9cran%202023-09-25%20%C3%A0%2008.45.24.png?raw=true)

# TP1 Summary

## Objective

- Create a Python application with Flask.
- Version control the code with GitHub.
- Deploy the application with Deta.
- Integrate Google Analytics for user tracking.
- Prepare a summary report.

## Achievements

### Python Application with Deta

- Registration/login to Deta.
- Deployment with Deta Micro.
- Access to the Deta dashboard.

### Version Control with GitHub

- Connection to GitHub.
- Creation of a GitHub repository.
- Git initialization.
- Creation of essential files (README, .gitignore, requirements.txt).

### Google Analytics

- Connection to Google Analytics.
- Creation of an account and property.
- Integration of Google Analytics tracking code.
- Installation testing.
- Viewing the Google Analytics dashboard.

### Report

- Creation of a PDF report including name, application URL, screenshot of the Google Analytics dashboard, and GitHub project URL.

## Additional Options

- Addition of a Google Analytics event button.
