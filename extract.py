import json

with open("german_english.json") as f:
    e_to_g: dict[str,str] = json.load(f)
    
with open("extract1.txt") as e:
    extract = e.read()
    
def canonicalise(w: str) -> str:
    return "".join((filter(lambda c: c.isalpha(), w.strip().lower())))

words = map(canonicalise, extract.split(" "))

def try_translate(w: str) -> str:
    gw = e_to_g.get(w)
    if gw:
        return gw
    gw = e_to_g.get(w.title())
    if gw:
        return gw
    return w

words = map(try_translate, words)

print(extract)
extract =  " ".join(words)
print(extract)
