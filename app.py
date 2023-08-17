from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.form['city']:
        url = "https://api.openweathermap.org/data/2.5/forecast?appid=a5b75526f326f806655d10545752ae30&q=" + \
            request.form['city']
        giphy = requests.get(url)
        dataGiphy = giphy.json()
        return render_template('index.html', weather=dataGiphy)
    else:
        return render_template('index.html')

def pagina_no_encontrada(error):
    return render_template('404.html'), 404


app.register_error_handler(404, pagina_no_encontrada)

if __name__ == "__main__":
    app.run(debug=True)
