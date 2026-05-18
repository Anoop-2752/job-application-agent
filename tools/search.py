import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests
from typing import List
from config.settings import get_settings

settings = get_settings()


def search_jobs(company: str, role_keywords: str = "AI ML engineer") -> List[dict]:
    """
    Search for job listings from a target company.
    Returns a list of results with title, link, snippet.
    """
    query = f"{company} {role_keywords} jobs site:linkedin.com OR site:careers.{company.lower().replace(' ', '')}.com"

    url = "https://html.duckduckgo.com/html/"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"q": query}

    try:
        response = requests.post(url, headers=headers, data=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return [{"error": str(e), "company": company}]

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    for result in soup.select(".result__body")[:5]:  # top 5 results
        title_tag = result.select_one(".result__title")
        link_tag = result.select_one(".result__url")
        snippet_tag = result.select_one(".result__snippet")

        results.append({
            "company": company,
            "title": title_tag.get_text(strip=True) if title_tag else "",
            "url": link_tag.get_text(strip=True) if link_tag else "",
            "snippet": snippet_tag.get_text(strip=True) if snippet_tag else "",
        })

    return results if results else [{"company": company, "message": "No results found"}]


if __name__ == "__main__":
    # Quick manual test
    results = search_jobs("Tata Elxsi", "AI ML engineer")
    for r in results:
        print(r)
        print("---")