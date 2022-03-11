

from draw_candle_stick import *
from fetch_data import *
from draw_price_line import *


if __name__ == '__main__':
    # df = fetch_data()
    # draw_price_with_plotly(df)
    m5 = fetch_minute5_data()
    #draw_candle_with_mplfinance(m5)
    draw_candle_with_plotly(m5)

