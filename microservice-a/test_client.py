import json
import os

request_data = {"title": "Halo 3"}
with open("request.json", "w") as f:
    json.dump(request_data, f)

os.system("python3 game_service.py")

with open("response.json", "r") as f:
    response = json.load(f)
    print("Response from Microservice:")
    print(json.dumps(response, indent=2))
