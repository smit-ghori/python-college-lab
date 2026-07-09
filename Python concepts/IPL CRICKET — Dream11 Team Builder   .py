#   🏏 IPL CRICKET — Dream11 Team Builder   You are building a mini Dream11-style app for the IPL. Every Player has a name, team, role (Batsman/Bowler/All-rounder/Wicketkeeper), credits (float), and points_scored (int). A Captain earns 2× points and a Vice-Captain earns 1.5× points. The app must also track how many total players have been added across all teams in the fantasy league.

# Design a Python Player class and a Captain subclass to model the above. Include: a constructor for Player with all attributes, a method get_fantasy_points() that returns points_scored, override this method in Captain to return 2× points, a class variable total_players that increments with each object created, and a __str__ method that prints: 'Rohit Sharma (MI) — Batsman — 9.5 credits'. Write driver code creating 2 players and 1 captain, print their fantasy points.


class Player:

    total_player = 0

    def __init__(self, player_name, team, role, credit, point_score):
        self.player_name = player_name
        self.team = team
        self.role = role
        self.credit = credit
        self.point_score = point_score

        Player.total_player += 1
        
    def __str__(self):
        return f"{self.player_name} | {self.team} | {self.role} | {self.credit} | {self.point_score}"

    def get_fantasy_points(self):
        return self.point_score


class Captain(Player):

    def get_fantasy_points(self):
        return self.point_score * 2


# Driver Code
player1 = Player("Virat Kohli", "RCB", "Batsman", 10.0, 75)
player2 = Player("Jasprit Bumrah", "MI", "Bowler", 9.0, 60)
captain = Captain("Rohit Sharma", "MI", "Batsman", 9.5, 80)

# Print player details
print(player1)
print(player2)
print(captain)

print()

# Print fantasy points
print(f"{player1.player_name} Fantasy Points:", player1.get_fantasy_points())
print(f"{player2.player_name} Fantasy Points:", player2.get_fantasy_points())
print(f"{captain.player_name} Fantasy Points:", captain.get_fantasy_points())

print()

# Print total players created
print("Total Players Created:", Player.total_player)