import dash
from dash import Dash, html
import dash_mantine_components as dmc

# dash.register_page(__name__) tells Dash that this is a page in your app.
dash.register_page(
    __name__,
)


#layout
layout = html.Div([
    html.H1("Hello, I'm Page1!"),
    html.P("This is the first page of the app."),
    dmc.Anchor(dmc.Button("Go to Page2"),href='/page2'),
    html.Button("Go to Home", id='home-button')
])