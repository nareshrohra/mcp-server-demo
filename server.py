from fastapi import FastAPI
import json
import random

app = FastAPI(title="MCP Demo")

# Load candidates
with open("candidates.json") as f:
    candidates = json.load(f)

# Load questionnaire
with open("questionnaire.json") as f:
    questionnaire = json.load(f)


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


@app.get("/screening_questions")
def get_questions(skill: str, count: int = 3):

    skill = skill.lower()

    if skill not in questionnaire:
        return {"message": "Skill not found"}

    questions = questionnaire[skill]

    sample = random.sample(questions, min(count, len(questions)))

    return {
        "skill": skill,
        "questions": sample
    }
