products = {}

    # === Input section ===
while True:
    code = int(input("Enter product code (-1 to finish): "))
    if code == -1:
        break

    productType = input("Enter product type (dairy, grocery, produce, cleaning, butcher, others): ")
    description = input("Enter product description: ")
    currentStock = int(input("Enter current stock: "))
    minStock = int(input("Enter minimum stock: "))
    unitPrice = float(input("Enter unit price: "))

    products[code] = {
        "productType": productType,
        "description": description,
        "currentStock": currentStock,
        "minStock": minStock,
        "unitPrice": unitPrice
    }

print("\n--- REPORTS ---")

if 124 in products:
    if products[124]["currentStock"] > 0:
            print("✅ Product 124 can be sold.")
    else:
        print("❌ Product 124 cannot be sold (no stock).")
else:
    print("❌ Product 124 does not exist.")

print("\nProducts below minimum stock:")
for code, data in products.items():
    if data["currentStock"] < data["minStock"]:
        print(f"Code: {code}, Description: {data['description']}")

dairyCount = sum(1 for data in products.values() if data["productType"].lower() == "dairy")
print("\nNumber of dairy products:", dairyCount)

groceryProducts = [data for data in products.items() if data[1]["productType"].lower() == "grocery"]
if groceryProducts:
    minStockProduct = min(groceryProducts, key=lambda x: x[1]["currentStock"])
    print("\nGrocery product with lowest stock:")
    print(f"Code: {minStockProduct[0]}, Description: {minStockProduct[1]['description']}")
else:
    print("\nNo grocery products registered.")

if 3148 in products:
    print("\nDescription of product 3148:", products[3148]["description"])
else:
    print("\nProduct 3148 does not exist.")

stockByType = {}
for data in products.values():
    t = data["productType"]
    stockByType[t] = stockByType.get(t, 0) + data["currentStock"]

if stockByType:
    minType = min(stockByType, key=stockByType.get)
    print("\nProduct type with the fewest units available:", minType)
else:
    print("\nNo product types available.")

order = []
print("\n--- Enter product codes for the order (0 to finish) ---")
while True:
    code = int(input("Product code: "))
    if code == 0:
        break
    order.append(code)

totalAmount = 0
soldProducts = []

for code in order:
    if code in products and products[code]["currentStock"] > 0:
        totalAmount += products[code]["unitPrice"]
        products[code]["currentStock"] -= 1
        soldProducts.append(code)

print("\n--- Purchase summary ---")
print("Total amount to pay:", totalAmount)
print("Products sold (codes):", soldProducts)