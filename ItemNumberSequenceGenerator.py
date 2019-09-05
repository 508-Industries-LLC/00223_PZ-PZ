# def item_number():
item_level_range = range(0,10000,1000)
for item_level_series in range(0,10,1):
    print(f"{item_level_series}",end=" ")
print("\n")
item_level_series = int(input("Select a series value: "))
if item_level_series == 0:
    for item_series_count in range(4):
        item_level_series = ''
        for new_item_series_count in range(4):
            item_level_series += str(0)
    print(f"You have chosen series: {item_level_series}")
    new_item_series = int(item_level_range[int(item_level_series)])
elif item_level_series or range(1,10,1):
    print(f"You have chosen series: {item_level_range[item_level_series]}")
    new_item_series = int(item_level_range[int(item_level_series)])
else:
    print("This is not an acceptable option")

item_range = range(0,1000,100)
for item_generator in range(0,10,1):
    print(f"{item_generator}",end=" ")
print("\n")
item_selection = int(input("Select a Resource range: "))
if item_selection == 0:
    for ResCount in range(3):
        item_selection = ''
        for NwResCount in range(3):
            item_selection += str(0)
    print(f"You have chosen Resource range: {item_selection}")
    new_item = int(item_range[int(item_selection)])
elif item_selection or range(1,10,1):
    print(f"You have chosen Resource range: {item_range[item_selection]}")
    new_item = int(item_range[int(item_selection)])
else:
    print("This is not an acceptable option")

item_qty_range = range(0,100,10)
for item_qty_generator in range(0,10,1):
    print(f"{item_qty_generator}",end=" ")
print("\n")
item_qty_selection = int(input("Select a Resource instance: "))
if item_qty_selection == 0:
    for ResQtyCount in range(2):
        item_qty_selection = ''
        for NwResQtyCount in range(2):
            item_qty_selection += str(0)
    print(f"You have chosen Resource instance: {item_qty_selection}")
    new_item_qty = int(item_qty_range[int(item_qty_selection)])
elif item_qty_selection or range(1,10,1):
    print(f"You have chosen Resource instance: {item_qty_range[item_qty_selection]}")
    new_item_qty = int(item_qty_range[int(item_qty_selection)])
else:
    print("This is not an acceptable option")

combined_series_item_qty = int(new_item_series) + int(new_item) + int(new_item_qty)
print(f"The Resource ID# is: {'{:04d}'.format(combined_series_item_qty)}")