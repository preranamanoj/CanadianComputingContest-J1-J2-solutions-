#Your job is to determine how many players on a team have a star rating greater than 40.You also need to determine if the team is considered a gold team which means that all the players have a star rating greater than 40.

#note, for every point gained it is 5 stars and for every foul it is 3 minus stars

# Read the number of players
num_players = int(input("Enter number of players in team:"))

# Keep track of the number of players with a star rating greater than   40
num_players_gt_40 = 0
# Keep track of whether all players have a star rating greater than 40
is_gold_team = True

# Process each player
for i in range(num_players):
  # Read the number of points and fouls for this player
  points = int(input("Enter number points per player:"))
  fouls = int(input("Enter number of fouls per player:"))
  star_rating = 5 * points - 3 * fouls

# Update the player count and gold team status
  if star_rating > 40:
    num_players_gt_40 += 1
  else:
    is_gold_team = False

  # Output the results
print(num_players_gt_40, end='')
if is_gold_team:
  print('+')
else:
  print()

