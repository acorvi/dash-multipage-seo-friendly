import dash
from dash import Dash, html
import dash_mantine_components as dmc

# dash.register_page(__name__) tells Dash that this is a page in your app.
dash.register_page(
    __name__,
)


#layout
layout = html.Div([
    html.H1("Hello, I'm Page3 and this time in my page source you will find everything!"),
    dmc.Accordion(
    children=[
        dmc.AccordionItem(
            [
                dmc.AccordionControl("Customization"),
                dmc.AccordionPanel(
                    "Colors, fonts, shadows and many other parts are customizable to fit your design needs"
                ),
            ],
            value="customization",
        ),
        dmc.AccordionItem(
            [
                dmc.AccordionControl("Flexibility"),
                dmc.AccordionPanel(
                    "Configure temp appearance and behavior with vast amount of settings or overwrite any part of "
                    "component styles "
                ),
            ],
            value="flexibility",
        ),
    ],
),
    dmc.Anchor(dmc.Button("Go to Homepage"),href='/'),
])