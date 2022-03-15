<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# Recieve and Download Images on incoming MMS Messages. Powered by Twilio - Python/Django

<!--
[![Build Status](https://travis-ci.org/TwilioDevEd/receive-mms-django.svg?branch=master)](https://travis-ci.org/TwilioDevEd/receive-mms-django)
-->

Use Twilio to receive SMS and MMS messages. For a step-by-step tutorial see
the [Twilio docs](https://www.twilio.com/docs/guides/receive-and-download-images-incoming-mms-messages-python-django).

## Note: protect your webhooks

Twilio supports HTTP Basic and Digest Authentication. Authentication allows you to password protect your TwiML URLs on your web server so that only you and Twilio can access them.

Learn more about HTTP authentication [here](https://www.twilio.com/docs/usage/security#http-authentication), which includes sample code you can use to secure your web application by validating incoming Twilio requests.

## Local development

This project is built using the [Django](https://www.djangoproject.com/) web
framework. It runs on Python 2.7+ and Python 3.4+.

To run the app locally:

1. Clone this repository and `cd` into it

   ```bash
   git clone git@github.com:TwilioDevEd/receive-mms-django.git
   cd receive-mms-django
   ```

1. Create a new virtual environment using
   [virtualenv](https://virtualenv.pypa.io/en/latest/)

   ```bash
   virtualenv -p python3 venv
   source venv/bin/activate
   ```

1. Install the requirements

   ```bash
   pip install -r requirements.txt
   ```

1. Copy the sample configuration file and edit it to match your configuration

   ```bash
   cp .env.example .env
   ```

   You can find your `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` in your
   [Twilio Account Settings](https://www.twilio.com/console).
   You will also need a `TWILIO_PHONE_NUMBER`, which you may find
   [here](https://www.twilio.com/console/phone-numbers/incoming).

   Note: To run using production environment use `cp .env.production.example .env` and follow
   previous steps


1. Load your environment configurations into your shell session

   ```bash
   source .env
   ```

1. Run the migrations

   ```bash
   python manage.py migrate
   ```

1. Run the application

   ```bash
   python manage.py runserver
   ```

1. Expose your application to the wider internet using
   [ngrok](http://ngrok.com/). This step is important because the
   application won't work as expected if you run it through localhost.

   ```bash
   ngrok http -host-header=localhost 8000
   ```

   Once ngrok is running, open up your browser and go to your ngrok URL.
   It will look something like this: `http://9a159ccf.ngrok.io`

   **Note:** You can read
   [this blog post](https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html)
   for more details on how to use ngrok.

1. Configure Twilio to call your webhooks

   You will also need to configure Twilio to call your application when calls
   are received on your TWILIO_NUMBER. The MMS url should look something
   like this:

   ```
   http://6b5f6b6d.ngrok.io/incoming/
   ```

   [Learn how to configure a Twilio phone number for Programmable Voice](https://www.twilio.com/docs/voice/quickstart/python#configure-your-webhook-url)


1. Check it out at http://localhost:8000

That's it

*Note:* To enable debug logs in local environment, set the `DEBUG` variable to `True` in the `developemt.py` file


## How to Demo

1. Send an MMS to your twilio number

1. Access http://localhost:8000. You should see a list with all the resources
   sent through your MMS

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
