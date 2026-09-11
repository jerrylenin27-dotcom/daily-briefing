# Daily Briefing

A command-line tool that fetches live weather data for any city, along with a random trivia question and answer, and saves a timestamped report to a file.

## Features
- Fetches real-time weather data (temperature) for any city using the OpenWeatherMap API
- Fetches a random trivia question and answer using the Open Trivia Database API
- Saves all results, along with a timestamp, to `briefing.txt`
- Handles invalid city names gracefully (falls back to "Unavailable" instead of crashing)
- Handles connection errors gracefully (e.g. no internet connection)
- Keeps your API key secure using an environment variable, instead of hardcoding it in the source code

## Setup

1. **Install the required library:**
   pip install requests

2. **Get a free API key:**
   Sign up for a free account at [openweathermap.org](https://openweathermap.org) and generate an API key.

3. **Store your API key as an environment variable** (Windows):
   setx OPENWEATHER_API_KEY "your_key_here"
   This permanently stores your API key as an environment variable, so it never has to appear directly in the code. Close and reopen your terminal after running this command.

## Usage

Run the script from the command line, passing a city name as an argument:

python dailybriefing.py "city_name_here"

Example: python dailybriefing.py "Tokyo"

This will create (or overwrite) a `briefing.txt` file containing the city name, temperature, a trivia question and answer, and the current date and time.

## What I learned building this
- Making GET requests and handling JSON responses with the `requests` library
- Reading and using command-line arguments with `sys.argv`
- Error handling with `if`/`else` (checking HTTP status codes) and `try`/`except` (handling connection failures)
- Writing to files with Python's built-in file handling
- Working with timestamps using the `datetime` module
- Keeping secrets (API keys) out of source code using environment variables
- Using Git and GitHub for version control