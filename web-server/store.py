import json
import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories', verify=False)
    print (r.status_code)
    print(r.text)
    print(type(r.text))
    print("\n")
    categories = r.json()
    
    with open("prueba.json", "w", encoding="utf-8") as file:
        json.dump(categories, file, indent=4, ensure_ascii=False)
    
    for category in categories:
        print(category['name'])
