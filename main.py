import flask
import os
from supabase import create_client, Client

url: str = "https://gzmpxnzxklmvrnbchcra.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd6bXB4bnp4a2xtdnJuYmNoY3JhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDQ5MTE3OTcsImV4cCI6MjAyMDQ4Nzc5N30.oFrBquw8pe1wWEHS9uggSykkuW8-LsNdSt7bJvrBvXk"
supabase: Client = create_client(url, key)

app = flask.Flask(__name__)



@app.route('/')
def index():
    return flask.render_template('index.html')

