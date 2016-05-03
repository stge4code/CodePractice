import re
class Team:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
        self.games = 0
        self.wins = 0
        self.draws = 0
        self.defeats = 0
        self.total = 0
    def game(this, other):
        this.games += 1
        other.games += 1
        if this.score > other.score:
            this.total += 3
            this.wins += 1
            other.total += 0
            other.defeats += 1
        elif this.score == other.score:
            this.total += 1
            this.draws += 1
            other.total += 1
            other.draws += 1
        else:
            this.total += 0
            this.defeats += 1
            other.total += 3
            other.wins += 1

    def mdfyscore(self, score):
        if type(score) is str:
            self.score = int(score)
        elif type(score) is int:
            self.score = score

class Pool(dict):
    def get(self, teamname):
        if teamname not in self:
            self[teamname] = Team(teamname)
        return self[teamname]
    def printpool(self):
        for item in self.values():
            print(item.name + ':', item.games, item.wins, item.draws, item.defeats, item.total, sep=' ')


n = int(input())
data = [input().split(';') for i in range(n)]
pool = Pool()
for line in data:
    team1 = pool.get(line[0])
    team2 = pool.get(line[2])
    team1.mdfyscore(line[1])
    team2.mdfyscore(line[3])
    Team.game(team1, team2)
pool.printpool()
