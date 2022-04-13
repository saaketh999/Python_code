lottery_numbers = {13, 21, 22, 5, 8}


"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""
players = [
    {
        "name" : "sam",
        'numbers' : {13,21,5,6,8}
    },
{
    "name" : "vin",
    "numbers" : {13,14,21,2,8}
}
]
#Storing the numbers of player 1 in s1 variable
s1=players[0]["numbers"]
#Storing the numbers of player 2 in s3 variable
s3=players[1]["numbers"]
#Comparing the numbers of player 1 with lottery numbers and getting common numbers to s2
s2=s1.intersection(lottery_numbers)
#Comparing the numbers of player 2 with lottery numbers and getting common numbers to s4
s4=s3.intersection(lottery_numbers)
#finding total number of common numbers b/w lottery and customer numbers usig LENGTH {len()} function
first_player=len(s2)
second_player=len(s4)

print(f'Player {(players[0]["name"])} got {first_player}  numbers right')
print(f'Player {(players[1]["name"])} got {second_player} numbers right')
