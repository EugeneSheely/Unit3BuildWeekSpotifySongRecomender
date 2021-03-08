import pandas as pd
import spotipycode
from flask import Flask, render_template, request
import numpy as np
import os

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

import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
users_gsheet = client.open("Lambda Unit 3 Project data server").worksheet("Sheet1")
#print(users_gsheet.get_all_records())
users_df = users_gsheet.get_all_values()
headers = users_df.pop(0)

users_df = pd.DataFrame(users_df, columns=headers)
#print(users_df)
usersK = users_df["User Name"].to_list()
usersV = users_df["Password"].to_list()
users = {}
users_index = 0
for key in usersK:
        users[key] = usersV[users_index]
        users_index = users_index +1



print(users)


#log in:
import sys


status = ""
user_name = ""

def newUser():
    createLogin = input("Create login name: ")
    login_success = False
    new_user_upload = []

    while login_success == False:


        if createLogin in users:
            print("\nLogin name already exists, please try again\n")
            createLogin = input("Create login name: ")






        else:
                createPassw = input("Create password: ")
                users[createLogin] = createPassw
                print("\nUser created\n")
                #Add new user to the dataframe:
                new_user_row = int(headers[-1])
                new_user_upload = [createLogin,createPassw, "", "", ""]
                #users_gsheet.insert_row(new_user_upload,2)
                users_gsheet.update_cell(new_user_row,1,createLogin)
                users_gsheet.update_cell(new_user_row,2,createPassw)


                login_success = True



    return createLogin

def oldUser():
    login = input("Enter login name: ")
    passw = input("Enter password: ")
    login_success = False
    while login_success == False:
        if login in users and users[login] == passw:
            print("\nLogin Successful!\n")
            login_success = True

        else:
            print("wrong username or password, please try again!")
            login = input("Enter login name: ")
            passw = input("Enter password: ")
    return login














#start model run
while user_name == "":
    status = input("Are you a registered user? y/n? Press q to quit")
    if status =="y":
        user_name = oldUser()

    elif status == "n":
        user_name = newUser()
    elif status == "q":
        print("quit")
        sys.exit()
    else:
        print("try again")




#create dictionary but for favorite songs:
users_df = users_gsheet.get_all_values()
headers = users_df.pop(0)
users_df = pd.DataFrame(users_df, columns=headers)
print("creating dictionaries")
#print(users_df)
usersK = users_df["User Name"].to_list()
usersV = users_df["Favorite Songs"].to_list()
users = {}
users_index = 0
for key in usersK:
    users[key] = usersV[users_index]
    users_index = users_index +1

#Dict to get row
users_df = users_gsheet.get_all_values()
headers = users_df.pop(0)
users_df = pd.DataFrame(users_df, columns=headers)
#print(users_df)
usersK = users_df["User Name"].to_list()
usersV = users_df["Row"].to_list()
usersrow = {}
users_index = 0
for key in usersK:
    usersrow[key] = usersV[users_index]
    users_index = users_index +1



#create dictionary but for song Id's:
users_df = users_gsheet.get_all_values()
headers = users_df.pop(0)
users_df = pd.DataFrame(users_df, columns=headers)

#print(users_df)
usersK = users_df["User Name"].to_list()
usersV = users_df["Song Id"].to_list()
userssongid = {}
users_index = 0
for key in usersK:
    userssongid[key] = usersV[users_index]
    users_index = users_index +1



#create dictionary but for song artists:
users_df = users_gsheet.get_all_values()
headers = users_df.pop(0)
users_df = pd.DataFrame(users_df, columns=headers)

#print(users_df)
usersK = users_df["User Name"].to_list()
usersV = users_df["Artist Name"].to_list()
userssongartist = {}
users_index = 0
for key in usersK:
    userssongartist[key] = usersV[users_index]
    users_index = users_index +1






#turn Google Sheets Data to lists:
users_favorite_songs = users.get(user_name).split(",")
users_favorite_songs_id = userssongid.get(user_name).split(",")
users_favorite_songs_artists = userssongartist.get(user_name).split(",")



#Greet and post fav songs list:
print(f"Welcome {user_name}!")

