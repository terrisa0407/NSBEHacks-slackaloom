#http://localhost:8000/
from flask import Flask
from slackaloom import slackaloom

social = Flask(__name__)
social.register_blueprint(slackaloom, url_prefix = '/slackaloom')

# 1st page for Social 


if __name__ == '__main__':
    social.run(debug = True, port= 8000)
