from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
import json
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

ideas = []
if os.path.exists("ideas.json"):
    with open("ideas.json", "r") as f:
        ideas = json.load(f)

@app.get("/")
async def read_root():
    return {"message": "Welcome to Mindforge Idea Tracker"}

@app.get("/api/ideas")
async def list_ideas():
    return ideas

@app.post("/api/ideas")
async def add_idea(title: str, description: str):
    idea = {"id": len(ideas) + 1, "title": title, "description": description}
    ideas.append(idea)
    with open("ideas.json", "w") as f:
        json.dump(ideas, f)
    return idea

@app.delete("/api/ideas/{id}")
async def delete_idea(id: int):
    global ideas
    ideas = [i for i in ideas if i["id"] != id]
    with open("ideas.json", "w") as f:
        json.dump(ideas, f)
    return {"message": "Idea deleted"}

@app.get("/api/ideas/search")
async def search_ideas(q: str):
    return [i for i in ideas if q.lower() in i["title"].lower() or q.lower() in i["description"].lower()]