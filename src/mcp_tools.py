from .teams import *
from .players import *
from .schedule import *
from .standings import *
from .stats import *

def setup_nhl_tools(mcp):
    """Setup NHL tools for the MCP server"""
    
    @mcp.tool()
    def get_nhl_teams_mcp(date: str = "now") -> dict:
        return get_nhl_teams(date)

    @mcp.tool()
    def get_nhl_team_roster_mcp(team_abbr: str, season: str) -> dict:
        return get_nhl_team_roster(team_abbr, season)

    @mcp.tool()
    def get_nhl_prospects_by_team_mcp(team_abbr: str) -> dict:
        return get_nhl_prospects_by_team(team_abbr)

    @mcp.tool()
    def get_nhl_players_by_team_mcp(team_abbr: str, season: str) -> dict:
        return get_nhl_players_by_team(team_abbr, season)

    @mcp.tool()
    def get_nhl_franchises_mcp() -> dict:
        return get_nhl_franchises()

    @mcp.tool()
    def get_nhl_team_ids_mcp() -> dict:
        return get_nhl_team_ids()

    @mcp.tool()
    def get_nhl_standings_mcp(date: str = "now", season: str = None) -> dict:
        return get_nhl_standings(date, season)

    @mcp.tool()
    def get_nhl_season_manifest_mcp() -> dict:
        return get_nhl_season_manifest()

    @mcp.tool()
    def get_nhl_daily_schedule_mcp(date: str = None) -> dict:
        return get_nhl_daily_schedule(date)

    @mcp.tool()
    def get_nhl_weekly_schedule_mcp(date: str = None) -> dict:
        return get_nhl_weekly_schedule(date)

    @mcp.tool()
    def get_nhl_team_monthly_schedule_mcp(team_abbr: str, month: str = None) -> dict:
        return get_nhl_team_monthly_schedule(team_abbr, month)

    @mcp.tool()
    def get_nhl_team_weekly_schedule_mcp(team_abbr: str, date: str = None) -> dict:
        return get_nhl_team_weekly_schedule(team_abbr, date)

    @mcp.tool()
    def get_nhl_team_season_schedule_mcp(team_abbr: str, season: str) -> dict:
        return get_nhl_team_season_schedule(team_abbr, season)

    @mcp.tool()
    def get_nhl_calendar_schedule_mcp(date: str) -> dict:
        return get_nhl_calendar_schedule(date)

    @mcp.tool()
    def get_nhl_playoff_carousel_mcp(season: str) -> dict:
        return get_nhl_playoff_carousel(season)

    @mcp.tool()
    def get_nhl_playoff_series_schedule_mcp(season: str, series: str) -> dict:
        return get_nhl_playoff_series_schedule(season, series)

    @mcp.tool()
    def get_nhl_playoff_bracket_mcp(year: str) -> dict:
        return get_nhl_playoff_bracket(year)

    # Stats API MCP Tools
    @mcp.tool()
    def get_nhl_gametypes_per_season_by_team_mcp(team_abbr: str) -> dict:
        return get_nhl_gametypes_per_season_by_team(team_abbr)

    @mcp.tool()
    def get_nhl_player_career_stats_mcp(player_id: str) -> dict:
        return get_nhl_player_career_stats(player_id)

    @mcp.tool()
    def get_nhl_player_game_log_mcp(player_id: str, season_id: str, game_type: int) -> dict:
        return get_nhl_player_game_log(player_id, season_id, game_type)

    @mcp.tool()
    def get_nhl_team_summary_stats_mcp(start_season: str, end_season: str, game_type_id: int = 2,
                                       is_game: bool = False, is_aggregate: bool = False,
                                       start: int = 0, limit: int = 50) -> dict:
        return get_nhl_team_summary_stats(start_season, end_season, game_type_id, is_game, 
                                        is_aggregate, start, limit)

    @mcp.tool()
    def get_nhl_skater_stats_summary_mcp(start_season: str, end_season: str, franchise_id: str = None,
                                         game_type_id: int = 2, aggregate: bool = False,
                                         start: int = 0, limit: int = 25) -> dict:
        return get_nhl_skater_stats_summary(start_season, end_season, franchise_id, game_type_id,
                                          aggregate, start, limit)

    @mcp.tool()
    def get_nhl_goalie_stats_summary_mcp(start_season: str, end_season: str = None,
                                         stats_type: str = "summary", game_type_id: int = 2,
                                         franchise_id: str = None, aggregate: bool = False,
                                         start: int = 0, limit: int = 25) -> dict:
        return get_nhl_goalie_stats_summary(start_season, end_season, stats_type, game_type_id,
                                          franchise_id, aggregate, start, limit)
