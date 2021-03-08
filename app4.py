from flask import Flask, render_template, request, url_for, redirect, session
from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)
app.secret_key = "hello"





@app.route("/",methods = ["POST", "GET"])
def home():
    from flask import Flask, render_template, request, url_for, redirect, session
    account = ""
    username = ""
    password = ""
    newusername = ""
    newpassword = ""
    users = {}
    favorite_songs = []
    artists_songs_list = []
    song_ids_list = []
    found_artist = ""
    found_song = ""
    found_song_to_delete = ""
    rec_based_on_fav_list = []
    rec_based_on_input_list = []


    test = ""

    if request.method =="POST":
        account = request.form["account"]
        session["account"] = account

        username = request.form["username"]
        session["username"] = username

        password = request.form["password"]
        session["password"] = password

        newusername = request.form["newusername"]
        session["newusername"] = newusername

        newpassword = request.form["newpassword"]
        session["newpassword"] = newpassword

        addnewsong = request.form["addnewsong"]
        session["addnewsong"] = addnewsong

        searchartist = request.form["searchartist"]
        session["searchartist"] = searchartist

        searchsong = request.form["searchsong"]
        session["searchsong"] = searchsong

        delete = request.form["delete"]
        session["delete"] = delete



        deletesong = request.form["deletesong"]
        session["deletesong"] = deletesong

        musicrecommendation = request.form["musicrecommendation"]
        session["musicrecommendation"] = musicrecommendation

        musicrecommendationresults = request.form["musicrecommendationresults"]
        session["musicrecommendationresults"] = musicrecommendationresults



        import sys
        import pandas as pd
        import spotipy
        from flask import Flask, render_template, request
        import numpy as np
        import os
        import request
        import requests












        spotify_df = pd.read_csv("data.csv")
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




        users_df = users_gsheet.get_all_values()
        headers = users_df.pop(0)
        users_df = pd.DataFrame(users_df, columns=headers)

        if account == "y":
            user_name = username
            password = password
        if account == "n":
            user_name = newusername
            password =newpassword
            createLogin = user_name


            createPassw = password
            users[createLogin] = createPassw
            print("\nUser created\n")
            #Add new user to the dataframe:
            new_user_row = int(headers[-1])
            new_user_upload = [createLogin,createPassw, "", "", ""]
            #users_gsheet.insert_row(new_user_upload,2)
            users_gsheet.update_cell(new_user_row,1,createLogin)
            users_gsheet.update_cell(new_user_row,2,createPassw)


















        users_df = pd.DataFrame(users_df, columns=headers)
        #print(users_df)
        usersK = users_df["User Name"].to_list()
        usersV = users_df["Password"].to_list()
        users = {}
        users_index = 0
        for key in usersK:
            users[key] = usersV[users_index]
            users_index = users_index +1


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
            favorite_songs = "You don't have any favorite songs yet..."
            num_of_fav_songs = 0
        else:
            for i in users_favorite_songs:
                favorite_songs.append(i)

        search_new_song = addnewsong
        user_artist_search = searchartist

        if search_new_song == "y":
            if user_artist_search in artists_list:
                found_artist = f"We found {user_artist_search} in our list!"
                artists_songs = df_groupby[df_groupby['artists_str']== user_artist_search]
                artists_songs_list = artists_songs["name"].to_list()
                song_ids_list = artists_songs["id"].to_list()
            else:
                found_artist = f"We could NOT found {user_artist_search} in our list!"

            song_input = searchsong
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
                found_song = f"I found the song {song_input}"

            else:
                found_song = f"I did NOT find the song {song_input}"
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


        #DELETE SONG SECTION:
        print("before delete section")
        delete_song = delete
        if delete_song == "y":
            song_to_delete = deletesong
            print("delete song is Y")
            if song_to_delete not in users_favorite_songs:
                found_song_to_delete = f"I did not find {song_to_delete} in your favorites to delete"
                print("song not found")
            else:
                print("song found")
                found_song_to_delete = f"I found {song_to_delete} in your favorites and deleted it"
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


        #SONG PREDICTION MODEL

        #from spotipycode.oauth2 import SpotifyClientCredentials
        if musicrecommendation == "y":
            from collections import defaultdict

            from sklearn.cluster import KMeans
            from sklearn.preprocessing import StandardScaler
            from sklearn.pipeline import Pipeline

            df_fav_songs = df_groupby[df_groupby["name"].isin(users_favorite_songs)]





            #df_fav_songs
            spotify_data = df_groupby




            song_cluster_pipeline = Pipeline([('scaler', StandardScaler()),
                                              ('kmeans', KMeans(n_clusters=20,
                                                                verbose=2, n_jobs=4))],verbose=True)
            X = spotify_data.select_dtypes(np.number)
            number_cols = list(X.columns)
            song_cluster_pipeline.fit(X)
            song_cluster_labels = song_cluster_pipeline.predict(X)
            spotify_data['cluster_label'] = song_cluster_labels


            from collections import defaultdict
            from scipy.spatial.distance import cdist
            import difflib

            number_cols = ['valence', 'year', 'acousticness', 'danceability', 'duration_ms', 'energy', 'explicit',
                           'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo']

            def get_song_data(song, spotify_data):

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



            #Recommendations based on the fav songs list:

            if num_of_fav_songs > 0:

                print(df_fav_songs)
                df_fav_songs_name_list = df_fav_songs['name'].tolist()
                df_fav_songs_year_list = df_fav_songs['year'].tolist()
                print(df_fav_songs_name_list)
                print(df_fav_songs_year_list)


                fave_name_index = 0
                fav_dict = {}
                fav_list = []
                for key in df_fav_songs_name_list:
                    print(key)
                    fav_dict['name'] = df_fav_songs_name_list[fave_name_index]
                    fav_dict['year'] = df_fav_songs_year_list[fave_name_index]
                    fav_list.append(fav_dict)
                    fave_name_index = fave_name_index +1


                print(fav_list)
                print(spotify_data)
                print(recommend_songs(fav_list,spotify_data))

                rec_based_on_fav_list = recommend_songs(fav_list,spotify_data)


            # ML by specific artists:

            #specific input data

            #rec_by_input_list = []
            #rec_by_input_list.append(musicrecommendationresults)
            rec_by_input_list = musicrecommendationresults.split(",")
            print(musicrecommendationresults)
            print(rec_by_input_list)
            rec_by_input_df = df_groupby[df_groupby["artists_str"].isin(rec_by_input_list)]
            print(rec_by_input_df)


            df_input_songs_name_list = rec_by_input_df['name'].tolist()
            df_input_songs_year_list = rec_by_input_df['year'].tolist()

            input_name_index = 0
            input_dict = {}
            input_list = []
            for key in df_input_songs_name_list:
                print(key)
                input_dict['name'] = df_input_songs_name_list[input_name_index]
                input_dict['year'] = df_input_songs_year_list[input_name_index]
                input_list.append(input_dict)
                input_name_index = input_name_index +1

            if musicrecommendationresults != "":
                rec_based_on_input_list = recommend_songs(input_list,spotify_data)





    return render_template("login.html", account = account, username = username, password = password, test = test,users = users, favorite_songs=favorite_songs, found_artist=found_artist, artists_songs_list=artists_songs_list, found_song=found_song , found_song_to_delete=found_song_to_delete, rec_based_on_fav_list=rec_based_on_fav_list , rec_based_on_input_list=rec_based_on_input_list)




if __name__ == "__main__":
    app.run(debug=True)