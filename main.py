from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import os
import json

db_path = "./db.json"
f =  open(db_path, "r")
usr = json.load(f)
f.close()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Welcome": "welcome"}

@app.get("/getNSPData")
def users(search: Optional[str] = None):
    f = open(db_path, 'r')
    usr = json.load(f)
    f.close()
    name = search

    
    
    if name in usr :
        return {
             name: usr[name]      
        }
    # if name not in  usr :
    #     raise HTTPException(status_code = 404, detail =
    #         "User Not Found"
    # )
    return usr 

    
