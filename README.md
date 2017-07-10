# webpy-heroku
Sample App of Web.py running on Heroku

## Background

Heroku's Python documention is a great resource for running Python applications on Heroku, however it does not include examples for web.py. The webpy-heroku code base contains a very minimalistic web.py application that can be used as a starting point for running web.py apps on Heroku. The sample app displays an image from the static/images directory over SSL via gunicorn. These are the three major differences of running a web.py application on a platform as a service like Heroku vs a server/VM. 

## Notes
* Assuming Python 2.7
* Assuming Heroku toolbelt is installed and Heoroku Python documentation has been read
* Gunicorn - Python WSGI server
* webpy-crust - Provides a wrapper for handling Heroku's SSL/TLS traffic 
* WhiteNoise - Adds support to WSGI for serving static assets

## Setup
    pip install -r requirements.txt

## Running Locally
    gunicorn sample.app
    
or using the development server

    python sample/app.py

## Running on Heroku

    heroku create    
    # Gunicorn Concurrency
    heroku config:set WEB_CONCURRENCY=3
    git push heroku master
