import spacy
import json

with open("backend\countries+states+cities.json", "r", encoding="utf-8") as file:
    geospatial_data = json.load(file)

cities = {city["name"].upper() for country in geospatial_data for state in country["states"] for city in state["cities"]}
states = {state["name"].upper() for country in geospatial_data for state in country["states"]}
countries = {country["name"].upper() for country in geospatial_data}


nlp = spacy.load("backend\en_core_web_sm")

def categorize_entities(text):
    
    doc = nlp(text)
    tokens = [token.text for token in doc]
    
    city_entities = set()
    state_entities = set()
    country_entities = set()

    
    for ent in tokens:
        if ent.upper() in cities:
            city_entities.add(ent)
        elif ent.upper() in states:
            state_entities.add(ent)
        elif ent.upper() in countries:
            country_entities.add(ent)

    
    categorized_entities = {
        "city_entities": list(city_entities),
        "state_entities": list(state_entities),
        "country_entities": list(country_entities),
    }
    
    return categorized_entities


