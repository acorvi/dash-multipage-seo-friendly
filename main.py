from dash import html,Dash, dcc, Input, Output, State, clientside_callback
from urllib.parse import urlparse, urlunparse
from dashseo.convert_to_html import convert_to_html
from flask import request
import dash_mantine_components as dmc
import dash

### CUSTOM TEMPLATE

class CustomDash(Dash):
    def interpolate_index(self, **kwargs):
        from pages.page1 import layout as layout_page1
        from pages.page2 import layout as layout_page2
        from pages.page0 import layout as layout_home

        # Get the current URL from the Flask request object
        current_url = urlparse(request.url)

        # Dictionary that maps page paths to titles
        page_titles = {
            '/': "Home Page",
            '/page1': "Page 1",
            '/page2': "Page 2",
            # Add more pages here
        }

        # Dictionary that maps page paths to layouts
        page_layouts = {
            '/': layout_home,
            '/page1': layout_page1,
            '/page2': layout_page2,
            # Add more pages here
        }


        # Get the title for the current page, or use a default title if the page is not in the dictionary
        title = page_titles.get(current_url.path, 'Default Title')

        # Get the layout for the current page, or use a default layout if the page is not in the dictionary
        layout_seo = page_layouts.get(current_url.path, html.Div())

        # print(layout_seo)

        # Override the title in the kwargs dictionary
        kwargs['title'] = title


        ### THIS IS WHERE I'M STUCK #### UNCOMMENT THIS TO SEE THE ERROR
        
        # Get the layout for the current page
        layout_html = convert_to_html(layout_seo)

        print(layout_html)

        # Include the layout HTML in the kwargs dictionary
        kwargs['layout'] = layout_html

        return '''
        <!DOCTYPE html>
        <html>
            <head>
                {metas}
                <title>{title}</title>
                {favicon}
                {css}
            </head>
            <body>
                <div id="react-entry-point">
                    <div class="_dash-loading">
                        {layout}
                    </div>
                </div>
                <footer>
                    {config}
                    {scripts}
                    {renderer}
                </footer>
            </body>
        </html>
        '''.format(
            metas=kwargs['metas'],
            title=kwargs['title'],
            favicon=kwargs['favicon'],
            css=kwargs['css'],
            layout=kwargs['layout'],
            config=kwargs['config'],
            scripts=kwargs['scripts'],
            renderer=kwargs['renderer'],
        )


#### APP DEFINITION ####
app = CustomDash(__name__, 
use_pages=True,
suppress_callback_exceptions=True,
include_pages_meta=True,
compress=True,
update_title=None,
meta_tags=[
        {
            "name": "favicon",
            "rel": "icon",
            "href": "/assets/favicon.ico",  # Replace with the path to your favicon
            "type": "image/x-icon",
        },
        {
            "http-equiv": "Content-Language",
            "content": "en",
        },
        
    ],)


app.layout = html.Div(
    children=[
            dmc.Container([
                dcc.Location(id='url', refresh=False),
                dash.page_container, #this is instead of the loading page
            ]),
    ]
    
)


# Running the server
server = app.server #This is for deployment
#This is a common Python idiom used to ensure that the script's code is run only when the script is run directly, not when it is imported as a module.
if __name__ == '__main__':
    app.run_server(debug=True)