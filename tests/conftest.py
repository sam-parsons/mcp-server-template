import pytest
from unittest.mock import Mock, MagicMock, patch
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture(autouse=True)
def mock_nhl_client():
    """
    Automatically mock the NHL client for all tests.
    This fixture runs automatically for every test.
    """
    # Create a mock client
    mock_client = Mock()
    
    # Mock the teams module
    mock_teams = Mock()
    mock_client.teams = mock_teams
    
    # Mock the players module
    mock_players = Mock()
    mock_client.players = mock_players
    
    # Mock the schedule module
    mock_schedule = Mock()
    mock_client.schedule = mock_schedule
    
    # Mock the standings module
    mock_standings = Mock()
    mock_client.standings = mock_standings
    
    # Mock the stats module
    mock_stats = Mock()
    mock_client.stats = mock_stats
    
    # Use patch to mock the client import at the module level
    with patch('src.client.client', mock_client):
        # Also patch the client in the teams module
        with patch('src.teams.client', mock_client):
            # Also patch the client in the players module
            with patch('src.players.client', mock_client):
                # Also patch the client in the schedule module
                with patch('src.schedule.client', mock_client):
                    # Also patch the client in the standings module
                    with patch('src.standings.client', mock_client):
                        # Also patch the client in the stats module
                        with patch('src.stats.client', mock_client):
                            yield mock_client

@pytest.fixture
def mock_teams(mock_nhl_client):
    """Fixture to access the mocked teams module"""
    return mock_nhl_client.teams

@pytest.fixture
def mock_players(mock_nhl_client):
    """Fixture to access the mocked players module"""
    return mock_nhl_client.players

@pytest.fixture
def mock_schedule(mock_nhl_client):
    """Fixture to access the mocked schedule module"""
    return mock_nhl_client.schedule

@pytest.fixture
def mock_standings(mock_nhl_client):
    """Fixture to access the mocked standings module"""
    return mock_nhl_client.standings

@pytest.fixture
def mock_stats(mock_nhl_client):
    """Fixture to access the mocked stats module"""
    return mock_nhl_client.stats

@pytest.fixture
def mock_standings_manifest():
    """Fixture to mock the season_standing_manifest function in standings module"""
    with patch('src.standings.season_standing_manifest') as mock_manifest:
        yield mock_manifest
