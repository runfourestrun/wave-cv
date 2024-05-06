import requests


class ScrapeFlicker:
    def __init__(self, api_key, api_secret, search, n=2000):
        self.api_key = api_key
        self.api_secret = api_secret
        self.search = search
        self.n = n

    def get_urls(self):
        url = "https://api.flickr.com/services/rest/"
        params = {
            "method": "flickr.photos.search",
            "api_key": self.api_key,
            "text": self.search,
            "per_page": self.n,
            "format": "json",
            "nojsoncallback": 1,
            "extras": "url_o"
        }
        response = requests.get(url, params=params)

        # Check if request was successful
        if response.status_code != 200:
            print(f"Error fetching data: {response.status_code}")
            return []

        data = response.json()

        urls = []
        for photo in data.get('photos', {}).get('photo', []):
            url = photo.get("url_o")
            if not url:
                url = f"https://farm{photo['farm']}.staticflickr.com/{photo['server']}/{photo['id']}_{photo['secret']}_b.jpg"
            urls.append(url)

        # Provide some feedback
        print(f"Fetched {len(urls)} URLs for search term: {self.search}")

        return urls
