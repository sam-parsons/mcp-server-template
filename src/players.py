from .client import client

def get_nhl_prospects_by_team(team_abbr: str) -> dict:
    """
    Get prospects for a specific NHL team.
    
    Args:
        team_abbr: Team abbreviation (e.g., BUF, TOR, BOS)
        
    Returns:
        dict: Prospects data for the specified team or error message.
    """
    try:
        prospects = client.players.prospects_by_team(team_abbr)
        return {"prospects": prospects}
    except Exception as e:
        return {"error": str(e)}

def get_nhl_players_by_team(team_abbr: str, season: str) -> dict:
    """
    Get the roster/players for the given team and season.
    
    This method provides the same functionality as get_nhl_team_roster(),
    offering a convenient way to access team rosters through the Players API.
    
    Args:
        team_abbr: Team abbreviation (e.g., BUF, TOR, BOS)
        season: Season in format YYYYYYYY (e.g., 20232024, 20242025)
        
    Returns:
        dict: Dictionary containing roster information for the specified team and season or error message.
    """
    try:
        players = client.players.players_by_team(team_abbr, season)
        return {"players": players}
    except Exception as e:
        return {"error": str(e)}
