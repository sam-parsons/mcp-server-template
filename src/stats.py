from .client import client

def get_nhl_gametypes_per_season_by_team(team_abbr: str) -> dict:
    """
    Gets all game types played by a team throughout their history.
    
    Args:
        team_abbr (str): The 3 letter abbreviation of the team (e.g., BUF, TOR)
        
    Returns:
        dict: A mapping of seasons to game types played by the team or error message.
    """
    try:
        data = client.stats.gametypes_per_season_directory_by_team(team_abbr)
        return {"gametypes": data}
    except Exception as e:
        return {"error": str(e)}

def get_nhl_player_career_stats(player_id: str) -> dict:
    """
    Gets a player's career statistics and biographical information.
    
    Args:
        player_id (str): The unique identifier for the NHL player
        
    Returns:
        dict: A dictionary containing the player's career statistics and personal information or error message.
    """
    try:
        data = client.stats.player_career_stats(player_id)
        return {"player_stats": data}
    except Exception as e:
        return {"error": str(e)}

def get_nhl_player_game_log(player_id: str, season_id: str, game_type: int) -> dict:
    """
    Gets a player's game log for a specific season and game type.
    
    Args:
        player_id (str): The unique identifier for the NHL player
        season_id (str): The season identifier in YYYYYYYY format (e.g., "20222023", "20232024")
        game_type (int): The type of games to retrieve:
            1: Preseason
            2: Regular season
            3: Playoffs
            
    Returns:
        dict: A dictionary containing the player's game-by-game statistics or error message.
    """
    try:
        data = client.stats.player_game_log(player_id, season_id, game_type)
        return {"game_log": data}
    except Exception as e:
        return {"error": str(e)}

def get_nhl_team_summary_stats(start_season: str, end_season: str, game_type_id: int = 2, 
                               is_game: bool = False, is_aggregate: bool = False, 
                               start: int = 0, limit: int = 50) -> dict:
    """
    Retrieves team summary statistics across one or more seasons.
    
    Args:
        start_season (str): Beginning of season range in YYYYYYYY format (e.g., "20202021")
        end_season (str): End of season range in YYYYYYYY format (e.g., "20212022")
        game_type_id (int, optional): Type of games to include:
            2: Regular season (default)
            3: Playoffs
            1: Preseason
        is_game (bool, optional): Defaults False
        is_aggregate (bool, optional): Defaults False. Whether to aggregate the statistics
        start (int, optional): Starting index for pagination. Defaults to 0
        limit (int, optional): Maximum number of results to return. Defaults to 50
        
    Returns:
        dict: List of dictionaries containing team summary statistics or error message.
    """
    try:
        data = client.stats.team_summary(
            start_season=start_season,
            end_season=end_season,
            game_type_id=game_type_id,
            is_game=is_game,
            is_aggregate=is_aggregate,
            start=start,
            limit=limit
        )
        return {"team_summary": data}
    except Exception as e:
        return {"error": str(e)}

def get_nhl_skater_stats_summary(start_season: str, end_season: str, franchise_id: str = None,
                                 game_type_id: int = 2, aggregate: bool = False,
                                 start: int = 0, limit: int = 25) -> dict:
    """
    Gets simplified skater statistics summary for specified seasons and franchises.
    
    Args:
        start_season (str): Beginning of season range in YYYYYYYY format (e.g., "20202021")
        end_season (str): End of season range in YYYYYYYY format
        franchise_id (str, optional): Franchise identifier specific to /stats APIs
        game_type_id (int, optional): Type of games to include:
            2: Regular season (Default)
            3: Playoffs
            1: Preseason
        aggregate (bool, optional): When True, combines multiple seasons' data per player
        start (int, optional): Starting index for pagination
        limit (int, optional): Maximum number of results to return. Defaults to 25
        
    Returns:
        dict: List of dictionaries containing skater statistics or error message.
    """
    try:
        data = client.stats.skater_stats_summary(
            start_season=start_season,
            end_season=end_season,
            franchise_id=franchise_id,
            game_type_id=game_type_id,
            aggregate=aggregate,
            start=start,
            limit=limit
        )
        return {"skater_stats": data}
    except Exception as e:
        return {"error": str(e)}

def get_nhl_goalie_stats_summary(start_season: str, end_season: str = None,
                                 stats_type: str = "summary", game_type_id: int = 2,
                                 franchise_id: str = None, aggregate: bool = False,
                                 start: int = 0, limit: int = 25) -> dict:
    """
    Retrieves goalie statistics with various filtering and aggregation options.
    
    Args:
        start_season (str): Beginning of season range in YYYYYYYY format (e.g., "20202021")
        end_season (str, optional): End of season range in YYYYYYYY format. Defaults to start_season
        stats_type (str): Type of statistics to retrieve:
            'summary', 'advanced', 'bios', 'daysrest', 'penaltyShots',
            'savesByStrength', 'shootout', 'startedVsRelieved'
        game_type_id (int, optional): Type of games to include:
            2: Regular season
            3: Playoffs
            1: Preseason
        franchise_id (str, optional): Franchise identifier to filter results
        aggregate (bool, optional): When True, combines multiple seasons' data per goalie
        start (int, optional): Starting index for pagination
        limit (int, optional): Maximum number of results to return. Defaults to 25
        
    Returns:
        dict: Dictionary containing goalie statistics or error message.
    """
    try:
        data = client.stats.goalie_stats_summary(
            start_season=start_season,
            end_season=end_season,
            stats_type=stats_type,
            game_type_id=game_type_id,
            franchise_id=franchise_id,
            aggregate=aggregate,
            start=start,
            limit=limit
        )
        return {"goalie_stats": data}
    except Exception as e:
        return {"error": str(e)}
