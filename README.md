# Auth-web-APP




# Flask App with Twitter OAuth 2.0 using Authomatic

This project is a simple Flask web application that demonstrates how to implement Twitter OAuth 2.0 authentication using the [Authomatic](https://authomatic.github.io/) library. The app allows users to log in with their Twitter account and displays their basic profile information upon successful authentication.

---

## Features

- **OAuth 2.0 Authentication**: Securely authenticate users via Twitter.
- **Authomatic Integration**: Simplifies the OAuth flow with minimal setup.
- **User-Friendly**: Displays user profile information (e.g., name, username) after login.

---

## Prerequisites

Before running this app, ensure you have the following:

1. **Python**: Version 3.7 or higher installed on your system.
2. **Twitter Developer Account**: Create an app in the [Twitter Developer Portal](https://developer.twitter.com/) to obtain your API key and secret.
3. **Flask**: Installed in your Python environment.
4. **Authomatic Library**: Installed via pip.

---

## Installation

Follow these steps to set up and run the project:

### 1. Clone the Repository

```bash
git clone https://github.com/boss6825/flask-twitter-oauth.git
cd flask-twitter-oauth
```


### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```


### 3. Install Dependencies

```bash
pip install -r requirements.txt
```


### 4. Set Up Environment Variables

Create a `.env` file in the project directory and add the following variables:

```plaintext
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_flask_secret_key
```

Replace `your_twitter_api_key`, `your_twitter_api_secret`, and `your_flask_secret_key` with your actual credentials.

### 5. Run the Application

Start the Flask development server:

```bash
flask run
```

The app will be accessible at `http://127.0.0.1:5000`.

---

## Usage

1. Open your browser and navigate to `http://127.0.0.1:5000`.
2. Click the "Login with Twitter" button.
3. Authorize the app using your Twitter account.
4. After successful login, you will see your Twitter profile information displayed on the screen.

---

## Project Structure

Here’s an overview of the project structure:

```
flask-twitter-oauth/
│
├── app.py                # Main application file
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not included in repo)
├── templates/
│   └── index.html        # HTML template for the home page
└── README.md             # Project documentation (this file)
```

---

## Dependencies

The following Python libraries are used in this project:

- **Flask**: Web framework for building the app.
- **Authomatic**: Handles OAuth authentication flows.
- **python-dotenv**: Loads environment variables from a `.env` file.

Install them using:

```bash
pip install flask authomatic python-dotenv
```

---

## Troubleshooting

### Common Issues and Fixes

1. **Invalid API Key or Secret**:
    - Ensure you’ve entered the correct values in the `.env` file.
    - Verify your credentials in the [Twitter Developer Portal](https://developer.twitter.com/).
2. **Callback URL Mismatch**:
    - Make sure you’ve added `http://127.0.0.1:5000/callback/twitter` as a valid callback URL in your Twitter app settings.
3. **Module Not Found**:
    - Run `pip install -r requirements.txt` to ensure all dependencies are installed.
4. **CSRF Token Error**:
    - Add a random secure value for `SECRET_KEY` in your `.env` file.

---

## Contributing

Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## Contact

If you have any questions or need further assistance, feel free to contact me:

- GitHub: [boss6825](https://github.com/boss6825)
- Email: [arpitsolanki6825@gmail.com](mailto:arpitsolanki6825@gmail.com)

---

Let me know if you’d like me to expand on any section or add more details!

