from flask import Flask, request, jsonify
from deta import Deta


deta = Deta('myProjectKey') # configure your Deta project
app = Flask(__name__)