# dash-multipage-seo-friendly

An approach for getting the page source on the client side to be SEO friendly for crawlers.

## Features

- **Custom Page Routing**: The application uses the Flask request object to determine the current URL and generate the appropriate page layout and title.
- **SEO-friendly Layouts**: The application uses the `dashseo.convert_to_html` function to convert Dash layouts into HTML for improved SEO.
- **Customizable Meta Tags**: The application allows for customizable meta tags for each page.

## Installation

To install the necessary dependencies for this project, run the following command:
`pip install dash dashseo flask dash_mantine_components`



## Usage

To start the server, run the following command:

python main.py


The server will start in debug mode.

## Adding New Pages

To add a new page to the application:

1. Create a new layout in the `pages` directory.
2. Import the layout in the `CustomDash.interpolate_index` method.
3. Add the page path and title to the `page_titles` dictionary.
4. Add the page path and layout to the `page_layouts` dictionary.


## Contributing

Contributions are welcome. Please open an issue to discuss your idea or submit a pull request.


## Current issues
With Dash Mantine Components library the convert to html function struggles to generate the HTML.