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
            '/page3': 'Page 3',
            # Add more pages here
        }

        #for layout of page 3 I do manual insertion so that each component is listed in the html
        layout_page3_simplified= '''
        <main id="_pages_content">
            <h1>Hello, I'm Page3 and this time in my page source you will find everything!</h1>
            <section>
                <h2>Customization</h2>
                <p>Colors, fonts, shadows and many other parts are customizable to fit your design needs</p>
            </section>
            <section>
                <h2>Flexibility</h2>
                <p>Configure temp appearance and behavior with vast amount of settings or overwrite any part of component styles</p>
            </section>
            <a href="/">Go to Homepage</a>
        </main>
        '''
        layout_page3= '''
        <div id="_pages_content"><div><h1>Hello, I'm Page3 and this time in my page source you will find everything!</h1><div class="mantine-1avyp1d" loading_state="[object Object]" data-accordion="true"><div class="mantine-Accordion-item mantine-v4lv9f" loading_state="[object Object]"><button class="mantine-UnstyledButton-root mantine-Accordion-control mantine-xizyzk" type="button" loading_state="[object Object]" data-accordion-control="true" aria-expanded="false" aria-controls="mantine-qvox5cid3-panel-customization" id="mantine-qvox5cid3-control-customization"><div class="mantine-1h6pkea mantine-Accordion-chevron"><svg viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg" width="16" height="16"><path d="M3.13523 6.15803C3.3241 5.95657 3.64052 5.94637 3.84197 6.13523L7.5 9.56464L11.158 6.13523C11.3595 5.94637 11.6759 5.95657 11.8648 6.15803C12.0536 6.35949 12.0434 6.67591 11.842 6.86477L7.84197 10.6148C7.64964 10.7951 7.35036 10.7951 7.15803 10.6148L3.15803 6.86477C2.95657 6.67591 2.94637 6.35949 3.13523 6.15803Z" fill="currentColor" fill-rule="evenodd" clip-rule="evenodd"></path></svg></div><div class="mantine-pildck mantine-Accordion-label">Customization</div></button><div class="mantine-Accordion-panel mantine-1supnlp" aria-hidden="true" loading_state="[object Object]" role="region" id="mantine-qvox5cid3-panel-customization" aria-labelledby="mantine-qvox5cid3-control-customization" style="box-sizing: border-box; height: 0px; overflow: hidden; display: none;"><div style="opacity: 0; transition: opacity 200ms ease 0s;"><div class="mantine-ukbbnm mantine-Accordion-content">Colors, fonts, shadows and many other parts are customizable to fit your design needs</div></div></div></div><div class="mantine-Accordion-item mantine-v4lv9f" loading_state="[object Object]"><button class="mantine-UnstyledButton-root mantine-Accordion-control mantine-xizyzk" type="button" loading_state="[object Object]" data-accordion-control="true" aria-expanded="false" aria-controls="mantine-qvox5cid3-panel-flexibility" id="mantine-qvox5cid3-control-flexibility"><div class="mantine-1h6pkea mantine-Accordion-chevron"><svg viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg" width="16" height="16"><path d="M3.13523 6.15803C3.3241 5.95657 3.64052 5.94637 3.84197 6.13523L7.5 9.56464L11.158 6.13523C11.3595 5.94637 11.6759 5.95657 11.8648 6.15803C12.0536 6.35949 12.0434 6.67591 11.842 6.86477L7.84197 10.6148C7.64964 10.7951 7.35036 10.7951 7.15803 10.6148L3.15803 6.86477C2.95657 6.67591 2.94637 6.35949 3.13523 6.15803Z" fill="currentColor" fill-rule="evenodd" clip-rule="evenodd"></path></svg></div><div class="mantine-pildck mantine-Accordion-label">Flexibility</div></button><div class="mantine-Accordion-panel mantine-1supnlp" aria-hidden="true" loading_state="[object Object]" role="region" id="mantine-qvox5cid3-panel-flexibility" aria-labelledby="mantine-qvox5cid3-control-flexibility" style="box-sizing: border-box; height: 0px; overflow: hidden; display: none;"><div style="opacity: 0; transition: opacity 200ms ease 0s;"><div class="mantine-ukbbnm mantine-Accordion-content">Configure temp appearance and behavior with vast amount of settings or overwrite any part of component styles </div></div></div></div></div><a class="mantine-Text-root mantine-Anchor-root mantine-1ut1du9" href="/" loading_state="[object Object]"><button class="mantine-UnstyledButton-root mantine-Button-root mantine-8nr514" type="button" data-button="true" loading_state="[object Object]"><div class="mantine-3xbgk5 mantine-Button-inner"><span class="mantine-qo1k2 mantine-Button-label">Go to Homepage</span></div></button></a></div></div>
        '''

        # Dictionary that maps page paths to layouts
        page_layouts = {
            '/': layout_home,
            '/page1': layout_page1,
            '/page2': layout_page2,
            '/page3': layout_page3_simplified,
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