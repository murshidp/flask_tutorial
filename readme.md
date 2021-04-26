### getting started

* seting environmental variable
    * export FLASK_APP=main.py 
    * export FLASK_DEBUG=1


### 2. Templates
 * to render template: from flask import render_template
 * to use url : from flask import url_for
 * using url in html :
    *   link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='main.css') }}"
