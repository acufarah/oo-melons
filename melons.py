"""Classes for melon orders."""


class AbstractMelonOrder:

    base_price = 5
    shipped = False

    # Specify these when subclassing
    tax = None

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty

    def get_total(self):
        total = (1 + self.tax) * self.qty * self.base_price
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True

        total = self.get_total()


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    tax = 0.08
    order_type = "domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        """Initialize melon order attributes."""
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

