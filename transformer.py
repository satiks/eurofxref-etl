from Currency import Currency
from fetcher import ECBFetcher


class ECBFTransformer:
    """
    Transform ECB exchange rate data into structured Currency objects.
    """

    CURRENCIES = ["USD", "SEK", "GBP", "JPY"]

    def __init__(self):
        """
        Initialize the ECBFTransformer instance.

        Creates an internal ECBFetcher instance used to retrieve
        ECB exchange rate data.
        """
        self.fetcher = ECBFetcher()

    def get_currencies_data(self) -> list[Currency]:
        """
        Fetch and transform ECB data into Currency objects.

        :returns: List of Currency objects containing current rate and historical mean rate.
        :rtype: list[Currency]
        """
        daily_data = self.__convert_to_dict(self.fetcher.fetch_daily_ecb())
        hist_data = self.__convert_to_dict(self.fetcher.fetch_historical_ecb())
        currencies = []

        for cur in self.CURRENCIES:
            rate_list = daily_data.get(cur)
            rate = rate_list[0] if rate_list else None

            mean_rate = self.__calculate_mean(hist_data, cur)

            currency_obj = Currency(cur, rate, mean_rate)
            currencies.append(currency_obj)

        return currencies

    def __convert_to_dict(self, data: str) -> dict[str, list[float]]:
        """
        Convert ECB CSV data into a dictionary structure.

        The first column (date) is ignored.

        :param data: Raw CSV content as a string.
        :type data: str
        :returns: Dictionary mapping currency codes to lists of float exchange rate values.
        :rtype: dict[str, list[float]]
        """
        lines = data.strip().split("\n")

        header = [h.strip() for h in lines[0].split(",") if h.strip() != ""][1:]
        data_dict = {h: [] for h in header}

        for line in lines[1:]:
            parts = [v.strip() for v in line.split(",") if v.strip() != ""][1:]
            for i, name in enumerate(header):
                value = parts[i]
                try:
                    data_dict[name].append(float(value))
                except ValueError:
                    continue
        return data_dict

    def __calculate_mean(self, data: dict[str, list[float]], cur: str) -> float | None:
        """
        Calculate the mean exchange rate for a currency.

        :param data: Dictionary containing currency rates.
        :type data: dict[str, list[float]]
        :param cur: Currency code (e.g., "USD").
        :type cur: str
        :returns: Mean exchange rate rounded to 4 decimals, or None if no values are available.
        :rtype: float | None
        """
        values = data.get(cur)

        if not values:
            return None

        return round(sum(values) / len(values), 4)