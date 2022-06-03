from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd


app = Flask(__name__,
        template_folder="./templates")


@app.route("/", methods=['POST', 'GET'])
def index():

    data = yf.download("DJIA")
    print(data)
    data.index = data.index.astype(str)
    data = data['Close']
    dates = data.index
    title = "Dow Jones Industrial Average"


    if request.method == "POST":
        ticker = request.form['stock_ticker']

        data = yf.download(ticker)
        print(data)
        data.index = data.index.astype(str)
        data = data['Close']
        dates = data.index
        
        return render_template("index.html", data=data, dates=dates, title=ticker)

    return render_template("index.html", data=data, dates=dates, title=title)


if __name__=="__main__":
    app.run(debug=True)