from .client import client

def get_nhl_standings(date: str = "now", season: str = None) -> dict:
    """
    Get NHL league standings for a specified season or date.
    
    Retrieves NHL standings either for a specific date or for the end of a season.
    If both parameters are provided, season takes precedence.
    
    Args:
        date: Date in YYYY-MM-DD format. Defaults to current date.
        season: Season identifier to get final standings (e.g., 20232024, 20242025).
               Takes precedence over date parameter if both are provided.
    
    Returns:
        dict: League standings data or error message.
    """
    try:
        # If season is provided, we need to look up the last date of the season
        if season:
            seasons_response = get_nhl_season_manifest()
            if "error" in seasons_response:
                return seasons_response
            seasons = seasons_response.get("seasons", [])
            season_data = next((s for s in seasons if s.get("id") == int(season)), None)
            if not season_data:
                raise ValueError(f"Invalid Season Id {season}")
            date = season_data.get("standingsEnd")
        
        res = date if date else "now"
        standings = client.standings.league_standings(res)
        return {"standings": standings}
    except Exception as e:
        return {"error": str(e)}

def get_nhl_season_manifest() -> dict:
    """
    Get metadata for all NHL seasons.
    
    Returns information about every season including start/end dates, 
    conference/division usage, and scoring rules.
    
    Returns:
        dict: Season metadata or error message.
        
    Example response format:
    [{
        "id": 20232024,
        "conferencesInUse": true,
        "divisionsInUse": true,
        "pointForOTlossInUse": true,
        "regulationWinsInUse": true,
        "rowInUse": true,
        "standingsEnd": "2023-11-10",
        "standingsStart": "2023-10-10",
        "tiesInUse": false,
        "wildcardInUse": true
    }]
    """
    try:
        seasons = client.standings.season_standing_manifest()
        return {"seasons": seasons}
    except Exception as e:
        return {"error": str(e)}
