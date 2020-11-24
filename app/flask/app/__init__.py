from flask import Flask
from app import instagram_bot

app = Flask(__name__)

from app import bot_api
