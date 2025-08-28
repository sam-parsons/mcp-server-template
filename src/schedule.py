from .client import client

def get_nhl_daily_schedule(date: str = None) -> dict:
    """
    Get NHL schedule for a specific date.
    
    Args:
        date: Date in YYYY-MM-DD format. Defaults to today's date.
    
    Returns:
        dict: Game schedule data for the specified date or error message.
    """
    try:
        from datetime import datetime
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")  # Default to today's date
        else:
            # Parse and reformat the date to ensure YYYY-MM-DD
            date = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
        
        schedule_data = client.schedule.daily_schedule(date)
        return {"schedule": schedule_data}
    except ValueError as e:
        return {"error": f"Invalid date format: {str(e)}. Please use YYYY-MM-DD."}
    except Exception as e:
        return {"error": str(e)}

def get_nhl_weekly_schedule(date: str = None) -> dict:
    """
    Get NHL schedule for a week starting from the specified date.
    
    Args:
        date: Date in YYYY-MM-DD format. Defaults to today's date.
              Note: NHL's "today" typically shifts around 12:00 EST.
    
    Returns:
        dict: Weekly game schedule data or error message.
    """
    try:
        res = date if date else "now"
        schedule = client.schedule.weekly_schedule(res)
        return {"schedule": schedule}
    except Exception as e:
        return {"error": str(e)}

def get_nhl_team_monthly_schedule(team_abbr: str, month: str = None) -> dict:
    """
    Get monthly schedule for specified team or the given month.
    
    Args:
        team_abbr: Three-letter team abbreviation (e.g., BUF, TOR)
        month: Month in YYYY-MM format (e.g., 2021-10). Defaults to current month.
    
    Returns:
        dict: Monthly schedule data or error message.
    """
    try:
        games = client.schedule.team_monthly_schedule(team_abbr, month)
        return {"games": games, "team": team_abbr, "month": month}
    except Exception as e:
        return {"error": str(e)}

def get_nhl_team_weekly_schedule(team_abbr: str, date: str = None) -> dict:
    """
    Get weekly schedule for specified team.
    
    Args:
        team_abbr: Three-letter team abbreviation (e.g., BUF, TOR)
        date: Date in YYYY-MM-DD format. Gets schedule for week containing this date.
              Defaults to current week.
    
    Returns:
        dict: Weekly schedule data or error message.
    """
    try:
        games = client.schedule.team_weekly_schedule(team_abbr, date)
        return {"games": games, "team": team_abbr, "date": date}
    except Exception as e:
        return {"error": str(e)}

def get_nhl_team_season_schedule(team_abbr: str, season: str) -> dict:
    """
    Get full season schedule for specified team.
    
    Args:
        team_abbr: Three-letter team abbreviation (e.g., BUF, TOR)
        season: Season in YYYYYYYY format (e.g., 20232024)
    
    Returns:
        dict: Complete season schedule data including metadata or error message.
    """
    try:
        schedule = client.schedule.team_season_schedule(team_abbr, season)
        return {"schedule": schedule, "team": team_abbr, "season": season}
    except Exception as e:
        return {"error": str(e)}

def get_nhl_calendar_schedule(date: str) -> dict:
    """
    Get schedule in calendar format for specified date.
    
    Args:
        date: Date in YYYY-MM-DD format (e.g., 2023-11-23)
    
    Returns:
        dict: Calendar-formatted schedule data or error message.
    """
    try:
        schedule = client.schedule.calendar_schedule(date)
        return {"schedule": schedule, "date": date}
    except Exception as e:
        return {"error": str(e)}

def get_nhl_playoff_carousel(season: str) -> dict:
    """
    Get list of all series games up to current playoff round.
    
    Args:
        season: Season in YYYYYYYY format (e.g., "20232024")
    
    Returns:
        dict: Playoff series data for the specified season or error message.
    """
    try:
        playoff_data = client.schedule.playoff_carousel(season)
        return {"playoff_data": playoff_data, "season": season}
    except Exception as e:
        return {"error": str(e)}

def get_nhl_playoff_series_schedule(season: str, series: str) -> dict:
    """
    Get the schedule for a specified playoff series.
    
    Args:
        season: Season in YYYYYYYY format (e.g., "20232024")
        series: Series identifier (a-h) for Round 1
    
    Returns:
        dict: Schedule data for the specified playoff series or error message.
    """
    try:
        series_schedule = client.schedule.playoff_series_schedule(season, series)
        return {"series_schedule": series_schedule, "season": season, "series": series}
    except Exception as e:
        return {"error": str(e)}

def get_nhl_playoff_bracket(year: str) -> dict:
    """
    Get the playoff bracket.
    
    Args:
        year: Year playoffs take place (e.g., "2024")
    
    Returns:
        dict: Playoff bracket data or error message.
    """
    try:
        bracket = client.schedule.playoff_bracket(year)
        return {"bracket": bracket, "year": year}
    except Exception as e:
        return {"error": str(e)}
