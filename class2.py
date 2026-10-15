""""students=("Bob",25,"DIT")
name,age,course=students
print(name)
print(course)
friends={"Lena":14,"Teesa":21,"Ethan":16}
print(friends["Lena"])

Students={
  "student1":{
  "name":"John Mark",
  "age":19,
  "course":"DS"
  },
  "student2":{
  "name":"Bob Marley",
  "age":24,
  "course":"CS"
  },
}

print(Students["student1"])

A={"s001","S002","S003"}
B={"S003","S004","S006"}
print(A&B)
print(A-B)
print(B-A)
print(A|B)
print(A-B|B-A)"""


stock = {
    "W001": ("Rolex Submariner", 1500),
    "W002": ("Casio G-Shock", 120),
    "S001": ("Nike Air Max", 90),
    "S002": ("Adidas Yeezy", 200),
    "S003": ("Rolex Submariner", 1500)
}
daily_orders = ["W001", "S001", "W001", "S002", "S001", "S001", "W002"]


# Unpack the tuple for 'S002' into variables 'name' and 'price'
name, price = stock["S002"]
print(f"{name} costs ${price}")

# i) Find and print the unique products ordered
unique_orders = set(daily_orders)
print("Unique products ordered:", unique_orders)

# ii) Use set difference to find which product was NOT ordered at all
all_stock_keys = set(stock.keys())
not_ordered = all_stock_keys.difference(unique_orders)
print("Product not ordered at all:", not_ordered)

# i) Add a new entry to 'stock'
stock["S004"] = ("Puma RS", 110)

# ii) Create a dictionary that counts product IDs in daily_orders
order_count = {}
for product_id in daily_orders:
    order_count[product_id] = order_count.get(product_id, 0) + 1
print("Order count:", order_count)

# iii) Calculate total sales for the day using order_count and stock
total_sales = 0
for product_id, count in order_count.items():
    price = stock[product_id][1]  # Extract price from the tuple
    total_sales += price * count

print(f"Total sales for the day: ${total_sales}")



