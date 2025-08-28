from .client import client

def get_nhl_teams(date: str = "now") -> dict:
    """
    Get all NHL teams with conference, division, and franchise information.
    
    Args:
        date: Date in format YYYY-MM-DD. Defaults to "now".
            Note: During preseason, "now" may default to last year's season.
            For accurate current season teams, supply a date at season start.
            Examples: "2024-04-18" for 2023-2024, "2024-10-04" for 2024-2025
    
    Returns:
        dict: All NHL teams with their information.
    """
    try:
        teams = client.teams.teams(date)
        return {"teams": teams}
    except Exception as e:
        return {"error": str(e)}

def get_nhl_team_roster(team_abbr: str, season: str) -> dict:
    """
    Get the roster for a specific NHL team and season.
    
    Args:
        team_abbr: Team abbreviation (e.g., BUF, TOR, BOS)
        season: Season in format YYYYYYYY (e.g., 20232024, 20242025)
        
    Returns:
        dict: Team roster or error message.
    """
    try:
        roster = client.teams.team_roster(team_abbr, season)
        return {"roster": roster}
    except Exception as e:
        return {"error": str(e)}

def get_nhl_franchises() -> dict:
    """
    Get a list of all past and current NHL franchises.
    
    Returns:
        dict: All NHL franchises including historical/defunct teams.
    """
    try:
        franchises = client.teams.franchises()
        return {"franchises": franchises}
    except Exception as e:
        return {"error": str(e)}

def get_nhl_team_ids(date: str = "now") -> dict:
    """
    Get a mapping of NHL team names to their abbreviations for reference.
    
    Args:
        date: Date in format YYYY-MM-DD. Defaults to "now".
            Note: During preseason, "now" may default to last year's season.
            For accurate current season teams, supply a date at season start.
    
    Returns:
        dict: Dictionary mapping team names to abbreviations or error message.
    """
    try:
        teams = client.teams.teams(date)
        team_mapping = {team.get('name', 'Unknown'): team.get('abbr', 'Unknown') for team in teams}
        return {"team_abbreviations": team_mapping}
    except Exception as e:
        return {"error": str(e)}
