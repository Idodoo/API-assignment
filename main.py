from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, Union
import os
import json
import re 

db_path = "./db.json"
f =  open(db_path, "r")
usr = json.load(f)
f.close()

db_info = "./search.json"
f =  open(db_info, "r")
data = json.load(f)
f.close()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Welcome": "welcome"}

@app.get("/getNSPData")
def users(search: Optional[str] = None):
    
    f = open(db_path, 'r')
    usr = json.load(f)
    
    
    f.close()
    

    if search == None:    
    
     return usr
    
    elif search in usr :
        return {search: usr[search]}

    elif search not in usr :
        raise HTTPException(status_code = 404, detail = "User Not Found")

@app.get("/NSPData/{str}")
def singleusr(str:str):
    f = open(db_path, 'r')
    usr = json.load(f)      
    f.close()

    if str in usr :
        return {str: usr[str]}

    else :
        raise HTTPException(status_code = 404, detail = "User Not Found")
            


@app.get("/Info")
def info():
    fs = open(db_info, 'r')
    google = json.load(fs)
    f.close()
    return google
    
@app.get("/Info/{search}")
def find(search:str):
    fs = open(db_info, 'r')
    google = json.load(fs)
    hh = search
    f.close()
    regex = "^(.?(\b"+search+"\b)[^$])$"
    foo = rf'^(.*?(\b{search}\b)[^$]*)$'
    wordRegex = '/\b(?:w|-)+\b/g'
    # rf"^(.?(\b{search}\b)[^$])$"
    # print(foo)
    
    # print(regex)
    json_string = "{Issues: 'an important topic or problem for debate or discussion, Food : 'Food is any substance consumed to provide nutritional support for an organism. Food is usually of plant, animal, or fungal origin, and contains essential nutrients, such as carbohydrates, fats, proteins, vitamins, or minerals.',Love : 'a great interest and pleasure in something.',Broken Heart : 'Broken heart syndrome is a heart condition and extreme emotions. The condition also can be triggered by a serious physical illness or surgery. Broken heart syndrome is often a temporary condition. But some people may continue to feel unwell after the heart is healed.',Family : 'a group of one or more parents and their children living together as a unit.'}"
    # re_pattern = re.compile(foo)
    # match = re_pattern.findall(json_string)
    # print(match)
    # result = re.search(foo, json_string, re.IGNORECASE)
    # fx = re.search(foo,json_string,)
    # spl = re.split(r'\s', search, re.IGNORECASE)
    # an = set(spl)
    # dd = list()


    # for i in an:
    #     if i in google:

    #         dd.append(google[i] )    

       
            

    
    # return dd


    arraySearch = []

    ff = re.split(" ", search.upper())
    df = set(ff)
    dddd = set()
    
    for el in google:

        for d in df:

            if (el==d):
                dddd.add(google[el])
                

    return dddd
        



      

         

    

   
    
   
    
    

    
   

    

    
    
    
    
    
    
    
    # if result:
    #     print("a")

    # else:
    #     print("f")    
    
    
    # for i in google:

   
        
      

        
    
    

    

    # result = re.match(df, string)
    

    # df = "^(.?(\b"+search+"\b)[^$])$"
    # print(df)

    

    # fff = re.match(df, google.match)
    # print(fff)


    # fss = re.findall(r"^(.?(\b" + search + "\b)[^$])$", google)

    # print(df)
    # patternx = r'\b(?:Issues|Food|Love|Broken Heart|Family)\b'
    # gf = r"^(.?(\b" + search + "\b)[^$])$"

    # s = re.search(patternx, search)
    # fsss = re.findall(r"^(.?(\b" + search + "\b)[^$])$")

    # print(fsss)

    


    # if re.match(pattern, string)

    
    
    # print(df)
        
    
        
        # return { 
        #     s : google[s]
        # }
        # print(google[s])
    # d = re.findall(, search)
    # for d in google:
    #     print({d:google[d]})

#    d= re.findall(r'', )

