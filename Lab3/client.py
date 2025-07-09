import requests

BASE_URL = "http://127.0.0.1:8000"

def print_response(resp):
    print(f"URL: {resp.url}")
    print(f"Status Code: {resp.status_code}")
    print(f"Response JSON: {resp.json()}")
    print("-" * 50)

def main():
    # Hello world
    resp = requests.get(BASE_URL + "/")
    print_response(resp)

    # GET with query string parameters
    resp = requests.get(BASE_URL + "/items/", params={"q": "test query", "limit": 5})
    print_response(resp)

    # GET with path parameter
    resp = requests.get(BASE_URL + "/items/123")
    print_response(resp)

    # PUT with path param + body input
    data = {
        "name": "Test Item",
        "description": "A sample item",
        "price": 12.5,
        "tax": 0.5
    }
    resp = requests.put(BASE_URL + "/items/123", json=data)
    print_response(resp)

    # GET with multiple query params
    resp = requests.get(BASE_URL + "/users/", params={"skip": 10, "limit": 3, "active": "false"})
    print_response(resp)

    # GET with required query param
    resp = requests.get(BASE_URL + "/search/", params={"term": "fastapi"})
    print_response(resp)

    # GET multiple path params
    resp = requests.get(BASE_URL + "/users/7/items/abc")
    print_response(resp)

    # PUT update user info with body input
    data = {"username": "jdoe", "email": "jdoe@example.com", "full_name": "John Doe"}
    resp = requests.put(BASE_URL + "/users/7", json=data)
    print_response(resp)

    # GET with optional query param
    resp = requests.get(BASE_URL + "/products/")
    print_response(resp)

    # PUT with partial update
    data = {"price": 19.99}
    resp = requests.put(BASE_URL + "/partial-item/42", json=data)
    print_response(resp)

    # GET with boolean query param
    resp = requests.get(BASE_URL + "/flags/", params={"enabled": "true"})
    print_response(resp)

    # GET with multiple path and query params
    resp = requests.get(BASE_URL + "/orders/1001", params={"detailed": "true"})
    print_response(resp)

    # PUT to update order status
    data = {"status": "shipped"}
    resp = requests.put(BASE_URL + "/orders/1001", json=data)
    print_response(resp)

    # GET with list query param
    resp = requests.get(BASE_URL + "/tags/", params=[("tags", "red"), ("tags", "blue")])
    print_response(resp)

    # GET with date query param
    resp = requests.get(BASE_URL + "/events/", params={"date": "2025-06-18"})
    print_response(resp)

    # PUT update event details
    data = {"name": "Conference", "location": "NYC", "attendees": 300}
    resp = requests.put(BASE_URL + "/events/55", json=data)
    print_response(resp)

if __name__ == "__main__":
    main()
