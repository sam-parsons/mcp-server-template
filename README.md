# 🚀 MCP Server Template

[![CI](https://github.com/sam-parsons/mcp-server-template/actions/workflows/ci.yml/badge.svg)](https://github.com/sam-parsons/mcp-server-template/actions/workflows/ci.yml)
[![Docker Hub](https://img.shields.io/docker/pulls/samparsons269/mcp-server-template.svg)](https://hub.docker.com/r/samparsons269/mcp-server-template)
[![Docker Image Size](https://img.shields.io/docker/image-size/samparsons269/mcp-server-template/latest)](https://hub.docker.com/r/samparsons269/mcp-server-template)

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server template that provides a clean, well-structured foundation for building custom MCP servers with FastMCP.

## 🎯 Overview

This template serves as a starting point for developers who want to create their own MCP servers. It includes a complete project structure with example tools, testing setup, and deployment configurations, making it easy to get started with MCP development.

## ✨ Features

### 🏗️ Project Structure
- **Clean Architecture**: Well-organized module structure for easy expansion
- **Example Tools**: Sample MCP tools demonstrating best practices
- **Testing Setup**: Complete test infrastructure with pytest
- **Docker Support**: Ready-to-use containerization
- **Development Tools**: Pre-configured linting and formatting

### 🔧 MCP Tools

The template includes example tools that demonstrate how to create and register MCP tools:

#### Example Tools
- `get_weather` - Get current weather for a location
- `calculate_math` - Perform mathematical calculations
- `get_time` - Get current time in various formats
- `search_web` - Search the web for information

For the full list and detailed descriptions, see `/tools/` or `/docs` when the server is running.

### 🌐 HTTP Endpoints

The following HTTP endpoints are available:
- `/` - Redirects to `/docs`
- `/docs` - Interactive API documentation and tool listing
- `/health/` - Health check endpoint
- `/mcp/info` - MCP server information
- `/tools/` - List of all available MCP tools
- `/mcp/` (POST) - MCP protocol endpoint for MCP-compatible clients

## 📦 Installation

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/sam-parsons/mcp-server-template.git
cd mcp-server-template
```

2. Create and activate a virtual environment:

```bash
uv venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
uv pip install -e .
```

### Docker Installation

1. Clone the repository:
```bash
git clone https://github.com/sam-parsons/mcp-server-template.git
cd mcp-server-template
```

2. Build the Docker image:
```bash
docker build -t mcp-server-template .
```

3. Run the container (default timezone is UTC, uses Python 3.12):
```bash
docker run -p 8000:8000 mcp-server-template
```

## 🧪 Testing

Run tests with a simple command:
```bash
pytest
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📄 License

This project is open source. Please check the license file for details.
