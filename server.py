import json
from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

app = FastAPI()

mcp = FastMCP("Infojini Staffing MCP")

with open("candidates.json") as f:
    candidates = json.load(f)


# MCP TOOL: search candidates
@mcp.tool()
def search_candidates(skill: str):
    result = []

    for c in candidates:
        if skill.lower() in [s.lower() for s in c["skills"]]:
            result.append(c)

    return result


# MCP TOOL: candidate summary
@mcp.tool()
def candidate_summary(name: str):

    for c in candidates:
        if c["name"].lower() == name.lower():
            return c

    return "Candidate not found"


# MCP TOOL: list candidates
@mcp.tool()
def available_candidates():
    return candidates


# REST API (for Copilot Studio)
@app.get("/candidates")
def get_candidates(skill: str):

    result = []

    for c in candidates:
        if skill.lower() in [s.lower() for s in c["skills"]]:
            result.append(c)

    return result


# Run MCP server
if __name__ == "__main__":
    mcp.run(transport="http", port=8080)
