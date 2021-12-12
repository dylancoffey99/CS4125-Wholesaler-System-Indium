"""This module contains the DiscountCategory class."""


class DiscountCategory:
    """
    This class represents a model of a discount category, containing a constructor,
    and the getter methods for its parameters.
    """

    def __init__(self, discount_id: int, discount_name: str, discount_percentage: float):
        """
        This constructor instantiates a discount category object.

        :param discount_id: ID of the discount category.
        :param discount_name: Name of the discount category.
        :param discount_percentage: Discount percentage of the discount category.
        """
        self.discount_id = discount_id
        self.discount_name = discount_name
        self.discount_percentage = discount_percentage

    def get_discount_id(self) -> int:
        """
        This method gets the discount ID.

        :returns: ID of the discount category.
        """
        return self.discount_id

    def get_discount_name(self) -> str:
        """
        This method gets the discount name.

        :returns: Name of the discount category.
        """
        return self.discount_name

    def get_discount_percentage(self) -> float:
        """
        This method gets the discount percentage.

        :returns: Discount percentage of the discount category.
        """
        return self.discount_percentage

    def calc_discount(self, order_subtotal: float):
        """
        This method calculates the discount amount of a order
        subtotal.

        :param order_subtotal: Subtotal of an order.
        :returns: Discount amount of an order subtotal.
        """
        return order_subtotal * self.get_discount_percentage()
