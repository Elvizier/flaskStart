# Import flask module that allows you to create a new application
from flask import Flask, request, render_template
import requests, json, os
from dotenv import load_dotenv

load_dotenv()
MAILCHIMP_API_KEY = os.getenv("MAILCHIMP_API_KEY")
MAILCHIMP_LIST_ID = os.getenv("MAILCHIMP_LIST_ID")

# Create a new web application
app = Flask(__name__)

# Create route for the root URL
@app.route('/')
def hello_world():
    return render_template('index.html')

# Create route for contact page, I used required in HTML to handle all errors
@app.route('/subscribe', methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        data = {
            "email_address": email,
            "status": "subscribed",
            "merge_fields": {
                "FNAME": name
            }
        }
        # Send a POST request to the MailChimp API and 
        # write in TXT file(NB- testing. Can be removed for better security)
        with open ('contact.txt', 'a') as f:
            f.write(f"['{name}','{email}']\n")
        response = requests.post(
            f'https://us13.api.mailchimp.com/3.0/lists/{MAILCHIMP_LIST_ID}/members/',
            auth=('anystring', MAILCHIMP_API_KEY),
            data=json.dumps(data)
        )
        if response.status_code == 200:
            return f"Welcome to our newsletter, {name}. {email} has been registered and be on the look for our exciting discoveries"
        else:
            return f"An error occurred: {response.text}"

    else:
        return render_template('subscribe.html')




if __name__ == '__main__':
    app.run(debug=True)


