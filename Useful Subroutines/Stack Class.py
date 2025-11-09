
list1 = {
    "Hopper": 28,
    "Chest": 22,
    "Glass": 16,
    "Yellow Wool": 13,
    "Orange Carpet": 12,
    "Redstone Dust": 8,
    "Activator Rail": 4,
    "Redstone Comparator": 4,
    "Redstone Torch": 4,
    "Target": 4,
    "White Concrete Powder": 4,
    "Blue Ice": 3,
    "Oak Sign": 2,
    "Oxidized Copper": 1,
    "Rail": 1,
    "Water Bucket": 1,
    "Waxed Oxidized Copper Chest": 1,
    "Waxed Oxidized Copper Trapdoor": 1,
}

list2 = {
    "Chest": 14,
    "Hopper": 12,
    "Glass": 10,
    "Yellow Wool": 7,
    "Orange Carpet": 6,
    "Redstone Dust": 4,
    "Activator Rail": 2,
    "Blue Ice": 2,
    "Redstone Comparator": 2,
    "Redstone Torch": 2,
    "Target": 2,
    "Rail": 1,
    "Water Bucket": 1,
    "White Concrete": 1,
    "White Concrete Powder": 1,
}

list3 = {
    "Hopper": 54,
    "Glass": 44,
    "Yellow Wool": 38,
    "Chest": 36,
    "Orange Carpet": 21,
    "Redstone Dust": 20,
    "Redstone Comparator": 9,
    "Blue Ice": 7,
    "Activator Rail": 6,
    "Redstone Torch": 6,
    "Target": 6,
    "White Concrete Powder": 6,
    "Observer": 4,
    "Dropper": 3,
    "Redstone Repeater": 3,
    "Oak Sign": 2,
    "Rail": 2,
    "Sticky Piston": 2,
    "Water Bucket": 2,
    "Oxidized Copper": 1,
    "Soul Sand": 1,
    "Waxed Oxidized Copper Chest": 1,
    "Waxed Oxidized Copper Trapdoor": 1,
}

# Multipliers
multiplied_list1 = {k: v*3 for k, v in list1.items()}  # 3x
multiplied_list2 = {k: v*2 for k, v in list2.items()}  # 2x
multiplied_list3 = {k: v*6 for k, v in list3.items()}  # 6x

# Combine into one dictionary
final_counts = {}

for d in [multiplied_list1, multiplied_list2, multiplied_list3]:
    for item, qty in d.items():
        final_counts[item] = final_counts.get(item, 0) + qty

for item, quant in final_counts.items():
    print(item, quant)
