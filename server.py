from fastmcp import FastMCP
import json
from pathlib import Path
from typing import Any
import requests
from typing import List, Dict

mcp = FastMCP("Fun-MCP Server")

# Load person data from JSON file once at server start

# Define person_data at module level to be accessible by tool functions
person_file = Path(__file__).parent / "data" / "persons.json"
with open(person_file, "r") as f:
    person_data = json.load(f)

@mcp.tool(name="person-info", description="Default - Find information about Arun")
def find_person() -> dict:
    # Use the module-level variable here
    return person_data

if __name__ == "__main__":
    # mcp.run(transport="streamable-http", port=8001)
    mcp.run(transport="stdio")