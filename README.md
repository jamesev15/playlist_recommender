# Playlist Recommender Based on Spotify, Powered by GPT
Imagine waking up with a particular song in mind and wanting to find a playlist that captures a similar vibe. Our project leverages your Spotify music history and utilizes GPT technology to suggest playlists based on similar feelings, emotions, and moods.  

By analyzing your entire music history, GPT identifies the emotions and moods associated with each track. When you provide the name of the single you have in mind, a cosine similarity algorithm is employed to identify the closest matches within your music library.  

With this information, our playlist recommender can generate curated playlists that align with your desired music style, capturing the essence and emotional undertones of your chosen single. Whether you're seeking upbeat and energetic tunes or mellow and introspective melodies, our recommender aims to deliver a playlist tailored to your specific preferences.  

By combining the power of GPT and your personalized music history, our project provides a unique and personalized playlist recommendation experience. So sit back, relax, and let us curate the perfect playlist for you based on your musical journey so far.  

# Considerations
Set the below environment variables  
`export SPOTIFY_TOKEN=<SPOTIFY_TOKEN>`  
`export OPENAI_API_KEY=<OPENAI_API_KEY>` 

# Pre process
To extract musics from your spotify account and save in the vector store  
`PYTHONPATH=. python3 pre_process/handler.py`

# Process
Get playlist based on a music  
`PYTHONPATH=. python3 process/handler.py`

# Test
Enter the music name: *wonderwall*  
Enter the artist name: *oasis*  

## Result
Playlist:  

1. You & Me - Flume Remix | Disclosure,Eliza Doolittle,Flume  
2. Nothing Breaks Like a Heart (feat. Miley Cyrus) | Mark Ronson,Miley Cyrus  
3. Love Song (feat. Glasses) | Kazy Lambist,Glasses  
4. We Might Even Be Falling In Love (Duet) - Spotify Singles | Victoria Monét,Bryson Tiller  

