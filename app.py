from flask import Flask,render_template,request,make_response
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"La URL /data no se puede acceder de forma directa. Pruebe yendo por '/' para completar el formulario"
    if request.method == 'POST':
        url = request.form['url']
        selector = request.form['selector']
        r = requests.get(url)
        data = r.content
        try:
            soup = BeautifulSoup(data,"lxml")
            filter = soup.select(selector)
            response = make_response(str(filter),200)
            response.mimetype = "text/plain"
        except Exception:
            response = "URL o Selector incorrecto, vuelva atrás para intentarlo nuevamente..."
        return response

app.run(host='localhost', port=5000)