# Spotify Playlist Recommender using GPT.
Imagine waking up with a particular song in mind and wanting to find a playlist that captures a similar vibe. The project leverages your Spotify music history and utilizes GPT technology to suggest playlists based on similar feelings, emotions, and moods.  

By analyzing your entire music history, GPT identifies the emotions and moods associated with each track. When you provide the name of the single you have in mind, a cosine similarity algorithm is employed to identify the closest matches within your music library.  

With this information, the playlist recommender can generate curated playlists that align with your desired music style, capturing the essence and emotional undertones of your chosen single. Whether you're seeking upbeat and energetic tunes or mellow and introspective melodies, the recommender aims to deliver a playlist tailored to your specific preferences.  

By combining the power of GPT and your personalized music history, the project provides a unique and personalized playlist recommendation experience. So sit back, relax, and let me curate the perfect playlist for you based on your musical journey so far.  

# Considerations
Set the below environment variables  
`export SPOTIFY_TOKEN=<SPOTIFY_TOKEN>`  
`export OPENAI_API_KEY=<OPENAI_API_KEY>` 

# Packages
`pip install -r requirements.txt`  

# Pre process
To extract musics from your spotify account and save in the vector store  
`python3 pre_process.py`

# Process
Get playlist based on a song  
`python3 process.py`

# Test
Enter the music name: *wonderwall*  
Enter the artist name: *oasis*  

## Result
Playlist:  

1. You & Me - Flume Remix | Disclosure,Eliza Doolittle,Flume
2. Je te laisserai des mots | Patrick Watson
3. Every Second | Mina Okabe
4. Turn Off The Light | Nelly Furtado
5. Tearin' up My Heart - Radio Edit | *NSYNC
6. Za Milena J. | Moriarty
7. Video Games | Lana Del Rey
8. Miss Those Days | Mina Okabe
9. Like Other People | Mina Okabe
10. cómo dormiste? | Rels B
