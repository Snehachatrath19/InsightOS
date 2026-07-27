import pandas as pd

class KPIEngine:

    def total_revenue(self, order_items):
        return order_items["price"].sum()

    def shipping_revenue(self, order_items):
        return order_items["freight_value"].sum()

    def total_items(self, order_items):
        return len(order_items)

    def average_price(self, order_items):
        return order_items["price"].mean()

    def average_shipping(self, order_items):
        return order_items["freight_value"].mean()