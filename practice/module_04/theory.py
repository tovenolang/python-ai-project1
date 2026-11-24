class Commission:
    def __init__(self, rate):
        self.rate = rate

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        if not 0 <= value <= 0.1:
            raise ValueError(f"rate must be between 0 and 0.1, not {value}")
        self._rate = value


commission = Commission(0.03)
print("Rate:", commission.rate)
commission.rate = 0.5