# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask
from flask import render_template
import json
import plotly
from fetch_data import *
from draw_candle_stick import *
import plotly.express as px


def fetch_data():
    df = pd.read_csv("time_price.csv")
    print(df)
    return df


app = Flask('stick')


@app.route("/")
@app.route("/price")
def price_line():
    df = fetch_data()
    line = px.line(df,
                   x='time',
                   y='price',
                   )
    data = line
    line_json = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('price.html', line_json=line_json)


@app.route("/candle_stick")
def candle_stick_minutes():
    minute5 = fetch_minute5_data()
    candlestick = go.Candlestick(
        #x=minute5.index,
        open=minute5['open'],
        high=minute5['high'],
        low=minute5['low'],
        close=minute5['close']
    )

    data = [candlestick]
    candle_json = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('candle_stick.html',
                           candle_json=candle_json)


if __name__ == '__main__':
    app.run(debug=True)
