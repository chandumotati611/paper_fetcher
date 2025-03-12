import requests
import pandas as pd
import re
from typing import List, Dict

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_paper_ids(query: str) -> List[str]:
    """Fetch paper IDs from PubMed based on the query."""
    params = {"db": "pubmed", "term": query, "retmax": 10, "retmode": "json"}
    response = requests.get(PUBMED_API_URL, params=params)
    response.raise_for_status()
    return response.json().get("esearchresult", {}).get("idlist", [])

def fetch_paper_details(paper_ids: List[str]) -> List[Dict]:
    """Fetch detailed information for each paper."""
    papers = []
    for paper_id in paper_ids:
        response = requests.get(PUBMED_FETCH_URL, params={"db": "pubmed", "id": paper_id, "retmode": "xml"})
        response.raise_for_status()
        data = response.text
        
        # Extracting details using regex
        title_match = re.search(r"<ArticleTitle>(.*?)</ArticleTitle>", data)
        date_match = re.search(r"<PubDate>(.*?)</PubDate>", data)
        authors = re.findall(r"<Author>(.*?)</Author>", data)
        affiliations = re.findall(r"<Affiliation>(.*?)</Affiliation>", data)
        emails = re.findall(r"[\w\.-]+@[\w\.-]+", data)

        company_authors, company_affiliations = [], []
        for author, affiliation in zip(authors, affiliations):
            # For finding non-academic authors
            if "pharma" in affiliation.lower() or "biotech" in affiliation.lower():
                company_authors.append(author)
                company_affiliations.append(affiliation)

        papers.append({
            "PubmedID": paper_id,
            "Title": title_match.group(1) if title_match else "N/A",
            "Publication Date": date_match.group(1) if date_match else "N/A",
            "Non-academic Author(s)": ", ".join(company_authors) if company_authors else "N/A",
            "Company Affiliation(s)": ", ".join(company_affiliations) if company_affiliations else "N/A",
            "Corresponding Author Email": emails[0] if emails else "N/A"
        })

    return papers

def save_to_csv(data: List[Dict], filename: str):
    """Save the results to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
