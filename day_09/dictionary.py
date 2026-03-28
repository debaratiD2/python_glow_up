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

country_capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
}
print(country_capitals)
print(country_capitals["USA"]) 
country_capitals["Germany"] = "Berlin"
country_capitals["Phillippines"] = "Manila"
print(country_capitals)
del country_capitals["USA"]
print(country_capitals)
my_dict = {}
my_dict["name"] = "Alice"
my_dict["age"] = 30
print(my_dict)

# Update the age
my_dict["age"] = 31
print(my_dict)

# Delete the age
del my_dict["age"]
print(my_dict)


