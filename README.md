# playlist_recommender
Playlist recommender based on your Spotify music history and powered by GPT

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

