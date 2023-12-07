import sys
import requests
import json

# Check if the base URL is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python your_script.py <base_url>")
    sys.exit(1)

# Get the base URL from the command-line argument
base_url = sys.argv[1]

def get_headers():
    # Define your headers here
    headers = {
        'Authorization': 'your_token_here',
        'Content-Type': 'application/json'
    }
    return headers

# Function to make a POST request
def post_request(endpoint, payload):
    url = f"{base_url}/{endpoint}"
    headers = get_headers()
    response = requests.post(url, headers=headers, data=payload)
    print(f"URL: {url}")
    print(f"Response: {response.text}\n")

# Function to make a GET request
def get_request(endpoint):
    url = f"{base_url}/{endpoint}"
    headers = get_headers()
    response = requests.get(url, headers=headers)
    print(f"URL: {url}")
    print(f"Response: {response.text}\n")

# Example usage:

# POST request to /customer/signup
payload_signup = json.dumps({
    "email": "test4@test.com",
    "phone": "12345"
})
post_request("customer/signup", payload_signup)

# POST request to /customer/login
payload_login = json.dumps({
    "email": "test4@test.com",
})
post_request("customer/login", payload_login)

# GET request to /customer/profile
get_request("customer/profile")

# GET request to /customer/shoping-details (assuming it's a typo in the endpoint name)
get_request("customer/shopping-details")

# POST request to /customer/address
payload_address = json.dumps({
    "street": "Mumbai",
    "postalCode": "400066",
    "city": "Mumbai",
    "country": "India"
})
post_request("customer/address", payload_address)

# GET request to /customer/wishlist
get_request("customer/wishlist")

# POST request to /customer/app-events
payload_app_events = json.dumps({
    "payload": {
        "event": "TESTING",
        "data": {}
    }
})
post_request("customer/app-events", payload_app_events)
