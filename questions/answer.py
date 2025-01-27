#################################################################################################################
#Date Created: 08/03/2022
#Authors: Dominic Williams (University of Bath)
#Purpose: DO I NEED THIS??
#################################################################################################################


from dash import dcc, html
import dash_bootstrap_components as dbc

# App layout
card_content = [
    dbc.CardHeader(
        html.Div([
            html.H5(['Total Radiation'], style={'display': 'inline-block'}),
            html.Div([
                html.I(className="fa fa-info-circle")
            ], style={'display': 'inline-block',
                      'margin-left': '10px'},
                id='answer'),
            #dbc.Tooltip(
            #    html.Div([
            #        "", html.Br(),
            #        "", html.Br(), html.Br(),
            #        ""
            #              ]),
            #    target='answer',
            #    placement='right'
            #    )
        ])
    ),

    dbc.CardBody(
        [
            dbc.Row([
                html.Div([
                    html.H4('Total Radiation Dose'),

                ]),
            ]),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H5(' 2.3 mSv'),

                    ], style={"width": "50%"}),
                ], width=12),
            ])

        ]
    )
]

#banana_image = html.Div([
#    html.Img(id="no_logo",
#             #src='/assets/banana_black.png',
#             height=100,
#             width=100,
#             style={'align-items': 'center'})
#])

def get_answer(app):
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
                html.I('')
                #banana_image
            ], width=3),

            dbc.Col([
                html.I('')
            ], width=1)
        ]),
    )

    return layout