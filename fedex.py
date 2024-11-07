import time
import pa
import requests

client_id_sandbox = 'l7994e4fc0ab85475cb993ff87e3586b0f'
client_id_prod = 'l7ad73b6b6da824b54ab0a290fcdd2a5c1'
client_secret_sandbox = '535386cf09344c88bc9791114651b568'
client_secret_prod = '191842e1-ef2e-44fa-9043-bd34ca15e476'
prod_url = 'https://apis.fedex.com/'
sandbox_url = 'https://apis-sandbox.fedex.com/'
auth = f"{sandbox_url}/oauth/token"
ship = f"{sandbox_url}/ship/v1/shipments"

payload = f'grant_type=client_credentials&client_id={client_id_sandbox}&client_secret={client_secret_sandbox}'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", auth, headers=headers, data=payload)

if response.status_code == 200:
    # Parse the JSON response to extract the token
    response_data = response.json()
    bearer_token = response_data.get('access_token')

    # Now you can use the 'bearer_token' for authenticated requests
    print(f"Bearer Token: {bearer_token}")
else:
    print(f"Failed to authenticate. Status code: {response.status_code}")


time.sleep(1)



