import json

with open("english_german.json") as f:
    e_to_g = json.load(f)
    
while True:
    e = input("e:")
    print(e_to_g.get(e, "not found"))

