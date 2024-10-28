"""Examplrs of dictionary syntax with Ice Cream Shop order tallies"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,  # trailing comma is not necessary, but can be easier to read visually, and adding a new entry is easier
}

print(len(ice_cream))

# use trailhead

# add key valye entries using subscription notation
ice_cream["mint"] = 10

# access values by their key using subscripton
mint_orders: int = ice_cream["mint"]
print(mint_orders)

# reassign values by their key using assignment
ice_cream["mint"] = ice_cream["mint"] + 1
ice_cream["mint"] += 1

# remove items by using the pop method
ice_cream.pop("strawberry")

# test if a key is in the dictionary
print("strawberry" in ice_cream)  # bool
print("vanilla" in ice_cream)  # bool

# loop through items using for-in loops
for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor}: {tally}")

