import requests
import xml.etree.ElementTree as ET

def fetch_sitemap(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.content

def parse_sitemap(xml_content):
    root = ET.fromstring(xml_content)
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    sitemap_urls = [elem.text for elem in root.findall('ns:sitemap/ns:loc', namespace)]
    return sitemap_urls

main_sitemap_url = 'https://www.espncricinfo.com/sitemap.xml'
main_sitemap_content = fetch_sitemap(main_sitemap_url)
individual_sitemaps = parse_sitemap(main_sitemap_content)

print(individual_sitemaps)

import gzip
import io

def fetch_and_decompress_gz(url):
    response = requests.get(url)
    response.raise_for_status()
    compressed_file = io.BytesIO(response.content)
    with gzip.GzipFile(fileobj=compressed_file) as decompressed_file:
        return decompressed_file.read()

# Example usage:
gz_sitemap_url = 'https://www.espncricinfo.com/sitemap/overall-match.xml.gz'
decompressed_content = fetch_and_decompress_gz(gz_sitemap_url)
