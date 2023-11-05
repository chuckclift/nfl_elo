import csv
game_scores = []

with open("2023_season.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["away_score"] and row["away_team"] and row["home_score"] and row["home_team"]:
            game_scores.append(row)
            game_scores[-1]["home_score"] = int(game_scores[-1]["home_score"])
            game_scores[-1]["away_score"] = int(game_scores[-1]["away_score"])
            game_scores[-1]["week"] = int(game_scores[-1]["week"])


# If you want to loop over every game, you do this:
for game in game_scores:
    # each game is a dictionary.  A dictionary maps keys to values
    # the Game dictionary contains keys such as "away_team", "home_team"
    # "home_score", "away_score", and "week"
    print(game)


# question: How many points have been scored by home teams so far this year? 
# Here is how we would figure it out
home_points = 0 
for game in game_scores:
    home_points += game["home_score"] # += adds the number on the left to the one on the right
print("total home points scored", home_points)


# Question: How many points have been scored by away teams? 
# The code for figuring this out will look very similar to the code 
# for finding the total home points
away_points = 0








# Bonus: How many games were won by home teams? How many games were
# won by away teams? You will need to use an if statement for this one.
home_wins = 0
away_wins = 0
