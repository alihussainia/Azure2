import requests
import json
from dataDict import data

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://6fdee2c8-b1fb-4820-8a1c-529c5cefb96b.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'vwYPRsml5isrAIlkKVeS28nBwYtVa3u3'


# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())


