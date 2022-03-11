import plotly.express as px


def draw_price_with_plotly(df):
    line = px.line(df,
                   x='time',
                   y='price',
                   )
    line.show()
    return
