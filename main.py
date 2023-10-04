from flask import Flask, request, render_template
import logging
from logging.config import dictConfig
import requests
import json

app = Flask(__name__, template_folder='templatesTP')

@app.route("/")
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
            req = requests.get("https://www.google.com/")
            # Get the cookies in cookies.html
            cookies = req.cookies
            # Return the cookies
            return render_template('cookies.html', cookies=cookies)
        except:
            return "Error"
         
    return render_template('cookies.html')
