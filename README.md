# TP1DataSource

Thibault Gillard

## TP2 Results

![yes](https://github.com/Thibault-GILLARD/TP1DataSource/blob/master/source/Video%20to%20GIF%202023-10-14%2016.33.20.gif?raw=true)

For the TP2 the stategie was to do the different tasks in different roots and when everything was working to merge them all together into the main root, with some css to make it look better.

First was to Manipulate cookies:
    
    ```python   
    

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
