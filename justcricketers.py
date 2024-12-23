import requests
import gzip
import io
import xml.etree.ElementTree as ET

def fetch_sitemap_content(url):
    """
    Fetches and optionally decompresses the content of a sitemap.

    Parameters:
    url (str): The URL of the sitemap to fetch.

    Returns:
    bytes: The raw XML content of the sitemap.
    """
    response = requests.get(url)
    response.raise_for_status()
    if url.endswith('.xml.gz'):
        # Handle gzipped sitemaps
        with gzip.GzipFile(fileobj=io.BytesIO(response.content)) as decompressed_file:
            return decompressed_file.read()
    else:
        # Handle plain XML sitemaps
        return response.content

def parse_sitemap(xml_content):
    """
    Parses the XML content of a sitemap and extracts URLs.

    Parameters:
    xml_content (bytes): The raw XML content of the sitemap.

    Returns:
    list: A list of URLs extracted from the sitemap.
    """
    root = ET.fromstring(xml_content)
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = [elem.text for elem in root.findall('ns:url/ns:loc', namespace)]
    return urls

def filter_relevant_urls(all_urls, players):
    """
    Filters URLs based on player names.

    Parameters:
    all_urls (list): A list of extracted URLs.
    players (list): A list of player names.

    Returns:
    dict: A dictionary of player names with their corresponding URLs.
    """
    player_urls = {}
    for player in players:
        player_key = player.lower().replace(" ", "-")  # Convert to URL-friendly format
        for url in all_urls:
            if player_key in url.lower():
                player_urls[player] = url
                break
    return player_urls

# List of sitemap URLs to process
sitemap_urls = [
    'https://www.espncricinfo.com/sitemap/overall-cricketer.xml.gz',
    'https://www.espncricinfo.com/sitemap/overall-cricketer-1.xml.gz',
    'https://www.espncricinfo.com/sitemap/overall-cricketer-2.xml.gz',
    'https://www.espncricinfo.com/sitemap/overall-cricketer-3.xml.gz',
]

# List of player names
players = [
    "Pat Cummins", "David Warner", "Marnus Labuschagne", "Steve Smith", 
    "Usman Khawaja", "Travis Head", "Cameron Green", "Alex Carey", 
    "Mitchell Starc", "Nathan Lyon", "Josh Hazlewood", "Rohit Sharma", 
    "Shubman Gill", "Cheteshwar Pujara", "Virat Kohli", "Ajinkya Rahane", 
    "Ravindra Jadeja", "Rishabh Pant", "Ravichandran Ashwin", 
    "Mohammed Shami", "Jasprit Bumrah", "Mohammed Siraj", 
    "Dean Elgar", "Aiden Markram", "Rassie van der Dussen", "Temba Bavuma", 
    "Quinton de Kock", "Keshav Maharaj", "Kagiso Rabada", "Anrich Nortje", 
    "Lungi Ngidi", "Marco Jansen", "Wiaan Mulder", "Ben Stokes", 
    "Zak Crawley", "Ben Duckett", "Joe Root", "Harry Brook", 
    "Jonny Bairstow", "Moeen Ali", "Chris Woakes", "Stuart Broad", 
    "James Anderson", "Ollie Robinson", "Kane Williamson", "Tom Latham", 
    "Devon Conway", "Henry Nicholls", "Daryl Mitchell", "Tom Blundell", 
    "Colin de Grandhomme", "Tim Southee", "Trent Boult", "Neil Wagner", 
    "Matt Henry", "Dimuth Karunaratne", "Pathum Nissanka", "Kusal Mendis", 
    "Angelo Mathews", "Dhananjaya de Silva", "Dinesh Chandimal", 
    "Ramesh Mendis", "Lasith Embuldeniya", "Suranga Lakmal", 
    "Lahiru Kumara", "Vishwa Fernando", "Babar Azam", "Abdullah Shafique", 
    "Azhar Ali", "Fawad Alam", "Mohammad Rizwan", "Faheem Ashraf", 
    "Shaheen Afridi", "Hasan Ali", "Naseem Shah", "Yasir Shah", 
    "Nauman Ali", "Kraigg Brathwaite", "John Campbell", "Nkrumah Bonner", 
    "Shai Hope", "Jason Holder", "Kyle Mayers", "Kemar Roach", 
    "Alzarri Joseph", "Shannon Gabriel", "Jomel Warrican", 
    "Roston Chase", "Mominul Haque", "Tamim Iqbal", "Mushfiqur Rahim", 
    "Shakib Al Hasan", "Liton Das", "Mehidy Hasan Miraz", "Taskin Ahmed", 
    "Mustafizur Rahman", "Shoriful Islam", "Ebadot Hossain", 
    "Taijul Islam", "Andrew Balbirnie", "Paul Stirling", 
    "Harry Tector", "Kevin O'Brien", "George Dockrell", "Lorcan Tucker", 
    "Mark Adair", "Barry McCarthy", "Andy McBrine", "Joshua Little", 
    "Craig Young", "Hashmatullah Shahidi", "Rahmat Shah", 
    "Ikram Alikhil", "Afsar Zazai", "Riaz Hassan", "Sediqullah Atal", 
    "Abdul Malik", "Bahir Shah Mahboob", "Ismat Alam", "Azmatullah Omarzai", 
    "Zahir Khan", "Zia Ur Rehman Akbar", "Zahir Shehzad", "Rashid Khan", 
    "Yamin Ahmadzai", "Bashir Ahmad Afghan", "Naveed Zadran", 
    "Fareed Ahmad Malik", "Rakep Patel", "Irfan Karim", "Shem Ngoche", 
    "Lucas Oluoch Ndandason", "Dhiren Gondaria", "Peter Langat", 
    "Sachin Bhudia", "Gerard Muthui", "Vraj Patel", "Francis Muia Mutua", 
    "Rushabvardhan Patel", "Pushkar Sharma", "Neil Mugabe", 
    "Sachin Gill"
]


# Process each sitemap and extract all URLs
all_extracted_urls = []

for sitemap_url in sitemap_urls:
    try:
        # Fetch the sitemap content
        xml_content = fetch_sitemap_content(sitemap_url)
        
        # Parse the sitemap and extract URLs
        extracted_urls = parse_sitemap(xml_content)
        
        # Append the extracted URLs to the main list
        all_extracted_urls.extend(extracted_urls)
        
        print(f"Successfully processed: {sitemap_url}")
    except Exception as e:
        print(f"Error processing {sitemap_url}: {e}")

# Filter URLs for relevant players
filtered_urls = filter_relevant_urls(all_extracted_urls, players)

# Output the filtered URLs in the specified format
for player, url in filtered_urls.items():
    print(f"{player}: {url}")
