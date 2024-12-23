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

# List of sitemap URLs to process
sitemap_urls = [
    'https://www.espncricinfo.com/sitemap/news-sitemap.xml',
    'https://www.espncricinfo.com/sitemap/standalone.xml.gz',
    'https://www.espncricinfo.com/sitemap/hindi/sitemap.xml',
    'https://www.espncricinfo.com/sitemap/overall-match.xml.gz',
    'https://www.espncricinfo.com/sitemap/overall-series.xml.gz',
    'https://www.espncricinfo.com/sitemap/story.xml.gz',
    'https://www.espncricinfo.com/sitemap/overall-cricketer.xml.gz',
    'https://www.espncricinfo.com/sitemap/overall-cricketer-1.xml.gz',
    'https://www.espncricinfo.com/sitemap/overall-cricketer-2.xml.gz',
    'https://www.espncricinfo.com/sitemap/overall-cricketer-3.xml.gz',
    'https://www.espncricinfo.com/sitemap/format-record.xml.gz',
    'https://www.espncricinfo.com/sitemap/overall-team.xml.gz',
    'https://www.espncricinfo.com/sitemap/overall-videos.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-decade-0.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-1.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-2.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-3.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-4.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-5.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-6.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-7.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-8.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-10.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-11.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-12.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-13.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-15.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-16.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-17.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-18.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-19.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-20.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-21.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-22.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-23.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-25.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-26.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-27.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-28.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-29.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-30.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-31.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-32.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-33.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-34.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-35.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-37.xml.gz',
    'https://www.espncricinfo.com/sitemap/records-headtohead-38.xml.gz',
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

# Output the total number of extracted URLs
print(f"Total URLs extracted: {len(all_extracted_urls)}")

print(all_extracted_urls)