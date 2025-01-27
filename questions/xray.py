#################################################################################################################
#Date Created: 08/03/2022
#Authors: Dominic Williams (University of Bath)
#Purpose: This code creates the x-ray question
#Images: xray_black.png

#################################################################################################################


from dash import dcc, html
import dash_bootstrap_components as dbc

# App layout
card_content = [
    dbc.CardHeader(
        html.Div([
            html.H5(['How many x-rays have you had this year?'], style={'display': 'inline-block'}),
            html.Div([
                html.I(className="fa fa-info-circle")
            ], style={'display': 'inline-block',
                      'margin-left': '10px'},
                id='question-1'),
            dbc.Tooltip(
                html.Div(["X-rays subject the patient to small amount of x-ray radiation.", html.Br(),
                          "X-rays are useful because they can penetrate through the body, allowing doctors to see organs and bones", html.Br(),
                          "Effective Dose: 0.005 mSv (dental x-ray) and 0.001 mSv (wrist x-ray)", html.Br(), html.Br(),
                          html.I("(This is the same dose as eating 50 and 10 bananas)"),
                          ]),
                target='question-1',
                placement='right'
                )
        ])
    ),

    dbc.CardBody(
        [
            dbc.Row([

                dbc.Col([
                    html.Div([
                        html.I('Dental X-Ray'),
                        dcc.Dropdown(
                            id='Q-1a-ddown',
                            options=[
                                {"label": value, "value": value} for value in range(6)])
                    ])
                ], width=12)]),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.I('Wrist X-Ray'),
                        dcc.Dropdown(id='Q-1b-ddown',
                                     options=[
                                         {"label": value, "value": value} for value in range(5)])
                    ])
                ], width=12)
            ])

        ]
    )
]

xray_image = html.Div([
    html.Img(id="xray-logo",
             src='/assets/xray_black.png',
             height=100,
             width=100,
             style={'align-items': 'center'})

])

pplant_image = html.Div([
    html.Img(id="pplant-logo",
             src='/assets/pplant_black.png',
             height=100,
             width=100,
             style={'align-items': 'center'})
])


def get_question1(app):
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
                xray_image
            ], width=3),

            dbc.Col([
                html.I('')
            ], width=1)
        ]),
    )

    return layout