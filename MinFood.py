class FoodItem:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def __lt__(self, other):
        return len(self.customers) > len(other.customers)

def main():
    N = int(input())
    food_item_map = {}
    rc = list(range(1, N + 1))
    for c in rc:
        p = input().split()
        for item in p:
            if item not in food_item_map:
                food_item_map[item] = FoodItem(item)
            food_item_map[item].customers.append(c)

    ct = 0
    while rc:
        items = sorted(food_item_map.values())
        mp = items[0]
        ct += 1
        food_item_map.pop(mp.name)
        rc = [customer for customer in rc if customer not in mp.customers]

        for food_item in food_item_map.values():
            food_item.customers = [customer for customer in food_item.customers if customer not in mp.customers]

    print(ct)


if __name__ == "__main__":
    main()
