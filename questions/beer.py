#################################################################################################################
#Date Created: 08/03/20222
#Authors: Dominic Williams (University of Bath)
#Purpose: This code creates the beer question
#Images: beer_black.png
#################################################################################################################


from dash import dcc, html
import dash_bootstrap_components as dbc

# App layout
card_content = [
    dbc.CardHeader(
        html.Div([
            html.H5(['How many beers do you drink a week?'], style={'display': 'inline-block'}),
            html.Div([
                html.I(className="fa fa-info-circle")
            ], style={'display': 'inline-block',
                      'margin-left': '10px'},
                id='question-5'),
            dbc.Tooltip(
                html.Div([
                    "Beer contains a very small amount of radioactive nuclides sourced from the water used to produce beer."
                    ,html.Br(),"Drinking beer subjects you to a tiny amount radation."
                    ,html.Br(), "Effective Dose: 0.000003 mSv (per pint)"
                    ,html.Br(),html.Br(), html.I("(This is the same as eating 1/29th bananas)"),
                          ]),
                target='question-5',
                placement='right'
                )
        ])
    ),

    dbc.CardBody(
        [
            dbc.Row([
                dbc.Col([
                    html.Div([
                        dcc.Dropdown(id='Q-5a-ddown',
                                     options=[
                                         {"label": value, "value": value} for value in range(21)])
                    ]),
                ], width=12),
            ])

        ]
    )
]

beer_image = html.Div([
    html.Img(id="beer-logo",
             src='/assets/beer_black.png',
             height=100,
             width=100,
             style={'align-items': 'center'})
])

def get_question5(app):
    layout = html.Div(
        dbc.Row([

            #Margin 1
            dbc.Col([
                html.I('')
            ], width=1),

            dbc.Col([
                dbc.Card(card_content, color="warning", outline=True)
            ], width=6),

            dbc.Col([
                html.I('')
            ], width=1),

            dbc.Col([
                beer_image
            ], width=3),

            dbc.Col([
                html.I('')
            ], width=1)
        ]),
    )

    return layout