num_of_fav_songs = len(users_favorite_songs)


if num_of_fav_songs == 1 and users_favorite_songs[0] == "":
    print("You don't have any favorite songs yet...")
    num_of_fav_songs = 0
else:
    print("Your favorite songs are:\n\n")
    for i in users_favorite_songs:
        print(i)

search_new_song = False
while search_new_song == False:
    search_new_song = input("would you like to add a new favorite song? y/n or q to quit")
    if search_new_song == "y":
        found_artist = False
        while found_artist == False:

            user_artist_search = input("Search for an artists to get a list of available song names: ")
            if user_artist_search in artists_list:
                print(f"We found {user_artist_search} in our dataset! here's a list of their songs:\n\n")


                artists_songs = df_groupby[df_groupby['artists_str']== user_artist_search]
                #print(artists_songs)
                artists_songs_list = artists_songs["name"].to_list()
                song_ids_list = artists_songs["id"].to_list()

                for i in artists_songs_list:
                    print(i)

                print("\n\nPlease select one of the artists songs and we'll look for similar songs you might enjoy!")
                while found_artist == False:
                    song_input = input("Pick a song: ")
                    if song_input in artists_songs_list:

                        song_index = artists_songs_list.index(song_input)
                        print(song_ids_list)
                        song_id = song_ids_list[song_index]
                        print(f"song id is: {song_id}")
                        users_favorite_songs.append(song_input)
                        print(f"print son ids {users_favorite_songs_id}")
                        users_favorite_songs_id.append(song_id)
                        print(f"print son ids {users_favorite_songs_id}")
                        users_favorite_songs_artists.append(user_artist_search)

                        row = usersrow.get(user_name)
                        print(user_name)

                        print("len for users favorite songs:")
                        print(len(users_favorite_songs))
                        print(users_favorite_songs)
                        if num_of_fav_songs == 0:
                            favorites_str = "".join(users_favorite_songs)
                            favorites_str_id = "".join(users_favorite_songs_id)
                            favorites_str_artist = "".join(users_favorite_songs_artists)
                        else:
                            favorites_str = ",".join(users_favorite_songs)
                            favorites_str_id = ",".join(users_favorite_songs_id)
                            favorites_str_artist = ",".join(users_favorite_songs_artists)


                        users_gsheet.update_cell(int(row),3,favorites_str)
                        users_gsheet.update_cell(int(row),4,favorites_str_artist)
                        #users_gsheet.update_cell(int(row),5,users_favorite_songs_id)

                        found_artist = True
                    else:
                        print("I couldn't find that song, please try again!")



            else:
                print(f"{user_artist_search} wasn't found in the database, please try again")

            print("code ended")



    delete_song = input("would you like to delete favorite song? y/n or q to quit")
    if delete_song == "y":
        deleted_song = False
        while deleted_song == False:
            for i in users_favorite_songs:
                print(i)
            song_to_delete = input("\nWhich song do you wish to delete?")
            if song_to_delete not in users_favorite_songs:
                print("Sorry, I couldn't find that song, try again")
            else:
                artist_index = users_favorite_songs.index(song_to_delete)
                print(artist_index)
                users_favorite_songs_artists.remove(users_favorite_songs_artists[artist_index])
                print(users_favorite_songs_artists)
                users_favorite_songs.remove(song_to_delete)
                row = usersrow.get(user_name)
                print(len(users_favorite_songs))

                if len(users_favorite_songs) > 0:
                    favorites_str = ",".join(users_favorite_songs)
                    favorites_str_artist = ",".join(users_favorite_songs_artists)
                else:
                    favorites_str = "".join(users_favorite_songs)
                    favorites_str_artist = "".join(users_favorite_songs_artists)
                print(favorites_str)
                users_gsheet.update_cell(int(row),3,favorites_str)
                users_gsheet.update_cell(int(row),4,favorites_str_artist)


                deleted_song = True

#MACHINE LEARNING MODEL:

from spotipycode.oauth2 import SpotifyClientCredentials
from collections import defaultdict

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

