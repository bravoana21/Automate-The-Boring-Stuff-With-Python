def displayInventory(inventory):
    items_count = 0
    print('Inventory:')
    for item, quantity in inventory.items():
        print(str(quantity) + ' ' + item)
        items_count += 1
    print('Total number of items: ' + str(items_count))

def addToInventory(inventory, addedItems):
    for added_item in addedItems:
        inventory[added_item] = inventory.get(added_item, 0) + 1
    return inventory

inventory_1 = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory_1 = addToInventory(inventory_1, dragonLoot)
displayInventory(inventory_1)