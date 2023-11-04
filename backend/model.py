import spacy
import json
import os

# Use os.path.join() to create the file path for the JSON data
json_data_path = os.path.join('backend', 'countries+states+cities.json')

# Use os.path.join() to create the path for the SpaCy model
spacy_model_path = os.path.join('backend', 'en_core_web_sm/en_core_web_sm')

with open(json_data_path, "r", encoding="utf-8") as file:
    geospatial_data = json.load(file)

cities = {city["name"].upper() for country in geospatial_data for state in country["states"] for city in state["cities"]}
states = {state["name"].upper() for country in geospatial_data for state in country["states"]}
countries = {country["name"].upper() for country in geospatial_data}

nlp = spacy.load(spacy_model_path)

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
