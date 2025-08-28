import argparse
import os
import warnings

import uvicorn
from fastmcp import FastMCP
from starlette.responses import HTMLResponse, JSONResponse, RedirectResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware

from src import setup_mcp_tools

# Suppress websockets deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="websockets")
warnings.filterwarnings("ignore", category=DeprecationWarning, module="uvicorn.protocols.websockets")

mcp = FastMCP("MCP Server Template")

# Register the example tool
setup_mcp_tools(mcp)

@mcp.custom_route("/", methods=["GET"])
async def root(request):
    return RedirectResponse(url="/docs")

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request):
    return JSONResponse({"status": "ok"})

@mcp.custom_route("/info", methods=["GET"])
async def mcp_info(request):
    tools_list = await mcp.get_tools()
    return JSONResponse(
        {
            "status": "running",
            "protocol": "mcp",
            "server_name": "MCP Server Template",
            "description": "Template for building custom Model Context Protocol servers",
            "mcp_endpoint": "/mcp",
            "tools_available": len(tools_list),
            "note": "This is an MCP server template. Customize the tools in src/tools.py",
        }
    )

@mcp.custom_route("/tools", methods=["GET"])
async def list_tools(request):
    tools = []
    tools_list = await mcp.get_tools()
    for tool_name, tool in tools_list.items():
        tools.append(
            {
                "name": tool_name,
                "description": getattr(tool, "description", None) or "No description available",
                "parameters": getattr(tool, "parameters", None) or {},
            }
        )
    return JSONResponse({"tools": tools})

@mcp.custom_route("/docs", methods=["GET"])
async def docs(request):
    tools_list = await mcp.get_tools()
    docs_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>MCP Server Template Documentation</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .endpoint {{ margin: 20px 0; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }}
            .method {{ font-weight: bold; color: #0066cc; }}
            .path {{ font-weight: bold; color: #cc6600; }}
            .tools {{ margin: 10px 0; }}
            .tool {{ margin: 5px 0; padding: 10px; background: #f5f5f5; border-radius: 3px; }}
        </style>
    </head>
    <body>
        <h1>MCP Server Template Documentation</h1>
        <p>Template for building custom Model Context Protocol servers.</p>

        <h2>Available Endpoints</h2>
        <div class="endpoint"><span class="method">GET</span> <span class="path">/health</span><p>Health check</p></div>
        <div class="endpoint"><span class="method">GET</span> <span class="path">/info</span><p>Server info</p></div>
        <div class="endpoint"><span class="method">GET</span> <span class="path">/tools</span><p>List MCP tools</p></div>
        <div class="endpoint"><span class="method">POST</span> <span class="path">/mcp</span><p>MCP protocol endpoint</p></div>

        <h2>Available MCP Tools ({len(tools_list)} total)</h2>
        <div class="tools">
    """
    for tool_name, tool in tools_list.items():
        description = getattr(tool, "description", None) or "No description available"
        docs_html += f'<div class="tool"><strong>{tool_name}</strong>: {description}</div>'
    docs_html += """
        </div>
        <h2>Usage</h2>
        <p>This server implements the Model Context Protocol (MCP). Customize the tools in src/tools.py to build your own MCP server.</p>
        
        <h2>Getting Started</h2>
        <p>1. Edit src/tools.py to add your own tools</p>
        <p>2. Update the server name and description in main.py</p>
        <p>3. Run with: python main.py --http</p>
        <p>4. Test with: pytest</p>
    </body>
    </html>
    """
    return HTMLResponse(content=docs_html)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server Template")
    parser.add_argument("--http", action="store_true", help="Run server with HTTP transport (default: stdio)")
    parser.add_argument("--port", "-p", type=int, default=8000, help="Port to run the server on (env PORT overrides)")
    args = parser.parse_args()

    if args.http:
        port = int(os.environ.get("PORT", args.port))
        cors_middleware = Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["GET", "POST", "OPTIONS"],
            allow_headers=["*"],
            expose_headers=["mcp-session-id"],
            max_age=86400,
        )
        app = mcp.http_app(middleware=[cors_middleware])

        uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
    else:
        mcp.run(transport="stdio")
