import plotly.graph_objs as go


def plotly_slider(df, column, title):

    trace = go.Scatter(x=list(df.index),
                       y=list(df[column]))

    data = [trace]
    layout = dict(title=title,
                  xaxis=dict(
                      rangeselector=dict(
                          buttons=list([
                              dict(count=1,
                                   label='1m',
                                   step='month',
                                   stepmode='backward'),
                              dict(count=6,
                                   label='6m',
                                   step='month',
                                   stepmode='backward'),
                              dict(count=1,
                                   label='YTD',
                                   step='year',
                                   stepmode='todate'),
                              dict(count=1,
                                   label='1y',
                                   step='year',
                                   stepmode='backward'),
                              dict(step='all')
                          ])
                      ),
                      rangeslider=dict(
                          visible=True
                      ),
                      type='date'
                  ))

    fig = dict(data=data, layout=layout)
    return fig
