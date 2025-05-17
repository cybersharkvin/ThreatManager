"""FastAPI backend for MCP UI."""

from fastapi import FastAPI

app = FastAPI(title="MCP Backend")

@app.get("/healthz")
async def health_check():
    return {"status": "ok"}

# TODO: Add session and audit trail endpoints
