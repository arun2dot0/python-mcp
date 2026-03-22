## MCP Server
MCP server that provides integration for
getting all the person information 

Also itegration to get details from Rag for blog search
There are multiple test scenarios . Tested with the streaming version


# Python version requirement
python>=3.10

# MCP Python client library for SSE transport
mcp

# Pydantic AI for OpenAI agent integration and MCP toolsets
pydantic-ai-slim[mcp]

# HTTP client and SSE support
httpx[sse]


# setup local environment

python3 -m venv myenv
uv venv myenv -p 3.11
source myenv/bin/activate 
uv add openai-agents
pip install "uvicorn[standard]"

uv pip install -r requirements.txt


# Debug what is in the port
sudo lsof -i :8000


# Using mcp with streaming option - Tested
Local run 
 uv run server.py

Server run 
nohup uvicorn server:app --reload --log-level error --host 0.0.0.0 --port 8080 &
