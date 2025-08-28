import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import setup_nhl_tools, client


class TestNHLAPI:
    
    def test_client_initialization(self):
        assert client is not None
        assert hasattr(client, 'teams')
        assert hasattr(client, 'standings')
        assert hasattr(client, 'schedule')
    
    def test_get_nhl_teams_success(self, mock_teams):
        mock_teams.teams.return_value = [
            {
                "name": "Boston Bruins",
                "abbr": "BOS",
                "conference": {"abbr": "EAST", "name": "Eastern"},
                "division": {"abbr": "ATL", "name": "Atlantic"}
            },
            {
                "name": "Toronto Maple Leafs",
                "abbr": "TOR",
                "conference": {"abbr": "EAST", "name": "Eastern"},
                "division": {"abbr": "ATL", "name": "Atlantic"}
            }
        ]
        
        from src import get_nhl_teams
        result = get_nhl_teams()
        
        assert "teams" in result
        assert len(result["teams"]) == 2
        assert result["teams"][0]["name"] == "Boston Bruins"
        assert result["teams"][0]["abbr"] == "BOS"
        assert result["teams"][1]["conference"]["abbr"] == "EAST"
        
        mock_teams.teams.assert_called_once_with("now")
    
    def test_get_nhl_teams_with_date(self, mock_teams):
        mock_teams.teams.return_value = [
            {
                "name": "Boston Bruins",
                "abbr": "BOS",
                "conference": {"abbr": "EAST", "name": "Eastern"}
            }
        ]
        
        from src import get_nhl_teams
        result = get_nhl_teams(date="2024-10-04")
        
        assert "teams" in result
        assert len(result["teams"]) == 1
        
        mock_teams.teams.assert_called_once_with("2024-10-04")
    
    def test_get_nhl_teams_error(self, mock_teams):
        mock_teams.teams.side_effect = Exception("API Error")
        
        from src import get_nhl_teams
        result = get_nhl_teams()
        
        assert "error" in result
        assert result["error"] == "API Error"
    
    def test_get_nhl_team_roster_success(self, mock_teams):
        mock_teams.team_roster.return_value = {
            "roster": [
                {"id": 1, "name": "Jack Hughes", "position": "C", "number": "86"},
                {"id": 2, "name": "Nico Hischier", "position": "C", "number": "13"}
            ]
        }
        
        from src import get_nhl_team_roster
        result = get_nhl_team_roster(team_abbr="NJD", season="20232024")
        
        assert "roster" in result
        assert "roster" in result["roster"]
        assert len(result["roster"]["roster"]) == 2
        assert result["roster"]["roster"][0]["name"] == "Jack Hughes"
        assert result["roster"]["roster"][1]["position"] == "C"
        
        mock_teams.team_roster.assert_called_once_with("NJD", "20232024")
    
    def test_get_nhl_team_roster_error(self, mock_teams):
        mock_teams.team_roster.side_effect = Exception("Team not found")
        
        from src import get_nhl_team_roster
        result = get_nhl_team_roster(team_abbr="INVALID", season="20232024")
        
        assert "error" in result
        assert result["error"] == "Team not found"
    
    def test_get_nhl_prospects_by_team_success(self, mock_players):
        mock_players.prospects_by_team.return_value = {
            "prospects": [
                {"id": 1, "name": "Connor Bedard", "position": "C", "draftYear": 2023},
                {"id": 2, "name": "Adam Fantilli", "position": "C", "draftYear": 2023}
            ]
        }
        
        from src import get_nhl_prospects_by_team
        result = get_nhl_prospects_by_team(team_abbr="CHI")
        
        assert "prospects" in result
        assert "prospects" in result["prospects"]
        assert len(result["prospects"]["prospects"]) == 2
        assert result["prospects"]["prospects"][0]["name"] == "Connor Bedard"
        assert result["prospects"]["prospects"][1]["position"] == "C"
        
        mock_players.prospects_by_team.assert_called_once_with("CHI")
    
    def test_get_nhl_prospects_by_team_error(self, mock_players):
        mock_players.prospects_by_team.side_effect = Exception("Prospects API error")
        
        from src import get_nhl_prospects_by_team
        result = get_nhl_prospects_by_team(team_abbr="INVALID")
        
        assert "error" in result
        assert result["error"] == "Prospects API error"
    
    def test_get_nhl_players_by_team_success(self, mock_players):
        mock_players.players_by_team.return_value = {
            "roster": [
                {"id": 1, "name": "Jack Hughes", "position": "C", "number": "86"},
                {"id": 2, "name": "Nico Hischier", "position": "C", "number": "13"}
            ]
        }
        
        from src import get_nhl_players_by_team
        result = get_nhl_players_by_team(team_abbr="NJD", season="20232024")
        
        assert "players" in result
        assert "roster" in result["players"]
        assert len(result["players"]["roster"]) == 2
        assert result["players"]["roster"][0]["name"] == "Jack Hughes"
        assert result["players"]["roster"][1]["position"] == "C"
        
        mock_players.players_by_team.assert_called_once_with("NJD", "20232024")
    
    def test_get_nhl_players_by_team_error(self, mock_players):
        mock_players.players_by_team.side_effect = Exception("Players API error")
        
        from src import get_nhl_players_by_team
        result = get_nhl_players_by_team(team_abbr="INVALID", season="20232024")
        
        assert "error" in result
        assert result["error"] == "Players API error"
    
    def test_get_nhl_franchises_success(self, mock_teams):
        mock_teams.franchises.return_value = [
            {"id": 1, "fullName": "Boston Bruins", "active": True},
            {"id": 2, "fullName": "Toronto Maple Leafs", "active": True},
            {"id": 3, "fullName": "Montreal Canadiens", "active": True}
        ]
        
        from src import get_nhl_franchises
        result = get_nhl_franchises()
        
        assert "franchises" in result
        assert len(result["franchises"]) == 3
        assert result["franchises"][0]["fullName"] == "Boston Bruins"
        assert result["franchises"][1]["active"] == True
        
        mock_teams.franchises.assert_called_once()
    
    def test_get_nhl_franchises_error(self, mock_teams):
        mock_teams.franchises.side_effect = Exception("Franchises API error")
        
        from src import get_nhl_franchises
        result = get_nhl_franchises()
        
        assert "error" in result
        assert result["error"] == "Franchises API error"
    
    def test_get_nhl_team_ids_success(self, mock_teams):
        mock_teams.teams.return_value = [
            {"name": "Boston Bruins", "abbr": "BOS"},
            {"name": "Toronto Maple Leafs", "abbr": "TOR"},
            {"name": "New Jersey Devils", "abbr": "NJD"}
        ]
        
        from src import get_nhl_team_ids
        result = get_nhl_team_ids()
        
        assert "team_abbreviations" in result
        assert result["team_abbreviations"]["Boston Bruins"] == "BOS"
        assert result["team_abbreviations"]["Toronto Maple Leafs"] == "TOR"
        assert result["team_abbreviations"]["New Jersey Devils"] == "NJD"
        
        mock_teams.teams.assert_called_once_with("now")
    
    def test_get_nhl_standings_success(self, mock_standings):
        mock_standings.league_standings.return_value = {
            "standings": [
                {"team": "Boston Bruins", "points": 100, "wins": 45},
                {"team": "Toronto Maple Leafs", "points": 95, "wins": 42}
            ]
        }
        
        from src import get_nhl_standings
        result = get_nhl_standings()
        
        assert "standings" in result
        assert "standings" in result["standings"]
        assert len(result["standings"]["standings"]) == 2
        assert result["standings"]["standings"][0]["team"] == "Boston Bruins"
        assert result["standings"]["standings"][1]["points"] == 95
        
        mock_standings.league_standings.assert_called_once_with("now")
    
    def test_get_nhl_standings_with_date(self, mock_standings):
        mock_standings.league_standings.return_value = {
            "standings": [
                {"team": "Boston Bruins", "points": 100, "wins": 45}
            ]
        }
        
        from src import get_nhl_standings
        result = get_nhl_standings(date="2024-01-15")
        
        assert "standings" in result
        assert "standings" in result["standings"]
        assert len(result["standings"]["standings"]) == 1
        
        mock_standings.league_standings.assert_called_once_with("2024-01-15")
    
    def test_get_nhl_standings_with_season(self, mock_standings):
        # Mock the season manifest call that happens inside get_nhl_standings
        with patch('src.standings.get_nhl_season_manifest') as mock_season_manifest:
            mock_season_manifest.return_value = {
                "seasons": [
                    {
                        "id": 20232024,
                        "standingsEnd": "2024-04-18",
                        "conferencesInUse": True,
                        "divisionsInUse": True
                    }
                ]
            }
            
            mock_standings.league_standings.return_value = {
                "standings": [
                    {"team": "Boston Bruins", "points": 100, "wins": 45}
                ]
            }
            
            from src import get_nhl_standings
            result = get_nhl_standings(season="20232024")
            
            assert "standings" in result
            assert "standings" in result["standings"]
            assert len(result["standings"]["standings"]) == 1
            
            mock_standings.league_standings.assert_called_once_with("2024-04-18")
    
    def test_get_nhl_standings_invalid_season(self):
        # Mock the season manifest call that happens inside get_nhl_standings
        with patch('src.standings.get_nhl_season_manifest') as mock_season_manifest:
            mock_season_manifest.return_value = {
                "seasons": [
                    {
                        "id": 20232024,
                        "standingsEnd": "2024-04-18"
                    }
                ]
            }
            
            from src import get_nhl_standings
            result = get_nhl_standings(season="99999999")
            
            assert "error" in result
            assert "Invalid Season Id 99999999" in result["error"]
    
    def test_get_nhl_standings_error(self, mock_standings):
        mock_standings.league_standings.side_effect = Exception("Standings API error")
        
        from src import get_nhl_standings
        result = get_nhl_standings()
        
        assert "error" in result
        assert result["error"] == "Standings API error"
    
    def test_get_nhl_season_manifest_success(self, mock_standings):
        mock_standings.season_standing_manifest.return_value = [
            {
                "id": 20232024,
                "conferencesInUse": True,
                "divisionsInUse": True,
                "pointForOTlossInUse": True,
                "regulationWinsInUse": True,
                "rowInUse": True,
                "standingsEnd": "2024-04-18",
                "standingsStart": "2023-10-10",
                "tiesInUse": False,
                "wildcardInUse": True
            },
            {
                "id": 20242025,
                "conferencesInUse": True,
                "divisionsInUse": True,
                "pointForOTlossInUse": True,
                "regulationWinsInUse": True,
                "rowInUse": True,
                "standingsEnd": "2025-04-17",
                "standingsStart": "2024-10-08",
                "tiesInUse": False,
                "wildcardInUse": True
            }
        ]
        
        from src import get_nhl_season_manifest
        result = get_nhl_season_manifest()
        
        assert "seasons" in result
        assert len(result["seasons"]) == 2
        assert result["seasons"][0]["id"] == 20232024
        assert result["seasons"][0]["standingsEnd"] == "2024-04-18"
        assert result["seasons"][1]["id"] == 20242025
        assert result["seasons"][1]["standingsStart"] == "2024-10-08"
        
        mock_standings.season_standing_manifest.assert_called_once()
    
    def test_get_nhl_season_manifest_error(self, mock_standings):
        mock_standings.season_standing_manifest.side_effect = Exception("Season manifest API error")
        
        from src import get_nhl_season_manifest
        result = get_nhl_season_manifest()
        
        assert "error" in result
        assert result["error"] == "Season manifest API error"
    
    def test_get_nhl_daily_schedule_success(self, mock_schedule):
        mock_schedule.daily_schedule.return_value = {
            "nextStartDate": "2024-01-16",
            "previousStartDate": "2024-01-14",
            "date": "2024-01-15",
            "oddsPartners": ["partner1", "partner2"],
            "games": [
                {"id": 1, "homeTeam": "BOS", "awayTeam": "TOR", "startTime": "19:00"},
                {"id": 2, "homeTeam": "NJD", "awayTeam": "NYR", "startTime": "19:30"}
            ],
            "numberOfGames": 2
        }
        
        from src import get_nhl_daily_schedule
        result = get_nhl_daily_schedule("2024-01-15")
        
        assert "schedule" in result
        assert result["schedule"]["date"] == "2024-01-15"
        assert result["schedule"]["numberOfGames"] == 2
        assert len(result["schedule"]["games"]) == 2
        
        mock_schedule.daily_schedule.assert_called_once_with("2024-01-15")
    
    def test_get_nhl_daily_schedule_default_date(self, mock_schedule):
        mock_schedule.daily_schedule.return_value = {
            "date": "2024-01-15",
            "games": [],
            "numberOfGames": 0
        }
        
        from src import get_nhl_daily_schedule
        result = get_nhl_daily_schedule()
        
        assert "schedule" in result
        assert "date" in result["schedule"]
        
        mock_schedule.daily_schedule.assert_called_once()
    
    def test_get_nhl_daily_schedule_invalid_date_format(self):
        from src import get_nhl_daily_schedule
        result = get_nhl_daily_schedule("invalid-date")
        
        assert "error" in result
        assert "Invalid date format" in result["error"]
    
    def test_get_nhl_daily_schedule_error(self, mock_schedule):
        mock_schedule.daily_schedule.side_effect = Exception("Daily schedule API error")
        
        from src import get_nhl_daily_schedule
        result = get_nhl_daily_schedule("2024-01-15")
        
        assert "error" in result
        assert result["error"] == "Daily schedule API error"
    
    def test_get_nhl_weekly_schedule_success(self, mock_schedule):
        mock_schedule.weekly_schedule.return_value = {
            "gameWeek": [
                {"date": "2024-01-15", "games": [{"id": 1, "homeTeam": "BOS"}]},
                {"date": "2024-01-16", "games": [{"id": 2, "homeTeam": "TOR"}]}
            ]
        }
        
        from src import get_nhl_weekly_schedule
        result = get_nhl_weekly_schedule("2024-01-15")
        
        assert "schedule" in result
        assert "gameWeek" in result["schedule"]
        assert len(result["schedule"]["gameWeek"]) == 2
        
        mock_schedule.weekly_schedule.assert_called_once_with("2024-01-15")
    
    def test_get_nhl_weekly_schedule_default_date(self, mock_schedule):
        mock_schedule.weekly_schedule.return_value = {"gameWeek": []}
        
        from src import get_nhl_weekly_schedule
        result = get_nhl_weekly_schedule()
        
        assert "schedule" in result
        
        mock_schedule.weekly_schedule.assert_called_once_with("now")
    
    def test_get_nhl_team_monthly_schedule_success(self, mock_schedule):
        mock_schedule.team_monthly_schedule.return_value = [
            {"id": 1, "homeTeam": "BOS", "awayTeam": "TOR", "date": "2024-01-15"},
            {"id": 2, "homeTeam": "BOS", "awayTeam": "NJD", "date": "2024-01-20"}
        ]
        
        from src import get_nhl_team_monthly_schedule
        result = get_nhl_team_monthly_schedule("BOS", "2024-01")
        
        assert "games" in result
        assert result["team"] == "BOS"
        assert result["month"] == "2024-01"
        assert len(result["games"]) == 2
        
        mock_schedule.team_monthly_schedule.assert_called_once_with("BOS", "2024-01")
    
    def test_get_nhl_team_monthly_schedule_default_month(self, mock_schedule):
        mock_schedule.team_monthly_schedule.return_value = []
        
        from src import get_nhl_team_monthly_schedule
        result = get_nhl_team_monthly_schedule("BOS")
        
        assert "games" in result
        assert result["team"] == "BOS"
        assert result["month"] is None
        
        mock_schedule.team_monthly_schedule.assert_called_once_with("BOS", None)
    
    def test_get_nhl_team_weekly_schedule_success(self, mock_schedule):
        mock_schedule.team_weekly_schedule.return_value = [
            {"id": 1, "homeTeam": "BOS", "awayTeam": "TOR", "date": "2024-01-15"},
            {"id": 2, "homeTeam": "BOS", "awayTeam": "NJD", "date": "2024-01-17"}
        ]
        
        from src import get_nhl_team_weekly_schedule
        result = get_nhl_team_weekly_schedule("BOS", "2024-01-15")
        
        assert "games" in result
        assert result["team"] == "BOS"
        assert result["date"] == "2024-01-15"
        assert len(result["games"]) == 2
        
        mock_schedule.team_weekly_schedule.assert_called_once_with("BOS", "2024-01-15")
    
    def test_get_nhl_team_season_schedule_success(self, mock_schedule):
        mock_schedule.team_season_schedule.return_value = {
            "games": [
                {"id": 1, "homeTeam": "BOS", "awayTeam": "TOR", "date": "2024-01-15"},
                {"id": 2, "homeTeam": "BOS", "awayTeam": "NJD", "date": "2024-01-20"}
            ],
            "season": "20232024"
        }
        
        from src import get_nhl_team_season_schedule
        result = get_nhl_team_season_schedule("BOS", "20232024")
        
        assert "schedule" in result
        assert result["team"] == "BOS"
        assert result["season"] == "20232024"
        assert "games" in result["schedule"]
        
        mock_schedule.team_season_schedule.assert_called_once_with("BOS", "20232024")
    
    def test_get_nhl_calendar_schedule_success(self, mock_schedule):
        mock_schedule.calendar_schedule.return_value = {
            "date": "2024-01-15",
            "games": [
                {"id": 1, "homeTeam": "BOS", "awayTeam": "TOR", "startTime": "19:00"}
            ]
        }
        
        from src import get_nhl_calendar_schedule
        result = get_nhl_calendar_schedule("2024-01-15")
        
        assert "schedule" in result
        assert result["date"] == "2024-01-15"
        assert "games" in result["schedule"]
        
        mock_schedule.calendar_schedule.assert_called_once_with("2024-01-15")
    
    def test_get_nhl_playoff_carousel_success(self, mock_schedule):
        mock_schedule.playoff_carousel.return_value = {
            "series": [
                {"id": "a", "homeTeam": "BOS", "awayTeam": "TOR", "status": "active"},
                {"id": "b", "homeTeam": "NJD", "awayTeam": "NYR", "status": "active"}
            ]
        }
        
        from src import get_nhl_playoff_carousel
        result = get_nhl_playoff_carousel("20232024")
        
        assert "playoff_data" in result
        assert result["season"] == "20232024"
        assert "series" in result["playoff_data"]
        
        mock_schedule.playoff_carousel.assert_called_once_with("20232024")
    
    def test_get_nhl_playoff_series_schedule_success(self, mock_schedule):
        mock_schedule.playoff_series_schedule.return_value = {
            "series": "a",
            "games": [
                {"id": 1, "homeTeam": "BOS", "awayTeam": "TOR", "date": "2024-01-15"},
                {"id": 2, "homeTeam": "TOR", "awayTeam": "BOS", "date": "2024-01-17"}
            ]
        }
        
        from src import get_nhl_playoff_series_schedule
        result = get_nhl_playoff_series_schedule("20232024", "a")
        
        assert "series_schedule" in result
        assert result["season"] == "20232024"
        assert result["series"] == "a"
        assert "games" in result["series_schedule"]
        
        mock_schedule.playoff_series_schedule.assert_called_once_with("20232024", "a")
    
    def test_get_nhl_playoff_bracket_success(self, mock_schedule):
        mock_schedule.playoff_bracket.return_value = {
            "bracket": {
                "round1": [
                    {"series": "a", "homeTeam": "BOS", "awayTeam": "TOR"},
                    {"series": "b", "homeTeam": "NJD", "awayTeam": "NYR"}
                ]
            }
        }
        
        from src import get_nhl_playoff_bracket
        result = get_nhl_playoff_bracket("2024")
        
        assert "bracket" in result
        assert result["year"] == "2024"
        assert "round1" in result["bracket"]["bracket"]
        
        mock_schedule.playoff_bracket.assert_called_once_with("2024")
    
    # Stats API Tests
    def test_get_nhl_gametypes_per_season_by_team_success(self, mock_stats):
        mock_stats.gametypes_per_season_directory_by_team.return_value = [
            {'season': 20242025, 'gameTypes': [2]},
            {'season': 20232024, 'gameTypes': [2, 3]},
            {'season': 20222023, 'gameTypes': [2, 3]}
        ]
        
        from src import get_nhl_gametypes_per_season_by_team
        result = get_nhl_gametypes_per_season_by_team("TOR")
        
        assert "gametypes" in result
        assert len(result["gametypes"]) == 3
        assert result["gametypes"][0]["season"] == 20242025
        assert result["gametypes"][1]["gameTypes"] == [2, 3]
        
        mock_stats.gametypes_per_season_directory_by_team.assert_called_once_with("TOR")
    
    def test_get_nhl_gametypes_per_season_by_team_error(self, mock_stats):
        mock_stats.gametypes_per_season_directory_by_team.side_effect = Exception("Team not found")
        
        from src import get_nhl_gametypes_per_season_by_team
        result = get_nhl_gametypes_per_season_by_team("INVALID")
        
        assert "error" in result
        assert result["error"] == "Team not found"
    
    def test_get_nhl_player_career_stats_success(self, mock_stats):
        mock_stats.player_career_stats.return_value = {
            'playerId': 8478402,
            'isActive': True,
            'currentTeamId': 22,
            'currentTeamAbbrev': 'EDM',
            'fullTeamName': {'default': 'Edmonton Oilers', 'fr': "Oilers d'Edmonton"},
            'firstName': {'default': 'Connor'},
            'lastName': {'default': 'McDavid'},
            'sweaterNumber': 97,
            'position': 'C'
        }
        
        from src import get_nhl_player_career_stats
        result = get_nhl_player_career_stats("8478402")
        
        assert "player_stats" in result
        assert result["player_stats"]["playerId"] == 8478402
        assert result["player_stats"]["firstName"]["default"] == "Connor"
        assert result["player_stats"]["lastName"]["default"] == "McDavid"
        assert result["player_stats"]["position"] == "C"
        
        mock_stats.player_career_stats.assert_called_once_with("8478402")
    
    def test_get_nhl_player_career_stats_error(self, mock_stats):
        mock_stats.player_career_stats.side_effect = Exception("Player not found")
        
        from src import get_nhl_player_career_stats
        result = get_nhl_player_career_stats("9999999")
        
        assert "error" in result
        assert result["error"] == "Player not found"
    
    def test_get_nhl_player_game_log_success(self, mock_stats):
        mock_stats.player_game_log.return_value = [
            {
                'gameId': 2024020641,
                'teamAbbrev': 'EDM',
                'homeRoadFlag': 'R',
                'gameDate': '2025-01-07',
                'goals': 1,
                'assists': 0,
                'points': 1,
                'plusMinus': 0,
                'shots': 5,
                'toi': '18:04'
            },
            {
                'gameId': 2024020642,
                'teamAbbrev': 'EDM',
                'homeRoadFlag': 'H',
                'gameDate': '2025-01-09',
                'goals': 0,
                'assists': 2,
                'points': 2,
                'plusMinus': 1,
                'shots': 3,
                'toi': '19:15'
            }
        ]
        
        from src import get_nhl_player_game_log
        result = get_nhl_player_game_log("8478402", "20242025", 2)
        
        assert "game_log" in result
        assert len(result["game_log"]) == 2
        assert result["game_log"][0]["goals"] == 1
        assert result["game_log"][0]["assists"] == 0
        assert result["game_log"][1]["goals"] == 0
        assert result["game_log"][1]["assists"] == 2
        
        mock_stats.player_game_log.assert_called_once_with("8478402", "20242025", 2)
    
    def test_get_nhl_player_game_log_error(self, mock_stats):
        mock_stats.player_game_log.side_effect = Exception("Game log not found")
        
        from src import get_nhl_player_game_log
        result = get_nhl_player_game_log("8478402", "20242025", 2)
        
        assert "error" in result
        assert result["error"] == "Game log not found"
    
    def test_get_nhl_team_summary_stats_success(self, mock_stats):
        mock_stats.team_summary.return_value = [
            {
                'faceoffWinPct': 0.48235,
                'gamesPlayed': 82,
                'goalsAgainst': 242,
                'goalsAgainstPerGame': 2.95121,
                'goalsFor': 337,
                'goalsForPerGame': 4.10975,
                'losses': 18,
                'otLosses': 6,
                'points': 122,
                'wins': 58,
                'teamFullName': 'Florida Panthers',
                'teamId': 13,
                'seasonId': 20212022
            }
        ]
        
        from src import get_nhl_team_summary_stats
        result = get_nhl_team_summary_stats("20202021", "20212022", 2)
        
        assert "team_summary" in result
        assert len(result["team_summary"]) == 1
        assert result["team_summary"][0]["teamFullName"] == "Florida Panthers"
        assert result["team_summary"][0]["points"] == 122
        assert result["team_summary"][0]["wins"] == 58
        
        mock_stats.team_summary.assert_called_once_with(
            start_season="20202021",
            end_season="20212022",
            game_type_id=2,
            is_game=False,
            is_aggregate=False,
            start=0,
            limit=50
        )
    
    def test_get_nhl_team_summary_stats_with_custom_params(self, mock_stats):
        mock_stats.team_summary.return_value = []
        
        from src import get_nhl_team_summary_stats
        result = get_nhl_team_summary_stats(
            "20202021", "20222023", 3, True, True, 10, 25
        )
        
        assert "team_summary" in result
        
        mock_stats.team_summary.assert_called_once_with(
            start_season="20202021",
            end_season="20222023",
            game_type_id=3,
            is_game=True,
            is_aggregate=True,
            start=10,
            limit=25
        )
    
    def test_get_nhl_team_summary_stats_error(self, mock_stats):
        mock_stats.team_summary.side_effect = Exception("Team summary API error")
        
        from src import get_nhl_team_summary_stats
        result = get_nhl_team_summary_stats("20202021", "20212022")
        
        assert "error" in result
        assert result["error"] == "Team summary API error"
    
    def test_get_nhl_skater_stats_summary_success(self, mock_stats):
        mock_stats.skater_stats_summary.return_value = [
            {
                'assists': 71,
                'evGoals': 38,
                'evPoints': 75,
                'faceoffWinPct': 0.1,
                'gameWinningGoals': 5,
                'gamesPlayed': 82,
                'goals': 49,
                'lastName': 'Panarin',
                'otGoals': 1,
                'penaltyMinutes': 24,
                'playerId': 8478550,
                'plusMinus': 18,
                'points': 120,
                'pointsPerGame': 1.46341,
                'positionCode': 'L',
                'ppGoals': 11,
                'ppPoints': 44,
                'seasonId': 20232024,
                'shGoals': 0,
                'shPoints': 1,
                'shootingPct': 0.16171,
                'shootsCatches': 'R',
                'shots': 303,
                'skaterFullName': 'Artemi Panarin',
                'teamAbbrevs': 'NYR',
                'timeOnIcePerGame': 1207.1341
            }
        ]
        
        from src import get_nhl_skater_stats_summary
        result = get_nhl_skater_stats_summary("20232024", "20232024")
        
        assert "skater_stats" in result
        assert len(result["skater_stats"]) == 1
        assert result["skater_stats"][0]["skaterFullName"] == "Artemi Panarin"
        assert result["skater_stats"][0]["points"] == 120
        assert result["skater_stats"][0]["goals"] == 49
        assert result["skater_stats"][0]["assists"] == 71
        
        mock_stats.skater_stats_summary.assert_called_once_with(
            start_season="20232024",
            end_season="20232024",
            franchise_id=None,
            game_type_id=2,
            aggregate=False,
            start=0,
            limit=25
        )
    
    def test_get_nhl_skater_stats_summary_with_franchise(self, mock_stats):
        mock_stats.skater_stats_summary.return_value = []
        
        from src import get_nhl_skater_stats_summary
        result = get_nhl_skater_stats_summary("20232024", "20232024", "10", 3, True, 5, 15)
        
        assert "skater_stats" in result
        
        mock_stats.skater_stats_summary.assert_called_once_with(
            start_season="20232024",
            end_season="20232024",
            franchise_id="10",
            game_type_id=3,
            aggregate=True,
            start=5,
            limit=15
        )
    
    def test_get_nhl_skater_stats_summary_error(self, mock_stats):
        mock_stats.skater_stats_summary.side_effect = Exception("Skater stats API error")
        
        from src import get_nhl_skater_stats_summary
        result = get_nhl_skater_stats_summary("20232024", "20232024")
        
        assert "error" in result
        assert result["error"] == "Skater stats API error"
    
    def test_get_nhl_goalie_stats_summary_success(self, mock_stats):
        mock_stats.goalie_stats_summary.return_value = [
            {
                'assists': 0,
                'gamesPlayed': 33,
                'gamesStarted': 33,
                'goalieFullName': 'Connor Hellebuyck',
                'goals': 0,
                'goalsAgainst': 69,
                'goalsAgainstAverage': 2.08485,
                'lastName': 'Hellebuyck',
                'losses': 6,
                'otLosses': 2,
                'penaltyMinutes': 0,
                'playerId': 8476945,
                'points': 0,
                'savePct': 0.92612,
                'saves': 865,
                'seasonId': 20242025,
                'shootsCatches': 'L',
                'shotsAgainst': 934,
                'shutouts': 5,
                'teamAbbrevs': 'WPG',
                'ties': None,
                'timeOnIce': 119145,
                'wins': 25
            }
        ]
        
        from src import get_nhl_goalie_stats_summary
        result = get_nhl_goalie_stats_summary("20242025", "20242025", "summary", 2)
        
        assert "goalie_stats" in result
        assert len(result["goalie_stats"]) == 1
        assert result["goalie_stats"][0]["goalieFullName"] == "Connor Hellebuyck"
        assert result["goalie_stats"][0]["wins"] == 25
        assert result["goalie_stats"][0]["savePct"] == 0.92612
        assert result["goalie_stats"][0]["shutouts"] == 5
        
        mock_stats.goalie_stats_summary.assert_called_once_with(
            start_season="20242025",
            end_season="20242025",
            stats_type="summary",
            game_type_id=2,
            franchise_id=None,
            aggregate=False,
            start=0,
            limit=25
        )
    
    def test_get_nhl_goalie_stats_summary_with_custom_params(self, mock_stats):
        mock_stats.goalie_stats_summary.return_value = []
        
        from src import get_nhl_goalie_stats_summary
        result = get_nhl_goalie_stats_summary(
            "20242025", "20232024", "advanced", 3, "10", True, 5, 15
        )
        
        assert "goalie_stats" in result
        
        mock_stats.goalie_stats_summary.assert_called_once_with(
            start_season="20242025",
            end_season="20232024",
            stats_type="advanced",
            game_type_id=3,
            franchise_id="10",
            aggregate=True,
            start=5,
            limit=15
        )
    
    def test_get_nhl_goalie_stats_summary_error(self, mock_stats):
        mock_stats.goalie_stats_summary.side_effect = Exception("Goalie stats API error")
        
        from src import get_nhl_goalie_stats_summary
        result = get_nhl_goalie_stats_summary("20242025")
        
        assert "error" in result
        assert result["error"] == "Goalie stats API error"
    
    def test_setup_nhl_tools_registers_all_tools(self):
        mock_mcp = Mock()
        
        setup_nhl_tools(mock_mcp)
        
        assert mock_mcp.tool.call_count == 23  # Updated count to include new Stats API tools
        
        tool_calls = mock_mcp.tool.call_args_list
        assert len(tool_calls) == 23


if __name__ == "__main__":
    pytest.main([__file__])
