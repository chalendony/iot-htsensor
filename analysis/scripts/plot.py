import plotly.graph_objs as go


# def plotly_slider(df, column, title):
#
#     trace = go.Scatter(x=list(df.index),
#                        y=list(df[column]))
#
#     data = [trace]
#     layout = dict(title=title,
#                   xaxis=dict(
#                       rangeselector=dict(
#                           buttons=list([
#                               dict(count=1,
#                                    label='1m',
#                                    step='month',
#                                    stepmode='backward'),
#                               dict(count=6,
#                                    label='6m',
#                                    step='month',
#                                    stepmode='backward'),
#                               dict(count=1,
#                                    label='YTD',
#                                    step='year',
#                                    stepmode='todate'),
#                               dict(count=1,
#                                    label='1y',
#                                    step='year',
#                                    stepmode='backward'),
#                               dict(step='all')
#                           ])
#                       ),
#                       rangeslider=dict(
#                           visible=True
#                       ),
#                       type='date'
#                   ))
#
#     fig = dict(data=data, layout=layout)
#     return fig


def slider_plotly(df, title):

    trace_temp = go.Scatter(x=list(df.index),
                            y=list(df.Temp),
                            name='Temperature',
                            line=dict(color='#3FA65F'))

    # set the initial graph
    data = [trace_temp]

    # when drop down changes:  get new values for y then update the graph
    updatemenus = list([
        dict(
            buttons=list([
                dict(label='Temperature',
                     method='update',
                     args=[{'y': [df.Temp]},
                           {'title': 'Temperature ' + title}]),

                dict(label='Humidity',
                     method='update',
                     args=[{'y': [df.Humi]},
                           {'title': 'Humidity ' + title}])
            ]),
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            xanchor='left',
            yanchor='top'
        )
    ])

    # Place widgets on screen
    layout = dict(updatemenus=updatemenus,
                  title=title,
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
                  )
                  )

    fig = dict(data=data, layout=layout)
    return fig
