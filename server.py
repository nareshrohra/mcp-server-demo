from fastapi import FastAPI
import json

app = FastAPI(title="Infojini MCP Demo")

with open("candidates.json") as f:
    candidates = json.load(f)


@app.get("/")
def home():
    return {"message": "MCP Demo Server Running"}


@app.get("/candidates")
def search_candidates(skill: str):
    results = []

    for c in candidates:
        if skill.lower() in [s.lower() for s in c["skills"]]:
            results.append(c)

    return results


@app.get("/candidate")
def candidate_summary(name: str):

    for c in candidates:
        if c["name"].lower() == name.lower():
            return c

    return {"message": "Candidate not found"}


@app.get("/all_candidates")
def available_candidates():
    return candidates
