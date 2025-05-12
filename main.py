from core.inventory import Inventory
from models.electronics import Electronics
from models.grocery import Grocery
from models.clothing import Clothing
from utils.json_handler import save_to_file, load_from_file

def menu():
    inv = Inventory()
    while True:
        print("\n=== Inventory Menu ===")
        print("1. Add Product")
        print("2. Sell Product")
        print("3. View All Products")
        print("4. Search Product by Name")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Total Inventory Value")
        print("8. Remove Expired Groceries")
        print("9. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            type_ = input("Product Type (Electronics/Grocery/Clothing): ").strip()
            pid = input("Product ID: ")
            name = input("Name: ")
            price = float(input("Price: "))
            qty = int(input("Quantity: "))

            if type_.lower() == 'electronics':
                brand = input("Brand: ")
                warranty = int(input("Warranty Years: "))
                product = Electronics(pid, name, price, qty, warranty, brand)
            elif type_.lower() == 'grocery':
                expiry = input("Expiry Date (YYYY-MM-DD): ")
                product = Grocery(pid, name, price, qty, expiry)
            elif type_.lower() == 'clothing':
                size = input("Size: ")
                material = input("Material: ")
                product = Clothing(pid, name, price, qty, size, material)
            else:
                print("Invalid product type.")
                continue

            try:
                inv.add_product(product)
                print("Product added.")
            except Exception as e:
                print(e)

        elif choice == '2':
            pid = input("Product ID to sell: ")
            qty = int(input("Quantity: "))
            try:
                inv.sell_product(pid, qty)
                print("Sold successfully.")
            except Exception as e:
                print(e)

        elif choice == '3':
            for p in inv.list_all_products():
                print(p)

        elif choice == '4':
            name = input("Search by name: ")
            for p in inv.search_by_name(name):
                print(p)

        elif choice == '5':
            save_to_file(inv, 'inventory.json')
            print("Saved to inventory.json")

        elif choice == '6':
            try:
                load_from_file(inv, 'inventory.json')
                print("Loaded successfully.")
            except Exception as e:
                print(e)

        elif choice == '7':
            print(f"Total Value: {inv.total_inventory_value()}")

        elif choice == '8':
            inv.remove_expired_products()
            print("Expired groceries removed.")

        elif choice == '9':
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
