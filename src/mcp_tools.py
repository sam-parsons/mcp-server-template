"""
MCP tools setup for the template server.
This module registers the example MCP tool with the FastMCP instance.
"""

from .tools import get_square


def setup_mcp_tools(mcp):
    """Setup MCP tools for the server"""
    
    @mcp.tool()
    def get_square_mcp(number: float) -> dict:
        """Calculate the square of a number"""
        return get_square(number)
