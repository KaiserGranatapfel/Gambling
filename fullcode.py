import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_html(url):
    """
    Fetches the HTML content of the given URL.

    Parameters:
    url (str): The URL of the webpage to fetch.

    Returns:
    BeautifulSoup object: Parsed HTML content of the page.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def extract_match_data(match_url):
    """
    Extracts match data from the given ESPNcricinfo match URL.

    Parameters:
    match_url (str): URL of the match page.

    Returns:
    dict: A dictionary containing match details.
    """
    soup = fetch_html(match_url)
    if soup:
        try:
            # Example extraction logic; adjust selectors based on actual HTML structure
            match_id = match_url.split('/')[-1]
            teams = [team.get_text() for team in soup.select('.team-name')]
            toss_winner = soup.select_one('.toss-winner').get_text()
            toss_decision = soup.select_one('.toss-decision').get_text()
            pitch_type = soup.select_one('.pitch-type').get_text()
            weather = soup.select_one('.weather').get_text()
            match_type = soup.select_one('.match-type').get_text()
            outcome = soup.select_one('.match-outcome').get_text()

            return {
                'Match ID': match_id,
                'Team1': teams[0],
                'Team2': teams[1],
                'Toss Winner': toss_winner,
                'Toss Decision': toss_decision,
                'Pitch Type': pitch_type,
                'Weather': weather,
                'Match Type': match_type,
                'Outcome': outcome
            }
        except AttributeError as e:
            print(f"Error parsing match data from {match_url}: {e}")
            return None
    return None

def extract_team_data(team_url):
    """
    Extracts team data from the given ESPNcricinfo team URL.

    Parameters:
    team_url (str): URL of the team page.

    Returns:
    dict: A dictionary containing team details.
    """
    soup = fetch_html(team_url)
    if soup:
        try:
            team_name = soup.select_one('.team-name').get_text()
            win_rate = soup.select_one('.win-rate').get_text()
            loss_rate = soup.select_one('.loss-rate').get_text()
            partnerships = soup.select_one('.partnerships').get_text()
            historical_performance = soup.select_one('.historical-performance').get_text()

            return {
                'Team Name': team_name,
                'Win Rate': win_rate,
                'Loss Rate': loss_rate,
                'Partnerships': partnerships,
                'Historical Performance': historical_performance
            }
        except AttributeError as e:
            print(f"Error parsing team data from {team_url}: {e}")
            return None
    return None


def extract_player_data(player_url):
    """
    Extracts player data from the given ESPNcricinfo player URL.

    Parameters:
    player_url (str): URL of the player page.

    Returns:
    dict: A dictionary containing player details.
    """
    soup = fetch_html(player_url)
    if soup:
        try:
            player_name = soup.select_one('.player-name').get_text()
            team_name = soup.select_one('.team-name').get_text()
            performance_metrics = soup.select_one('.performance-metrics').get_text()
            player_form = soup.select_one('.player-form').get_text()
            age = soup.select_one('.age').get_text()
            specialization = soup.select_one('.specialization').get_text()

            return {
                'Player Name': player_name,
                'Team Name': team_name,
                'Performance Metrics': performance_metrics,
                'Player Form': player_form,
                'Age': age,
                'Specialization': specialization
            }
        except AttributeError as e:
            print(f"Error parsing player data from {player_url}: {e}")
            return None
    return None


# Example URLs; replace with actual URLs
match_urls = ['https://www.espncricinfo.com/match_url_1', 'https://www.espncricinfo.com/match_url_2']
team_urls = ['https://www.espncricinfo.com/team_url_1', 'https://www.espncricinfo.com/team_url_2']
player_urls = ['https://www.espncricinfo.com/player_url_1', 'https://www.espncricinfo.com/player_url_2']

# Extract data
match_data = [extract_match_data(url) for url in match_urls]
team_data = [extract_team_data(url) for url in team_urls]
player_data = [extract_player_data(url) for url in player_urls]

# Create DataFrames
match_df = pd.DataFrame(match_data)
team_df = pd.DataFrame(team_data)
player_df = pd.DataFrame(player_data)


match_df.to_csv('match_data.csv', index=False)
team_df.to_csv('team_data.csv', index=False)
player_df.to_csv('player_data.csv', index=False)


import logging

# Configure logging
logging.basicConfig(
    filename='scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def fetch_html(url):
    """
    Fetches the HTML content of the given URL.

    Parameters:
    url (str): The URL of the webpage to fetch.

    Returns:
    BeautifulSoup object: Parsed HTML content of the page, or None if an error occurs.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.info(f"Successfully fetched content from {url}")
        return BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return None



def main():
    # Example URLs; replace with actual URLs
    match_urls = [
        'https://www.espncricinfo.com/match_url_1',
        'https://www.espncricinfo.com/match_url_2'
    ]
    team_urls = [
        'https://www.espncricinfo.com/team_url_1',
        'https://www.espncricinfo.com/team_url_2'
    ]
    player_urls = [
        'https://www.espncricinfo.com/player_url_1',
        'https://www.espncricinfo.com/player_url_2'
    ]

    # Extract data
    match_data = [extract_match_data(url) for url in match_urls]
    team_data = [extract_team_data(url) for url in team_urls]
    player_data = [extract_player_data(url) for url in player_urls]

    # Filter out None values resulting from errors
    match_data = [data for data in match_data if data is not None]
    team_data = [data for data in team_data if data is not None]
    player_data = [data for data in player_data if data is not None]

    # Create DataFrames
    match_df = pd.DataFrame(match_data)
    team_df = pd.DataFrame(team_data)
    player_df = pd.DataFrame(player_data)

    # Save DataFrames to CSV
    match_df.to_csv('match_data.csv', index=False)
    team_df.to_csv('team_data.csv', index=False)
    player_df.to_csv('player_data.csv', index=False)

    logging.info("Data scraping and saving completed successfully.")

if __name__ == "__main__":
    main()

