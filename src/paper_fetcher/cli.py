import argparse
import sys
from paper_fetcher.paper_fetcher import fetch_paper_ids, fetch_paper_details, save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("-f", "--file", type=str, help="Save results to the specified file")
    
    args = parser.parse_args()

    if args.debug:
        print(f"Searching PubMed for: {args.query}")

    paper_ids = fetch_paper_ids(args.query)
    if not paper_ids:
        print("No papers found.")
        sys.exit(1)

    paper_details = fetch_paper_details(paper_ids)

    if args.file:
        save_to_csv(paper_details, args.file)
        print(f"Results saved to {args.file}")
    else:
        for paper in paper_details:
            print(paper)

if __name__ == "__main__":
    main()
