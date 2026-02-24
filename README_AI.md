add minimal error handling using raise

    from io import BytesIO
    from zipfile import ZipFile
    from requests import get

    class ECBFetcher:
    """
    Class to fetch and extract ECB (European Central Bank) exchange rate data.
    Provides methods to get daily and historical rates from ECB ZIP files.
    """

    DAILY_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip"
    HIST_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip"

    def __download_and_extract(self, url: str) -> str:
        """
        Download and extract ECB exchange rates from a ZIP file.

        Args:
            url (str): URL of the ZIP file to download.

        Returns:
            str: CSV content of the exchange rates.
        """
        response = get(url, timeout=10)
        response.raise_for_status()

        with ZipFile(BytesIO(response.content)) as z:
            with z.open(z.namelist()[0]) as f:
                return f.read().decode("utf-8")

    def fetch_daily_ecb(self) -> str:
        """Fetch the daily ECB exchange rate data."""
        return self.__download_and_extract(self.DAILY_URL)

    def fetch_historical_ecb(self) -> str:
        """Fetch the historical ECB exchange rate data."""
        return self.__download_and_extract(self.HIST_URL)

Here’s a minimal adjustment to your class that adds basic error handling with raise statements, keeping it simple and Pythonic:

    from io import BytesIO
    from zipfile import ZipFile, BadZipFile
    from requests import get, RequestException
    
    class ECBFetcher:

    DAILY_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip"
    HIST_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip"

    def __download_and_extract(self, url: str) -> str:
        """
        Download and extract ECB exchange rates from a ZIP file.
        Raises an exception on network or extraction failure.
        """
        try:
            response = get(url, timeout=10)
            response.raise_for_status()
        except RequestException as e:
            raise RuntimeError(f"Failed to download data from {url}") from e

        try:
            with ZipFile(BytesIO(response.content)) as z:
                with z.open(z.namelist()[0]) as f:
                    return f.read().decode("utf-8")
        except (BadZipFile, KeyError, OSError) as e:
            raise RuntimeError(f"Failed to extract ZIP content from {url}") from e

    def fetch_daily_ecb(self) -> str:
        """Fetch the daily ECB exchange rate data."""
        return self.__download_and_extract(self.DAILY_URL)

    def fetch_historical_ecb(self) -> str:
        """Fetch the historical ECB exchange rate data."""
        return self.__download_and_extract(self.HIST_URL)

What changed:

Wrapped the HTTP request in try/except and raise a RuntimeError on failure.

Wrapped the ZIP extraction in try/except for BadZipFile, KeyError, or OSError.

Uses raise ... from e to preserve the original exception traceback.

This keeps the class interface the same but gives clear errors if something goes wrong.

If you want, I can also make it fail gracefully with default return values instead of crashing. Do you want that version too?


Generate simple css for html page

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Exchange Rates</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
    
    <h2>ECB Euro Reference Exchange Rates</h2>
    
    <div class="table">
        <div class="row header">
            <div class="cell">Currency Code</div>
            <div class="cell">Rate (Today)</div>
            <div class="cell">Mean Historical Rate</div>
        </div>
    
            <div class="row">
                <div class="cell">USD</div>
                <div class="cell">1.1777</div>
                <div class="cell">1.1823</div>
            </div>
            
            <div class="row">
                <div class="cell">SEK</div>
                <div class="cell">10.688</div>
                <div class="cell">9.6903</div>
            </div>
            
            <div class="row">
                <div class="cell">GBP</div>
                <div class="cell">0.8731</div>
                <div class="cell">0.7849</div>
            </div>
            
            <div class="row">
                <div class="cell">JPY</div>
                <div class="cell">183.53</div>
                <div class="cell">131.6722</div>
            </div>
            
    </div>
    
    </body>
    </html>

Here’s a clean styles.css that matches your HTML structure

    /* styles.css*/
    
    /* 1) Basic page styles */
    body {
      margin: 0;
      padding: 40px 16px;
      font-family: Arial, sans-serif;
      background: #f6f7fb;   /* light gray background */
      color: #222;           /* dark text */
    }
    
    /* Title */
    h2 {
      margin: 0 auto 8px;
      max-width: 900px;
    }
    
    /* 2) The main table container */
    .table {
      max-width: 900px;
      margin: 16px auto 0;        /* center it */
      background: #fff;           /* white card */
      border: 1px solid #ddd;     /* light border */
      border-radius: 10px;
      overflow: hidden;           /* keeps rounded corners clean */
    }
    
    /* 3) Each row is a grid with 3 columns */
    .row {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr; /* three equal columns */
    }
    
    /* Header row */
    .row.header {
      background: #eef2ff;        /* light bluish background */
      font-weight: bold;
    }
    
    /* 4) Each cell */
    .cell {
      padding: 12px 14px;
      border-bottom: 1px solid #eee;
    }
    
    /* Remove border from last row */
    .row:last-child .cell {
      border-bottom: none;
    }
    
    /* 5) Align numbers to the right */
    .row .cell:nth-child(2),
    .row .cell:nth-child(3) {
      text-align: right;
    }
    
    /* Make currency codes a bit stronger */
    .row .cell:nth-child(1) {
      font-weight: 600;
    }
    
    /* 6) Simple hover effect on body rows (not header) */
    .row:not(.header):hover {
      background: #f3f6ff;
    }