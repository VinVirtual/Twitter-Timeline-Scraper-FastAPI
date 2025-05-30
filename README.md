# Twitter Timeline Scraper

A Python-based tool for scraping Twitter timelines and extracting tweet data efficiently.

## Features

- Scrape tweets from user timelines
- Extract tweet content, metadata, and engagement metrics
- Save data in structured formats
- Handle rate limiting and pagination
- Configurable scraping parameters

## Prerequisites

- Python 3.8 or higher
- GROQ API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/VinVirtual/Twitter-Timeline-Scrapper.git
cd Twitter-Timeline-Scrapper
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your GROQ API key:
```
GROQ_API_KEY=your_groq_api_key
```

## Usage

1. Configure your scraping parameters in the script
2. Run the scraper:
```bash
python scraper.py
```

## Output

The scraper will generate output files containing the scraped tweet data in your preferred format.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for educational purposes only. Please ensure you comply with Twitter's Terms of Service and API usage guidelines when using this scraper. 