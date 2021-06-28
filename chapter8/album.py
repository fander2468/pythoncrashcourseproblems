def make_album(artist_name, album_title, number_of_tracks = ''):
    album = {'person_name': artist_name, 'record_name': album_title}
    if number_of_tracks:
        album['number_of_tracks'] = number_of_tracks
    return album

great_music = make_album('David Bowie', 'Hours')
print(great_music)
great_music = make_album('Jimmy Hendrix', 'Electic Ladyland')
print(great_music)
great_music = make_album('John Lennon', 'Milk and Honey')
print(great_music)
great_music = make_album('Bob Marley', 'Robert Nesta', number_of_tracks = 4)
print(great_music)