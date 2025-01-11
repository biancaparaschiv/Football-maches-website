from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv()

ES_USERNAME = os.getenv("ES_USERNAME")
ES_PASSWORD = os.getenv("ES_PASSWORD")
#Elasticsearch connection
try:
    es = Elasticsearch(
        "https://localhost:9200",
        
        basic_auth=(ES_USERNAME,ES_PASSWORD), 
        verify_certs=False
#        ca_certs="/Users/remygodin/Desktop/Semester2/DSE/project/elasticsearch-8.13.4/config/certs/http_ca.crt"
    )
except Exception as e:
    print("Error: ", e)
if es.ping():
    
    print("Connected to ES!")
else: 
    print(es.info())
    print("Could not connect to ES") 
INDEX_NAME = "matches"

#FastAPI
app = FastAPI()

#Pydantic model for input validation
class Match(BaseModel):
    id: int
    time: str
    date: str
    stage: str
    stadium: str
    city: str
    home_team: str
    home_team_goals: int
    away_team_goals: int
    away_team: str
    win_conditions: str
    penalty: Optional[str]
    win: str
    total_goals: int
    attendance: int
    

#Initialize Elasticsearch index
def initialize_index():
    if not es.indices.exists(index=INDEX_NAME):
        es.indices.create(
            index=INDEX_NAME,
            body={
                "mappings": {
                    "properties": {
                        "id": {"type": "integer"},
                        "time": {"type": "text"},
                        "date": {"type": "date"},
                        "stage": {"type": "text"},
                        "stadium": {"type": "text"},
                        "city": {"type": "text"},
                        "home_team": {"type": "text"},
                        "home_team_goals": {"type": "integer"},
                        "away_team_goals": {"type": "integer"},
                        "away_team": {"type": "text"},
                        "win_conditions": {"type": "text"},
                        "penalty": {"type": "text"},
                        "win": {"type": "text"},
                        "total_goals": {"type": "integer"},
                        "attendance": {"type": "integer"},
                    }
                }
            },
        )

initialize_index()

#API Endpoints
@app.post("/matches")
def add_match(match: Match):
    if es.exists(index=INDEX_NAME, id=match.id):
        raise HTTPException(status_code=400, detail="Match with this ID already exists.")
    es.index(index=INDEX_NAME, id=match.id, document=match.dict())
    return {"message": "Match added successfully."}

@app.get("/matches")
def get_all_matches():
    response = es.search(index=INDEX_NAME, body={"query": {"match_all": {}}})
    matches = [hit["_source"] for hit in response["hits"]["hits"]]
    return {"matches": matches}

@app.get("/matches/home-team")
def search_by_home_team(home_team: str):
    response = es.search(
        index=INDEX_NAME,
        body={"query": {"match": {"home_team": home_team}}}
    )
    matches = [hit["_source"] for hit in response["hits"]["hits"]]
    if not matches:
        raise HTTPException(status_code=404, detail="No matches found for this home team.")
    return {"matches": matches}

@app.get("/matches/away-team")
def search_by_away_team(away_team: str):
    response = es.search(
        index=INDEX_NAME,
        body={"query": {"match": {"away_team": away_team}}}
    )
    matches = [hit["_source"] for hit in response["hits"]["hits"]]
    if not matches:
        raise HTTPException(status_code=404, detail="No matches found for this away team.")
    return {"matches": matches}

@app.get("/matches/team")
def search_by_team(team: str):
    response = es.search(
        index=INDEX_NAME,
        body={
            "query": {
                "bool": {
                    "should": [
                        {"match": {"home_team": team}},
                        {"match": {"away_team": team}}
                    ]
                }
            }
        }
    )
    matches = [hit["_source"] for hit in response["hits"]["hits"]]
    if not matches:
        raise HTTPException(status_code=404, detail="No matches found for this team.")
    return {"matches": matches}

@app.get("/matches/city")
def search_by_city(city: str):
    response = es.search(
        index=INDEX_NAME,
        body={"query": {"match": {"city": city}}}
    )
    matches = [hit["_source"] for hit in response["hits"]["hits"]]
    if not matches:
        raise HTTPException(status_code=404, detail="No matches found in this city.")
    return {"matches": matches}

@app.get("/matches/stadium")
def search_by_stadium(stadium: str):
    response = es.search(
        index=INDEX_NAME,
        body={"query": {"match": {"stadium": stadium}}}
    )
    matches = [hit["_source"] for hit in response["hits"]["hits"]]
    if not matches:
        raise HTTPException(status_code=404, detail="No matches found in this stadium.")
    return {"matches": matches}

@app.get("/matches/date")
def search_by_date(date: str):
    response = es.search(
        index=INDEX_NAME,
        body={"query": {"match": {"date": date}}}
    )
    matches = [hit["_source"] for hit in response["hits"]["hits"]]
    if not matches:
        raise HTTPException(status_code=404, detail="No matches found on this date.")
    return {"matches": matches}

@app.put("/matches/byID")
def update_match(match_id: int, updated_match: Match):
    if not es.exists(index=INDEX_NAME, id=match_id):
        raise HTTPException(status_code=404, detail="Match not found.")
    es.update(index=INDEX_NAME, id=match_id, doc=   {"doc": updated_match.dict()})
    return {"message": "Match updated successfully."}

@app.delete("/matches/byID")
def delete_match(match_id: int):
    if not es.exists(index=INDEX_NAME, id=match_id):
        raise HTTPException(status_code=404, detail="Match not found.")
    es.delete(index=INDEX_NAME, id=match_id)
    return {"message": "Match deleted successfully."}