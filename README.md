# Twitter Timeline Scraper

A Python-based tool for scraping Twitter timelines and extracting tweet data efficiently.

## ⚠️ Security Warnings

Before using this tool, please be aware of the following security considerations:

1. **API Key Security**:
   - Never commit your `.env` file to version control
   - Keep your GROQ API key secure and rotate it if compromised
   - Monitor your API usage for any unauthorized access

2. **Chrome Profile Security**:
   - The tool uses your Chrome profile to access Twitter
   - This means it has access to your Twitter session
   - Use a separate Chrome profile for scraping to limit access to your main account
   - Never share your Chrome user data directory

3. **Twitter Terms of Service**:
   - This tool is for educational purposes only
   - Ensure you comply with Twitter's Terms of Service
   - Do not use this tool for:
     - Mass scraping
     - Automated posting
     - Data collection for commercial purposes without permission
     - Any activity that could harm Twitter's services

4. **Best Practices**:
   - Use a dedicated Twitter account for testing
   - Regularly clear your Chrome profile data
   - Monitor your Twitter account for any suspicious activity
   - Keep your ChromeDriver and Chrome browser updated

## Features

- Scrape tweets from user timelines
- Extract tweet content, metadata, and engagement metrics
- Save data in structured formats
- Handle rate limiting and pagination
- Configurable scraping parameters

## Prerequisites

- Python 3.8 or higher
- GROQ API key
- Google Chrome browser
- ChromeDriver (matching your Chrome version)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/VinVirtual/Twitter-Timeline-Scrapper-FastAPI.git
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

4. Create a `.env` file in the project root with the following configuration:
```
# API Keys
GROQ_API_KEY=your_groq_api_key_here

# Chrome Configuration
CHROME_USER_DATA_DIR=C:/Users/YourUsername/AppData/Local/Google/Chrome/User Data
CHROME_PROFILE_NAME=Default
CHROME_BINARY_LOCATION=C:/Program Files/Google/Chrome/Application/chrome.exe
CHROMEDRIVER_PATH=path/to/your/chromedriver.exe
```

### Environment Variables Explanation

- `GROQ_API_KEY`: Your Groq API key for AI-powered tweet summarization
- `CHROME_USER_DATA_DIR`: Path to your Chrome user data directory
- `CHROME_PROFILE_NAME`: Chrome profile to use (usually "Default")
- `CHROME_BINARY_LOCATION`: Path to your Chrome browser executable
- `CHROMEDRIVER_PATH`: Path to your ChromeDriver executable

### Finding Chrome Configuration Paths

1. **Chrome User Data Directory**:
   - Windows: `C:\Users\YourUsername\AppData\Local\Google\Chrome\User Data`
   - MacOS: `~/Library/Application Support/Google/Chrome`
   - Linux: `~/.config/google-chrome`

2. **Chrome Binary Location**:
   - Windows: `C:\Program Files\Google\Chrome\Application\chrome.exe`
   - MacOS: `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`
   - Linux: `/usr/bin/google-chrome`

3. **ChromeDriver**:
   - Download the appropriate version from [ChromeDriver website](https://sites.google.com/chromium.org/driver/)
   - Place it in a known location and update `CHROMEDRIVER_PATH` accordingly

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

This tool is for educational purposes only. Please ensure you comply with Twitter's Terms of Service and API usage guidelines when using this scraper. The authors are not responsible for any misuse of this tool or any consequences resulting from such misuse. 
