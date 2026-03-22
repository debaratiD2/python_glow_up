'''dictionary-->collection of data that stores data in key-value pairs'''
song = {
    1: 'make you mine',
    2: 'let me love you',
    3: 'as you are'

}
print(song)
song[4] = 'perfect'
print(song)
print(song[2])
print(song[1][0:])
print(sorted(song))
val1 = "let me love you" in song
print(val1)
val2 = "as you are" in song.values()
print(val2)
val3 = 5 not in song
print(val3)