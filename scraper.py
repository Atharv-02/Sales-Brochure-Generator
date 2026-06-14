from bs4 import BeautifulSoup
import requests


# Use a browser-like User-Agent so basic website requests are less likely to be
# rejected by sites that block the default Python requests header.
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def fetch_website_contents(url):
    """
    Fetch a web page and return clean text content for brochure generation.

    The returned text includes the page title followed by visible body text.
    Script, style, image, and input elements are removed because they do not add
    useful written content for the LLM prompt. The result is capped at 2,000
    characters to keep downstream prompts compact.
    """
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string if soup.title else "No title found"

    if soup.body:
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""
    return (title + "\n\n" + text)[:2_000]


def fetch_website_links(url):
    """
    Return all non-empty links found on a web page.

    This helper intentionally keeps scraping simple for the notebook workflow:
    fetch the page, parse all anchor tags, and return each href value that is
    present. Relative links are left as-is so the notebook can decide how to
    interpret them.
    """
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")]
    return [link for link in links if link]
