#MACHINE LEARNING MODEL:
import pandas as pd

#Grab Spotify data and turn to DF
spotify_df = pd.read_csv("data.csv")
#print(spotify_df.head())

#Artist column is a list, turn it to a string:
spotify_df['artist_string'] = spotify_df['artists']
#Dataframe that will be manipulated with groupby:
df_groupby = spotify_df
#artist_string has quotation marks on the side, get rid of them:
df_groupby['artists_str'] = df_groupby['artists'].str[1:-1]
#print(df_groupby['artists_str'].str[1:-1])
#turn artist column to a list for loops:
artists_list = df_groupby['artists_str'].str[1:-1].to_list()
df_groupby['artists_str'] = df_groupby['artists_str'].str[1:-1]
#print(artists_list)
#Google Sheets connection (grab usernames, passwords, fav songs)

print(df_groupby.head())

get_song_reco = False
while get_song_reco == False:
    #get dataframe with favorite songs for training:
    fav_songs_df = df_groupby[df_groupby["name"] in users_favorite_songs]
    print(fav_songs_df)
