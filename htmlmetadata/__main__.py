import argparse
import json

from htmlmetadata import extract_metadata

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract HTML metadata')
    parser.add_argument('url', help='URL to fetch and extract metadata')
    args = parser.parse_args()

    data = extract_metadata(args.url)
    print(json.dumps(data, indent=2))
