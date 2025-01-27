#################################################################################################################
#Date Created: 08/03/2022
#Authors: Dominic Williams (University of Bath)
#Purpose: This code creates the coffee question
#Images: beer_black.png
#################################################################################################################


from dash import dcc, html
import dash_bootstrap_components as dbc

# App layout
card_content = [
    dbc.CardHeader(
        html.Div([
            html.H5(['How many coffees do you drink a week?'], style={'display': 'inline-block'}),
            html.Div([
                html.I(className="fa fa-info-circle")
            ], style={'display': 'inline-block',
                      'margin-left': '10px'},
                id='question-3'),
            dbc.Tooltip(
                html.Div(["Coffee contains naturally occurring radioactive nuclides from the soil coffee plants are grown in.", html.Br(),
                          "When you drink a coffee you ingest a tiny amount of radiation.", html.Br(),
                          "Effective Dose: 0.00001 mSv (approx. one coffee).", html.Br(),html.Br(),
                          html.I("(This is the same eating 1/9th of a banana)"),
                          ]),
                target='question-3',
                placement='right'
                )
        ])
    ),

    dbc.CardBody(
        [
            dbc.Row([
                dbc.Col([
                    html.Div([
                        dcc.Dropdown(id='Q-3a-ddown',
                                     options=[
                                         {"label": value, "value": value} for value in range(50)])
                    ]),
                ], width=12),
            ])

        ]
    )
]

coffee_image = html.Div([
    html.Img(id="coffee-logo",
             src='/assets/coffee_black.png',
             height=100,
             width=100,
             style={'align-items': 'center'})
])

def get_question3(app):
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
                coffee_image
            ], width=3),

            dbc.Col([
                html.I('')
            ], width=1)
        ]),
    )

    return layout