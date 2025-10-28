# ecommerce_sorting.py

orders = [
    {"order_id": 1001, "customer_name": "Alice", "total_amount": 1200.50, "order_date": "2025-10-21", "delivery_status": "Delivered"},
    {"order_id": 1002, "customer_name": "Bob", "total_amount": 800.00, "order_date": "2025-10-24", "delivery_status": "Pending"},
    {"order_id": 1003, "customer_name": "Charlie", "total_amount": 1500.00, "order_date": "2025-10-20", "delivery_status": "Shipped"},
    {"order_id": 1004, "customer_name": "David", "total_amount": 950.75, "order_date": "2025-10-23", "delivery_status": "Delivered"},
    {"order_id": 1005, "customer_name": "Eva", "total_amount": 300.25, "order_date": "2025-10-22", "delivery_status": "Cancelled"},
]

# 1. Implement a custom sorting algorithm (e.g., merge sort)
def bubble_sort(data, key_func, reverse=False):
    # Your code here
    arr = data.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if reverse:
                condition = key_func(arr[j]) < key_func(arr[j + 1])
            else:
                condition = key_func(arr[j]) > key_func(arr[j + 1])
            if condition:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 2. Sorting cases
def sort_by_amount(orders):
    #   """Sort by total amount (ascending)."""
     return bubble_sort(orders, key_func=lambda x: x["total_amount"], reverse=False)

def sort_by_date(orders):
    #   """Sort by order date (descending)."""
    return bubble_sort(orders, key_func=lambda x: x["order_date"], reverse=True)

def sort_by_status(orders):
    #   """Sort by delivery status (custom order)."""
    order_status = {"Delivered": 1, "Shipped": 2, "Pending": 3, "Cancelled": 4}
    return bubble_sort(orders, key_func=lambda x: order_status[x["delivery_status"]])

# 3. Print Top 5 Orders
def top_five_orders(orders):
    sorted_orders = bubble_sort(orders, key_func=lambda x: x["total_amount"], reverse=True)
    return sorted_orders[:5]


def main():
    print("Case 1: Sorted by total amount (ascending)")
    print(sort_by_amount(orders))

    print("\nCase 2: Sorted by order date (descending)")
    print(sort_by_date(orders))

    print("\nCase 3: Sorted by delivery status (custom order)")
    print(sort_by_status(orders))

    print("\nTop 5 orders by total amount:")
    print(top_five_orders(orders))

if __name__ == "__main__":
    main()