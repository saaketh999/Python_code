friends_age=[{"Title": "Smith","Year_of_publication":2018,"Author":"RLD"},
             {"Title": "Vilan","Year_of_publication":2009,"Author":"DLF"},
             {"Title": "Rowdie","Year_of_publication":2010,"Author":"GSR"},
             {"Title": "Jeens","Year_of_publication":2012,"Author":"DLD"},
             {"Title": "Shirt","Year_of_publication":2022,"Author":"DNF"}
]
#print(friends_age[0])
for i in range(len(friends_age)):
    sock=friends_age[i]
    print("---------------------")
    for key in sock:
        print(f"{key}:{sock[key]}")
