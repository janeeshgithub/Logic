
class FoodItem:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def __lt__(self, other):
        return len(self.customers) > len(other.customers)  # To sort in descending order of customer count


def main():
    N = int(input())
    food_item_map = {}
    rc = list(range(1, N + 1))  # List of customer IDs

    for c in rc:
        p = input().split()
        for item in p:
            if item not in food_item_map:
                food_item_map[item] = FoodItem(item)
            food_item_map[item].customers.append(c)

    ct = 0
    while rc:
        # Sort food items by the number of customers, descending
        items = sorted(food_item_map.values())

        # Choose the food item with the most customers
        mp = items[0]
        ct += 1
        food_item_map.pop(mp.name)  # Remove the food item

        # Remove covered customers from the remaining list
        rc = [customer for customer in rc if customer not in mp.customers]

        # Remove the covered customers from other food items
        for food_item in food_item_map.values():
            food_item.customers = [customer for customer in food_item.customers if customer not in mp.customers]

    print(ct)


if __name__ == "__main__":
    main()
