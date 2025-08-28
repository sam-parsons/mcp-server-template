from .client import client
from .teams import *
from .players import *
from .schedule import *
from .standings import *
from .stats import *
from .mcp_tools import setup_nhl_tools

# Re-export the client and setup function for convenience
__all__ = [
    'client',
    'setup_nhl_tools',
    # Teams
    'get_nhl_teams',
    'get_nhl_team_roster', 
    'get_nhl_franchises',
    'get_nhl_team_ids',
    # Players
    'get_nhl_prospects_by_team',
    'get_nhl_players_by_team',
    # Schedule
    'get_nhl_daily_schedule',
    'get_nhl_weekly_schedule',
    'get_nhl_team_monthly_schedule',
    'get_nhl_team_weekly_schedule',
    'get_nhl_team_season_schedule',
    'get_nhl_calendar_schedule',
    'get_nhl_playoff_carousel',
    'get_nhl_playoff_series_schedule',
    'get_nhl_playoff_bracket',
    # Standings
    'get_nhl_standings',
    'get_nhl_season_manifest',
    # Stats
    'get_nhl_gametypes_per_season_by_team',
    'get_nhl_player_career_stats',
    'get_nhl_player_game_log',
    'get_nhl_team_summary_stats',
    'get_nhl_skater_stats_summary',
    'get_nhl_goalie_stats_summary',
]
