#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '''
<html>
    <head><title>Hello world!</title></head>
    <body>page content</body>
</html>
'''

if __name__ == '__main__':
    app.run()