df_fav_songs = df_groupby[df_groupby["name"].isin(users_favorite_songs)]
df_fav_songs
spotify_data = df_groupby
song_cluster_pipeline = Pipeline([('scaler', StandardScaler()),
                                  ('kmeans', KMeans(n_clusters=20,
                                                    verbose=2, n_jobs=4))],verbose=True)
X = spotify_data.select_dtypes(np.number)
number_cols = list(X.columns)
song_cluster_pipeline.fit(X)
song_cluster_labels = song_cluster_pipeline.predict(X)
spotify_data['cluster_label'] = song_cluster_labels




sp = spotipycode.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ["b45431fa8cc24106b032e2ac3234d647"],
                                                               client_secret=os.environ["cf385b16cb214bbeadbe2bc4dbbee090"]))
def find_song(name, year):

    """
    This function returns a dataframe with data for a song given the name and release year.
    The function uses Spotipy to fetch audio features and metadata for the specified song.

    """

    song_data = defaultdict()
    results = sp.search(q= 'track: {} year: {}'.format(name,
                                                       year), limit=1)
    if results['tracks']['items'] == []:
        return None

    results = results['tracks']['items'][0]

    track_id = results['id']
    audio_features = sp.audio_features(track_id)[0]

    song_data['name'] = [name]
    song_data['year'] = [year]
    song_data['explicit'] = [int(results['explicit'])]
    song_data['duration_ms'] = [results['duration_ms']]
    song_data['popularity'] = [results['popularity']]

    for key, value in audio_features.items():
        song_data[key] = value

    return pd.DataFrame(song_data)


from collections import defaultdict
from scipy.spatial.distance import cdist
import difflib

number_cols = ['valence', 'year', 'acousticness', 'danceability', 'duration_ms', 'energy', 'explicit',
               'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo']

def get_song_data(song, spotify_data):

    """
    Gets the song data for a specific song. The song argument takes the form of a dictionary with
    key-value pairs for the name and release year of the song.
    """

    try:
        song_data = spotify_data[(spotify_data['name'] == song['name'])
                                 & (spotify_data['year'] == song['year'])].iloc[0]
        return song_data

    except IndexError:
        return find_song(song['name'], song['year'])


def get_mean_vector(song_list, spotify_data):

    """
    Gets the mean vector for a list of songs.
    """

    song_vectors = []

    for song in song_list:
        song_data = get_song_data(song, spotify_data)
        if song_data is None:
            print('Warning: {} does not exist in Spotify or in database'.format(song['name']))
            continue
        song_vector = song_data[number_cols].values
        song_vectors.append(song_vector)

    song_matrix = np.array(list(song_vectors))
    return np.mean(song_matrix, axis=0)

def flatten_dict_list(dict_list):

    """
    Utility function for flattening a list of dictionaries.
    """

    flattened_dict = defaultdict()
    for key in dict_list[0].keys():
        flattened_dict[key] = []

    for dictionary in dict_list:
        for key, value in dictionary.items():
            flattened_dict[key].append(value)

    return flattened_dict


def recommend_songs(song_list, spotify_data, n_songs=10):

    """
    Recommends songs based on a list of previous songs that a user has listened to.
    """

    metadata_cols = ['name', 'year', 'artists']
    song_dict = flatten_dict_list(song_list)

    song_center = get_mean_vector(song_list, spotify_data)
    scaler = song_cluster_pipeline.steps[0][1]
    scaled_data = scaler.transform(spotify_data[number_cols])
    scaled_song_center = scaler.transform(song_center.reshape(1, -1))
    distances = cdist(scaled_song_center, scaled_data, 'cosine')
    index = list(np.argsort(distances)[:, :n_songs][0])

    rec_songs = spotify_data.iloc[index]
    rec_songs = rec_songs[~rec_songs['name'].isin(song_dict['name'])]
    return rec_songs[metadata_cols].to_dict(orient='records')



print(recommend_songs([{'name': 'Come As You Are', 'year':1991},
                       {'name': 'Smells Like Teen Spirit', 'year': 1991},
                       {'name': 'Lithium', 'year': 1992},
                       {'name': 'All Apologies', 'year': 1993},
                       {'name': 'Stay Away', 'year': 1993}],  spotify_data))