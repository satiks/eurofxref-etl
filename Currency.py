class Currency:
    """
    A class used to represent a Currency.

    Attributes:
        name (str): Currency code (e.g., "USD", "GBP")
        exchange_rate (float | None): Latest available exchange rate from ECB
        mean_rate (float | None): Average historical exchange rate
    """

    def __init__(self, name: str, exchange_rate: float | None, mean_rate: float | None):
        """
        Initialize a Currency object.

        :param name: Currency code
        :type name: str
        :param exchange_rate: Current exchange rate
        :type exchange_rate: float | None
        :param mean_rate: Average historical exchange rate
        :type mean_rate: float | None
        """
        self.name = name
        self.exchange_rate = exchange_rate
        self.mean_rate = mean_rate

    def __str__(self) -> str:
        """
        String representation of a Currency object.

        If a rate is missing, "N/A" is shown.

        :return: Returns string representation of a Currency object
        :rtype: str
        """
        exchange = self.exchange_rate if self.exchange_rate is not None else "N/A"
        mean = self.mean_rate if self.mean_rate is not None else "N/A"
        return f"{self.name}: current={exchange}, mean={mean}"