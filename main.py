import webbrowser
from transformer import ECBFTransformer
from loader import ECBLoader

"""
Application entry point for generating and displaying ECB exchange rates.

Workflow:
1. Fetch and transform ECB exchange rate data.
2. Render the data into an HTML file.
3. Open the generated HTML file in the default web browser.
"""

if __name__ == "__main__":
    transformer = ECBFTransformer()
    currencies = transformer.get_currencies_data()

    loader = ECBLoader()
    output_path = loader.render(currencies)

    webbrowser.open(output_path)
