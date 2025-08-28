"""
Example MCP tool demonstrating how to create a simple tool.
This shows the basic structure for implementing MCP tools.
"""

from typing import Dict, Any


def get_square(number: float) -> Dict[str, Any]:
    """
    Calculate the square of a number.
    
    Args:
        number: The number to square
    
    Returns:
        Dictionary containing the result
    """
    try:
        result = number ** 2
        
        return {
            "success": True,
            "number": number,
            "square": result
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "number": number
        }
