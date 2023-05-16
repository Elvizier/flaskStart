
# Flask-Mailchimp Integration

This project is a simple Flask web application that offers a contact form for users to subscribe to a newsletter. It integrates with the Mailchimp API to automatically add subscribers to a Mailchimp audience.

The project is a demonstration of the following:

- Creating routes in a Flask application
- Rendering HTML templates
- Handling form data
- Making API requests

## Getting Started

To get started with the project, follow these steps:

1. **Clone the repository:**
```bash
git clone https://github.com/elvizier/flaskstart.git
```
2. **pip install -r requirements.txt**
```bash
pip install -r requirements.txt
```
3. **Set your Mailchimp API key and list ID as environment variables in a .env file:**
```bash
MAILCHIMP_API_KEY=your-api-key
MAILCHIMP_LIST_ID=your-list-id
```
4. **Run the application:**
```bash
python3 app.py
```

The application will be available at http://localhost:5000.

## Usage
Navigate to http://localhost:5000/subscribe to view the subscription form. Enter a name and an email address to subscribe to the newsletter. The application will make a POST request to the Mailchimp API to add the subscriber to your audience.

