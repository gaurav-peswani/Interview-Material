"""
Task: Calculate Total Price Based on Order and Shipping Cost

Given:
- An order containing the destination country and a list of items.
- A shipping cost table that specifies the cost for each product in each country.

Example 1: Fixed Shipping Cost
Order:
{
    "country": "US",  # or "CA" for Canadian orders
    "items": [
        {"product": "mouse", "quantity": 20},
        {"product": "laptop", "quantity": 5}
    ]
}

Shipping Cost Table:
{
    "US": [
        {"product": "mouse", "cost": 550},
        {"product": "laptop", "cost": 1000}
    ],
    "CA": [
        {"product": "mouse", "cost": 750},
        {"product": "laptop", "cost": 1100}
    ]
}

Expected Output:
- For order_US, the total shipping cost = 16,000.
- For order_CA, the total shipping cost = 20,500.

---

Example 2: Tiered Shipping Cost Based on Quantity
In this scenario, the shipping cost decreases as the quantity increases.

Order (unchanged):
{
    "country": "US",
    "items": [
        {"product": "mouse", "quantity": 20},
        {"product": "laptop", "quantity": 5}
    ]
}

Shipping Cost Table with Tiers:
{
    "US": [
        {"product": "mouse", "costs": [{"minQuantity": 0, "maxQuantity": null, "cost": 550}]},
        {"product": "laptop", "costs": [
            {"minQuantity": 0, "maxQuantity": 2, "cost": 1000},
            {"minQuantity": 3, "maxQuantity": null, "cost": 900}
        ]}
    ],
    "CA": [
        {"product": "mouse", "costs": [{"minQuantity": 0, "maxQuantity": null, "cost": 750}]},
        {"product": "laptop", "costs": [
            {"minQuantity": 0, "maxQuantity": 2, "cost": 1100},
            {"minQuantity": 3, "maxQuantity": null, "cost": 1000}
        ]}
    ]
}

Expected Output:
- For order_US with tiered shipping cost = 15,700.
- For order_CA with tiered shipping cost = 20,500.

---

Task:
Implement a function `calculate_shipping_cost(order, shipping_cost)` to compute 
the total shipping cost based on the rules described above.
"""

class ShippingCost:

    def __init__(self, costs: dict) -> None:
        self.costs = costs
        
    def calculate_shipping_cost(self, order: str) -> int:
        country = order["country"]
        items = order["items"]
        total_price = 0

        for item in items:
            product = item["product"]
            quantity = item["quantity"]
            cost = self.__get_item_price(country, product, quantity)
            print(f"[{country}] Price for {quantity} {product}(s) is {cost} * {quantity} = {cost * quantity}")
            total_price += (cost * quantity)
        
        return total_price


    def __get_item_price(self, country: str, product: str, quantity: int) -> int:
        for item_details in self.costs[country]:
            if item_details["product"] == product:
                if "cost" in item_details:
                    return item_details["cost"]

                if "costs" in item_details:
                    for cost in item_details["costs"]:
                        
                        if cost["minQuantity"] is None:
                            minQty = -float('inf')
                        else:
                            minQty = cost["minQuantity"]

                        if cost["maxQuantity"] is None:
                            maxQty = float('inf')
                        else:
                            maxQty = cost["maxQuantity"]

                        if minQty <= quantity <= maxQty:
                            return cost["cost"]
        return 0
    
if __name__ == "__main__":
    orders = [{
        "country": "US",  # or "CA" for Canadian orders
        "items": [
            {"product": "mouse", "quantity": 20},
            {"product": "laptop", "quantity": 5}
        ]
    },
    {
        "country": "CA",  # or "CA" for Canadian orders
        "items": [
            {"product": "mouse", "quantity": 20},
            {"product": "laptop", "quantity": 5}
        ]
    }]

    costs = {
        "US": [
            {"product": "mouse", "cost": 550},
            {"product": "laptop", "cost": 1000}
        ],
        "CA": [
            {"product": "mouse", "cost": 750},
            {"product": "laptop", "cost": 1100}
        ]
    }

    sc = ShippingCost(costs=costs)
    for order in orders:
        print(f"[TOTAL] {sc.calculate_shipping_cost(order=order)}")
    print()

    costs = {
        "US": [
            {"product": "mouse", "costs": [{"minQuantity": 0, "maxQuantity": None, "cost": 550}]},
            {"product": "laptop", "costs": [
                {"minQuantity": 0, "maxQuantity": 2, "cost": 1000},
                {"minQuantity": 3, "maxQuantity": None, "cost": 900}
            ]}
        ],
        "CA": [
            {"product": "mouse", "costs": [{"minQuantity": 0, "maxQuantity": None, "cost": 750}]},
            {"product": "laptop", "costs": [
                {"minQuantity": 0, "maxQuantity": 2, "cost": 1100},
                {"minQuantity": 3, "maxQuantity": None, "cost": 1000}
            ]}
        ]
    }

    sc = ShippingCost(costs=costs)
    for order in orders:
        print(f"[TOTAL] {sc.calculate_shipping_cost(order=order)}")



