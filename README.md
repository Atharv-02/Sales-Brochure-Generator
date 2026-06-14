# Sales Brochure Generator

Generate a concise sales brochure for a company from its public website. The notebook scrapes a company homepage, asks an OpenAI-compatible model to choose useful supporting pages, gathers those page contents, and produces a Markdown brochure for prospects, investors, or recruiting audiences.

## What This Project Does

- Scrapes visible website text with `requests` and `BeautifulSoup`
- Extracts links from a company homepage
- Uses an LLM to select relevant pages such as about, careers, blog, or company pages
- Builds a short brochure in Markdown from the collected website content

## Project Structure

```text
.
├── day5.ipynb       # Main notebook workflow
├── scraper.py       # Website scraping helpers used by the notebook
├── requirements.txt # Python dependencies
└── .env.example     # Template for local API configuration
```

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Create your local environment file:

```bash
cp .env.example .env
```

Then update `.env` with your API details:

```text
API_KEY=your_api_key_here
BASE_URL=https://api.example.com/openai/v1
```

The current notebook is configured for:

```python
MODEL = "llama-3.3-70b-versatile"
```

Use the `BASE_URL`, `API_KEY`, and model that match your provider.

## Running the Notebook

Open `day5.ipynb` in Jupyter or VS Code and select the `.venv` Python kernel. Run the cells from top to bottom.

The core workflow is:

1. Load environment variables
2. Fetch links from a company website
3. Ask the model to choose relevant brochure links
4. Fetch content from those pages
5. Generate a Markdown brochure

## Notes

- Do not commit your real `.env` file. It may contain private API keys.
- Some websites may block scraping or fail DNS resolution. If a request fails, try another URL or check that the site is reachable in your browser.
- The scraper is intentionally simple for learning purposes. Production scraping should add timeouts, error handling, rate limiting, and respect each website's terms and robots rules.

