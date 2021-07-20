
'''
Simple python Backend Using Fast Api, 
No dependencies , no yarn no npm or any other boring library !!
Just clear and simple rest Api !!
Wrap data inside a dictionnary the send it !!
I love back end !!! :) !! 
'''
from fastapi import FastAPI,Request
from typing import Optional
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

album = [{'key':1,'title':'All the piano you need','artist':'Mireille Dumas','rating':4.1,'price':12},
{'key':2,'title':'Songs to test by','artist':'Francis Quokka','rating':4.9,'price':14},
{'key':3,'title':'The Greatest Show on Earth','artist':'Jean-Luc Kekes','rating':4.3,'price':16.50},
{'key':4,'title':'Dream is collapsing','artist':'Emy Le Iench','rating':4.6,'price':14.50},
{'key':5,'title':'Furious Ferrieu','artist':'Yanis Bensetti','rating':4.2,'price':12.50},
{'key':6,'title':'Mr. Roquefort','artist':'Océane and the Queens','rating':4.8,'price':14}]


@app.get("/albums")
def albums():
    result = album
    return result
