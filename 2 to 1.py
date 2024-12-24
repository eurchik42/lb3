import requests
from requests.auth import HTTPBasicAuth

# Constants
USERNAME = 'admin'
PASSWORD = 'password'
BASE_URL = 'http://127.0.0.1:5000/items'

# Function to fetch all items
def get_items():
    response = requests.get(BASE_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if response.status_code == 200:
        items = response.json()
        print("Items in catalog:")
        for item in items:
            print(item)
    else:
        print(f"Failed to get items: {response.status_code}, {response.text}")

# Function to add a new item
def add_item(name, price, size, weight, color):
    item_data = {
        'name': name,
        'price': price,
        'size': size,
        'weight': weight,
        'color': color
    }
    response = requests.post(BASE_URL, json=item_data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if response.status_code == 201:
        print(f"Item added successfully: {response.json()}")
    else:
        print(f"Failed to add item: {response.status_code}, {response.text}")

# Function to update an existing item
def update_item(item_id, name=None, price=None, size=None, weight=None, color=None):
    item_data = {}
    if name:
        item_data['name'] = name
    if price:
        item_data['price'] = price
    if size:
        item_data['size'] = size
    if weight:
        item_data['weight'] = weight
    if color:
        item_data['color'] = color

    response = requests.put(f"{BASE_URL}/{item_id}", json=item_data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if response.status_code == 200:
        print(f"Item updated successfully: {response.json()}")
    else:
        print(f"Failed to update item: {response.status_code}, {response.text}")

# Function to delete an item
def delete_item(item_id):
    response = requests.delete(f"{BASE_URL}/{item_id}", auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if response.status_code == 200:
        print("Item deleted successfully")
    else:
        print(f"Failed to delete item: {response.status_code}, {response.text}")

# Main script
if __name__ == '__main__':
    print("Fetching all items...")
    get_items()

    print("\nAdding a new item...")
    add_item("New Item", 100.0, "M", 1.2, "Red")

    print("\nUpdating an item...")
    update_item(1, price=120.0, color="Blue")

    print("\nDeleting an item...")
    delete_item(1)

    print("\nFetching all items again...")
    get_items()