from html import escape
from Currency import Currency

class ECBLoader:
    """
    Render exchange rate data into an HTML file using a template.
    """

    TEMPLATE_FILE = "exchange_rates_template.html"
    OUTPUT_FILE = "exchange_rates.html"

    def render(self, currencies: list[Currency]) -> str:
        """
        Render currency data into the HTML template and write to output file.

        The method:
        1. Reads the template file.
        2. Generates HTML rows for each Currency object.
        3. Replaces the {{ROWS}} placeholder.
        4. Writes the final HTML to disk.

        :param currencies: List of Currency objects to render.
        :type currencies: list[Currency]
        :returns: Path to the generated HTML output file.
        :rtype: str
        """

        with open(self.TEMPLATE_FILE, "r", encoding="utf-8") as file:
            template = file.read()

        rows_html = ""

        for cur in currencies:
            rate = "N/A" if cur.exchange_rate is None else f"{cur.exchange_rate}"
            mean = "N/A" if cur.mean_rate is None else f"{cur.mean_rate}"

            rows_html += f"""
            <div class="row">
                <div class="cell">{escape(cur.name)}</div>
                <div class="cell">{rate}</div>
                <div class="cell">{mean}</div>
            </div>
            """

        final_html = template.replace("{{ROWS}}", rows_html)

        with open(self.OUTPUT_FILE, "w", encoding="utf-8") as file:
            file.write(final_html)

        return self.OUTPUT_FILE