movies = [
    {
		"name":"Eternal Sunshine of the Spotless Mind",
		"director":"Michel Gondry",
		"year":2004
    },

    {
		"name":"Memento",
		"director" : "Christopher Nolan",
		"year" : 2000
    },
    {
		"name":"Requiem for a Dream",
		"director" : "Darren Aronofsky",
		"year" : 2000
    },
]

for movie in movies:
	movie_details = movie
	#print(movie_details)
	for	name,year in movie_details.items():
		print(name,year,director)
		#"""is release in {year} and was directed by {director}")"""

print("END")

