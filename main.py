from fastapi import FastAPI
from pydantic import BaseModel
import spacy
import random



nlp = spacy.blank('en')
custom_nlp = spacy.load("custom_ner_model")

app = FastAPI()

class text(BaseModel):
    Text: str


@app.post('/')
async def label_location(item: text):
    
    text = item.Text
    doc = custom_nlp(text)
    location_label = []
    for ent in doc.ents:
        location_label.append([ent.text, ent.label_])
    return {"result": location_label}