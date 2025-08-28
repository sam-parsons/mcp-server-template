# 🏒 NHL API MCP Server

[![CI](https://github.com/sam-parsons/nhl-api-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/sam-parsons/nhl-api-mcp/actions/workflows/ci.yml)
[![Docker Hub](https://img.shields.io/docker/pulls/samparsons269/nhl-api-mcp.svg)](https://hub.docker.com/r/samparsons269/nhl-api-mcp)
[![Docker Image Size](https://img.shields.io/docker/image-size/samparsons269/nhl-api-mcp/latest)](https://hub.docker.com/r/samparsons269/nhl-api-mcp)

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that provides comprehensive access to NHL statistics, game data, and hockey analytics through a FastMCP-based interface.

## 🏒 Overview

This MCP server acts as a bridge between AI applications and NHL data sources, enabling seamless integration of hockey statistics, team information, player data, game schedules, and performance analytics into AI workflows and applications.

## ✨ Features

### 🏒 NHL Data Access
- **Team Information**: Complete team rosters, prospects, and franchise details across all NHL teams
- **Game Schedules**: Daily, weekly, monthly, and season-long schedules for teams and leagues
- **Player Statistics**: Comprehensive career stats, game logs, and performance metrics
- **Standings & Rankings**: Current and historical league standings with flexible filtering
- **Playoff Data**: Tournament brackets, series schedules, and championship history

### 🔧 MCP Tools

All NHL/statistics/game/player/team/etc. functionality is exposed as MCP tools, not as RESTful HTTP endpoints. These tools are accessible via the `/mcp/` endpoint using the MCP protocol. For a list of available tools and their descriptions, visit `/tools/` when the server is running.

#### Key MCP Tools
- `get_nhl_player_career_stats` - Comprehensive player career statistics
- `get_nhl_player_game_log` - Game-by-game performance data
- `get_nhl_goalie_stats_summary` - Goalie performance metrics

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

<!-- ### Installing via Smithery

To install NHL API Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@sam-parsons/nhl-api-mcp):

```bash
npx -y @smithery/cli install @sam-parsons/nhl-api-mcp --client claude
``` -->

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/sam-parsons/nhl-api-mcp.git
cd nhl-api-mcp
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
git clone https://github.com/sam-parsons/nhl-api-mcp.git
cd nhl-api-mcp
```

2. Build the Docker image:
```bash
docker build -t nhl-api-mcp .
```

3. Run the container (default timezone is UTC, uses Python 3.12):
```bash
docker run -p 8000:8000 nhl-api-mcp
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📄 License

This project is open source. Please check the license file for details.
