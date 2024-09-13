import requests, time, json, os
from datetime import datetime, timedelta
from tqdm import tqdm

def generate_date_ranges(start_year, end_year):
    date_ranges = []
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            start_date = datetime(year, month, 1)
            end_date = (start_date + timedelta(days=32)).replace(day=1) - timedelta(days=1)
            date_ranges.append(f"{start_date.date()}..{end_date.date()}")
    return date_ranges

def save_progress(progress, filename='script/progress.json'):
    with open(filename, 'w') as f:
        json.dump(progress, f)

def load_progress(filename='script/progress.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return {}

def fetch_repositories_sorted_by_stars(token, languages=['C++', 'C'], per_page=100, filename='script/repositories.json', start_year=2008, end_year=datetime.now().year):
    progress = load_progress()
    date_ranges = generate_date_ranges(start_year, end_year)
    
    for language in languages:
        for date_range in tqdm(date_ranges, desc=f"Fetching {language} repositories"):
            if language in progress and date_range in progress[language]:
                print(f"Skipping {language} {date_range} (already fetched)")
                continue

            url = f'https://api.github.com/search/repositories?q=language:{language}+created:{date_range}&sort=stargazers_count&order=desc&per_page={per_page}'
            headers = {
                'Accept': 'application/vnd.github+json',
                'Authorization': f'token {token}'
            }

            while url:
                try:
                    response = requests.get(url, headers=headers)
                    if response.status_code == 200:
                        repositories = response.json().get('items', [])
                        
                        with open(filename, 'a', encoding='utf-8') as file:
                            for repo in repositories:
                                json.dump(repo, file)
                                file.write('\n')
                        
                        # Check for 'next' link in the headers to get the next page
                        if 'Link' in response.headers:
                            links = response.headers['Link']
                            next_link = None
                            for link in links.split(','):
                                if 'rel="next"' in link:
                                    next_link = link.split(';')[0].strip('<> ')
                                    break
                            url = next_link
                        else:
                            url = None

                        # Save progress after each successful page fetch
                        if language not in progress:
                            progress[language] = []
                        if date_range not in progress[language]:
                            progress[language].append(date_range)
                        save_progress(progress)
                    else:
                        print(f"Error fetching {language} repositories: {response.status_code}")
                        url = None

                    # Add delay to avoid hitting API rate limits
                    time.sleep(2)
                except requests.exceptions.RequestException as e:
                    print(f"Request failed: {e}. Retrying in 5 seconds...")
                    time.sleep(5)

    print(f"Results saved to {filename}")

if __name__ == "__main__":
    fetch_repositories_sorted_by_stars(token='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')
