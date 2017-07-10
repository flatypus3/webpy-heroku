# coding: utf-8
import os
import web

from crust import sslify
from whitenoise import WhiteNoise

urls = (
    "/", "index",
)

app = web.application(urls, globals())

# use SSL
if 'DYNO' in os.environ:
    sslify.sslify(app)


class index:
    def GET(self):
        return """<html>
                    <body>
                      <img src="static/images/success.jpg"/>
                    </body>
                  </html>"""


# Adds a wsgi callable for uwsgi
application = app.wsgifunc()
application = WhiteNoise(application, root="static/", prefix="static/")

if __name__ == "__main__":
    app.run()
