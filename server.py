from mcp.server.fastmcp import FastMCP
import json
import random
import os

mcp = FastMCP("Recruitment MCP Server")

# Load data
with open("candidates.json") as f:
    candidates = json.load(f)

with open("questionnaire.json") as f:
    questions = json.load(f)


@mcp.tool()
def search_candidates(skill: str):
    """
    Search candidates by skill
    """
    results = []

    for c in candidates:
        if skill.lower() in [s.lower() for s in c["skills"]]:
            results.append(c)

    return results


@mcp.tool()
def candidate_summary(name: str):
    """
    Get summary of a candidate by name
    """
    for c in candidates:
        if c["name"].lower() == name.lower():
            return c

    return {"message": "Candidate not found"}


@mcp.tool()
def list_candidates():
    """
    Return all available candidates
    """
    return candidates


@mcp.tool()
def screening_questions(skill: str, count: int = 3):
    """
    Return random screening questions for a skill
    """

    if skill not in questions:
        return {"message": "Skill not found"}

    return random.sample(questions[skill], min(count, len(questions[skill])))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print(f"Starting MCP server on port {port}")

    mcp.run(
        transport="sse",
        host="0.0.0.0",
        port=port
    )
