from fastapi import FastAPI, Path
app = FastAPI()

@app.get("/") # home page

def myprofile():
    return {"name":"Nesre"}

friends = {
    1:{
        "name": "Fozi", 
        "age": 20,
        "Level":"BSc"
    }
}

@app.get("/friends/{friend_id}")

def get_friend(friend_id: int = Path(..., description="ID of the friend you wanna view.", gt=0)):
    return friends[friend_id]

countries = {
    251:{"name": "Ethiopia"
         }
             }

@app.get("/country/{country_code}")

def country(country_code: int):
    return countries[country_code]