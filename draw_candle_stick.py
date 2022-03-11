import mplfinance as mpf
import plotly.graph_objects as go


def draw_candle_with_mplfinance(minute5):
    color = mpf.make_marketcolors(up='red', down='green')
    # style = mpf.make_mpf_style(color=color)
    style = mpf.make_mpf_style(base_mpl_style="ggplot", marketcolors=color)
    mpf.plot(minute5, type='candle', style=style)


def draw_candle_with_plotly(minute5):
    candlestick = go.Candlestick(
        x=minute5.index,
        open=minute5['open'],
        high=minute5['high'],
        low=minute5['low'],
        close=minute5['close']
    )

    fig = go.Figure(data=[candlestick])

    fig.show()

    return
