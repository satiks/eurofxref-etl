from io import BytesIO
from zipfile import ZipFile, BadZipFile
from requests import get, RequestException

class ECBFetcher:
    """
    Class to fetch and extract ECB (European Central Bank) exchange rate data.
    Provides methods to get daily and historical rates from ECB ZIP files.
    """

    DAILY_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip"
    HIST_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip"

    def __download_and_extract(self, url: str) -> str | None:
        """
        Download and extract the daily ECB exchange rates.

        :param url:URL of the ZIP file to download.
        :type url: str
        :return: Returns string representation of a daily ECB exchange rates
        :rtype: str
        :raises RuntimeError: If downloading or extracting fails.
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
        """
        Fetch the daily ECB exchange rate data.

        :returns: Content of the daily exchange rates file (decoded as UTF-8).
        :rtype: str
        :raises RuntimeError: If downloading or extracting the ECB ZIP file fails.
        """
        return self.__download_and_extract(self.DAILY_URL)

    def fetch_historical_ecb(self) -> str:
        """
        Fetch the historical ECB exchange rate data.

        :returns: Content of the historical exchange rates file (decoded as UTF-8).
        :rtype: str
        :raises RuntimeError: If downloading or extracting the ECB ZIP file fails.
        """
        return self.__download_and_extract(self.HIST_URL)