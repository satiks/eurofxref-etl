# ECB Exchange Rates Viewer

A small Python application that downloads official exchange rate data
from the European Central Bank (ECB), calculates the average historical
rate for selected currencies, and generates a simple HTML page
displaying the results.

------------------------------------------------------------------------

## What the Program Does

When you run the application, it:

-   Downloads the latest daily exchange rates from the ECB
-   Downloads historical exchange rate data
-   Calculates the mean historical rate
-   Generates an HTML file with the results
-   Automatically opens the file in your default web browser

------------------------------------------------------------------------

## Project Structure

### main.py

Entry point of the application.
Connects all components together: fetching data, transforming it,
generating HTML, and opening the result in a browser.

### fetcher.py

Handles downloading ZIP files from the ECB website and extracting the
CSV content.

### transformer.py

Converts raw CSV data into structured Python objects and calculates the
mean historical rate for each supported currency.

### Currency.py

Simple data model that stores:
- Currency code 
- Current exchange rate 
- Mean historical exchange rate

### loader.py

Loads the HTML template, inserts currency rows, writes the final HTML
file, and returns the output path.

### exchange_rates_template.html

Base HTML template containing a `{{ROWS}}` placeholder that is
dynamically replaced with generated content.

### styles.css

Basic styling for table layout and formatting.

------------------------------------------------------------------------

## Requirements

-   Python 3.10 or newer
-   Internet connection
-   requests library

Install dependencies:

``` bash
pip install requests
```

------------------------------------------------------------------------

## How to Run

From the project root folder:

``` bash
py main.py
```

After running, the program will:

1.  Fetch data from the ECB
2.  Generate `exchange_rates.html`
3.  Open it automatically in your default web browser
