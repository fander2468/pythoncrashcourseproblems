def make_album(artist_name, album_title, number_of_tracks = ''):
    album = {'person_name': artist_name, 'record_name': album_title}
    if number_of_tracks:
        album['number_of_tracks'] = number_of_tracks
    return album

while True:
    print('Enter musician name: ')
    print('Enter p to quit')
    musician = input('Musician name: ')
    if musician == 'q':
        break
    print('Enter album title')
    album = input('Music title: ')
    if musician == 'q':
        break
    print('Enter number of tracks')
    tracks = input('Music tracks: ')
    if musician == 'q':
        break
    album_name = make_album(musician, album, number_of_tracks = tracks)
    print(album_name)