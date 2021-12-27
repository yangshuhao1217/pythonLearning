def make_album(name_artist, album_title, number_songs=None):
    """Make albums that include artists names and album titles, even number of songs."""
    album = {'n_artist': name_artist, 'a_title': album_title}
    if number_songs:
        album['number_songs'] = number_songs
    return album

while True:
    print("\nPlease tell me name of your favorite artist!")
    print("\n(enter 'q' at any time to quit)")

    artist = input("Artist name: ")
    if artist == 'q':
        break
    title = input("Title: ")
    if title == 'q':
        break
    album = make_album(artist, title)
    print(album)
