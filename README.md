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

## Step-by-Step Process

1. __Spotify Authentication:__
   
- Use Spotipy for OAuth authentication with Spotify, obtaining a token to interact with the API. The user will need to log in to their Spotify account and paste the provided URL into the console to complete the authentication. A cache token file will created so the user won't need to sign every time

![](https://github.com/AlvinChin1608/day46_100/blob/main/gif/Step%201_login.gif)

2. __User Prompt to enter the date (YYYY-MM-DD):__
   
- This step also ensures the user provides a valid date in YYYY-MM-DD format.

![](https://github.com/AlvinChin1608/day46_100/blob/main/gif/Step%201.gif)

3. __Web Scraping with BeautifulSoup:__
   
- Fetch the HTML content of the Billboard Hot 100 page for the specified date. Start scraping it using the CSS selector by identifying the specific line of code for the extraction.

- Notice that the billboard's top 100 URL

![](https://github.com/AlvinChin1608/day46_100/blob/main/gif/Screenshot%202024-07-02%20at%2016.59.01.png)

4. __Searching and collecting Spotify URLs:__

- Search for each song on Spotify and collect their URIs.

![](https://github.com/AlvinChin1608/day46_100/blob/main/gif/step%202.gif)

5. __Creating and populating Spotify Playlist:__
   
- Create a new playlist on Spotify in the user's account and add the collected song URIs.

![](https://github.com/AlvinChin1608/day46_100/blob/main/gif/Screenshot%202024-07-02%20at%2016.56.27.png)


