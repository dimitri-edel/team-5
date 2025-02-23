import requests

PROD_URL = "https://team5-api-eu-5d24fa110c36.herokuapp.com"

def visit_prod_endpoint(endpoint: str = "/") -> requests.Response:
    """
    Visit a production endpoint and return the response.
    
    Args:
        endpoint (str): The endpoint to visit, defaults to root "/"
    
    Returns:
        requests.Response: The response from the production server
    """
    # Ensure endpoint starts with /
    if not endpoint.startswith("/"):
        endpoint = f"/{endpoint}"
        
    url = f"{PROD_URL}{endpoint}"
    response = requests.get(url)
    return response

