from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal


class Fund(models.Model):
    """
    Stores information about an investment fund, including its identification,
    management details, performance metrics, and other key attributes.

    The Fund model represents a financial investment vehicle with various
    characteristics such as NAV (Net Asset Value), performance metrics,
    and management information.

    Fields:
        fund_id (CharField): Primary key identifier for the fund, max length 50 chars
        fund_name (CharField): Name of the fund, max length 255 chars
        fund_manager_name (CharField): Name of the fund manager, max length 255 chars
        fund_description (TextField): Detailed description of the fund
        fund_nav (DecimalField): Current Net Asset Value, non-negative, max 20 digits with 2 decimal places
        date_of_creation (DateField): Date when the fund was established
        fund_performance (DecimalField): Fund's performance as a percentage, between -100% and 1000%

    Example:
        >>> fund = Fund.objects.create(
        ...     fund_id="TECH001",
        ...     fund_name="Technology Growth Fund",
        ...     fund_manager_name="Jane Smith",
        ...     fund_description="A fund focused on high-growth tech companies",
        ...     fund_nav=Decimal('1000000.00'),
        ...     date_of_creation='2024-01-01',
        ...     fund_performance=Decimal('15.50')
        ... )
    """

    fund_id = models.CharField(
        "Fund ID",
        max_length=50,
        primary_key=True,
        help_text="Unique identifier for the fund. Used as the primary key.",
    )

    fund_name = models.CharField(
        "Fund Name",
        max_length=255,
        help_text="The full name of the investment fund.",
    )

    fund_manager_name = models.CharField(
        "Fund Manager Name",
        max_length=255,
        help_text="The name of the person managing this fund.",
    )

    fund_description = models.TextField(
        "Fund Description",
        help_text="Detailed description of the fund's investment strategy and objectives.",
    )

    fund_nav = models.DecimalField(
        "Fund Net Asset Value (NAV)",
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))],
        help_text="Current Net Asset Value of the fund. Must be non-negative.",
    )

    date_of_creation = models.DateField(
        "Date of Creation",
        help_text="The date when this fund was established.",
    )

    fund_performance = models.DecimalField(
        "Fund Performance (as a percentage)",
        max_digits=7,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal('-100.00')),
            MaxValueValidator(Decimal('1000.00'))
        ],
        help_text="Fund's performance as a percentage. Must be between -100% and 1000%.",
    )

    def __str__(self):
        """
        Returns a string representation of the Fund.

        Returns:
            str: Fund name followed by its ID in parentheses
        """
        return f"{self.fund_name} ({self.fund_id})"
