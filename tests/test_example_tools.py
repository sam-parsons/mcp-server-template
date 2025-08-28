import pytest
from unittest.mock import Mock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.tools import get_square


class TestExampleTools:
    
    def test_get_square(self):
        """Test that square tool returns expected result"""
        result = get_square(5)
        
        assert result["success"] is True
        assert result["number"] == 5
        assert result["square"] == 25


class TestMCPToolsSetup:
    
    def test_setup_mcp_tools_registers_tool(self):
        """Test that the square tool is properly registered with MCP"""
        from src.mcp_tools import setup_mcp_tools
        
        mock_mcp = Mock()
        setup_mcp_tools(mock_mcp)
        
        # Should register 1 tool
        assert mock_mcp.tool.call_count == 1


if __name__ == "__main__":
    pytest.main([__file__])
