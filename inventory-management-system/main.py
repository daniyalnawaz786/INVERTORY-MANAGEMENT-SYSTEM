from inventory import Inventory

inv = Inventory()

while True:
    print("\n--- Inventory Management System ---")
    print("1. Add Item")
    print("2. Update Quantity")
    print("3. Delete Item")
    print("4. View All Items")
    print("5. Search Item")
    print("6. Show Only Item Names")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        qty = int(input("Quantity: "))
        price = float(input("Price: "))
        inv.add_item(name, qty, price)

    elif choice == "2":
        item_id = int(input("Item ID: "))
        new_qty = int(input("New Quantity: "))
        inv.update_quantity(item_id, new_qty)

    elif choice == "3":
        item_id = int(input("Item ID: "))
        inv.delete_item(item_id)

    elif choice == "4":
        inv.view_items()

    elif choice == "5":
        name = input("Enter name to search: ")
        results = inv.search_item(name)

        if results:
            print("\n--- Search Results ---")
            for item in results:
                print(f"{item['id']}. {item['name']} | Qty: {item['quantity']} | Price: {item['price']}")
        else:
            print("No item found.")

    elif choice == "6":
        print(inv.get_item_names())

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")

