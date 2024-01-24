import dash
from dash import Dash, html
import dash_mantine_components as dmc

# dash.register_page(__name__) tells Dash that this is a page in your app.
dash.register_page(
    __name__,
    path='/' #this is the default page
)


#layout
layout = html.Div([
    html.H1("Hello, I'm the Homepage, aka Page0!"),
    dmc.Anchor(dmc.Button("Go to Page1"),href='/page1'),
])