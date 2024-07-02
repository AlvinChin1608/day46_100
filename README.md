# day46_100
I am currently engaged in a 100-day Python Bootcamp, which I am documenting and sharing my progress on GitHub. The boot camp is designed to progressively intensify, allowing me to deepen my understanding and proficiency in Python programming.

Additionally, I have chosen to include the beginner, intermediate and advanced in my documentation to provide a valuable reference for my future growth and development.

-------
# Create a Spotify Playlist using the musical time machine

## Web Scraping with BeautifulSoup
I learned how to scrape data from websites using the BeautifulSoup library in Python. Specifically, I scraped the Billboard Hot 100 chart to extract song names. Here’s an overview of what I did:

- __Fetching the Webpage:__ I used the requests library to fetch the HTML content of the Billboard Hot 100 chart for a specific date provided by the user.
- __Parsing HTML:__ I parsed the fetched HTML content using BeautifulSoup.
- __Extracting Data:__ I extracted song titles from the HTML using CSS selectors.

## Spotify API Integration with Spotipy
I also integrated the scraped data with the Spotify API to create a playlist containing the top songs from the Billboard Hot 100 chart for the specified date. Here’s what I learned:

- __Using Spotipy:__ I used the Spotipy library to interact with the Spotify API.
- __OAuth Authentication:__ I implemented OAuth authentication to access the Spotify API securely.
- __Creating Playlists:__ I created a private Spotify playlist and added the top songs to it using their URIs.
