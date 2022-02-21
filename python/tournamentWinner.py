def tournamentWinner(competitions, results):
    bestTeam = ''
    HOMETEAMWINS = 1
    scores = {bestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == HOMETEAMWINS else awayTeam

        updateScore(winningTeam, scores)

        if scores[winningTeam] > scores[bestTeam]:
            bestTeam = winningTeam
    return bestTeam

def updateScore(winner, scores):
    if winner not in scores:
        scores[winner] = 0
    scores[winner] += 1
