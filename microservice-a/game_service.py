import json

games = {
    "halo 3": {"title": "Halo 3", "genre": "Shooter", "platform": "Xbox 360", "year": 2007},
    "minecraft": {"title": "Minecraft", "genre": "Sandbox", "platform": "Multi-platform", "year": 2011},
    "portal": {"title": "Portal", "genre": "Puzzle", "platform": "PC", "year": 2007}
}

with open('request.json', 'r') as f:
    data = json.load(f)
    title = data.get("title", "").lower()

result = games.get(title, {"error": "Game not found. Please try another title."})

with open('response.json', 'w') as f:
    json.dump(result, f, indent=2)
