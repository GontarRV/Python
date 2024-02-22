from typing import List

def MassVote(N: int, Votes: List[int]) -> str:

    number_winner = -1
    sum_votes = 0
    votes_winner = 0
    for i in range(N):
        if votes_winner < Votes[i]:
            votes_winner = Votes[i]
            sum_votes += Votes[i]
            number_winner = i + 1
        else:
            sum_votes += Votes[i]
    
    votes_percent = []
    big_percent = 0
    for i in range(N):
        percent = round(((Votes[i] / sum_votes) * 100), 3)
        votes_percent.append(percent)
        if big_percent < votes_percent[i]:
            big_percent = votes_percent[i]

    if votes_percent.count(big_percent) >= 2:
        return 'no winner'
    
    if (votes_winner / sum_votes) * 100 >= 50:
        return 'majority winner ' + str(number_winner)
    else:
        return 'minority winner ' + str(number_winner)

print(MassVote(4, [100000, 99999, 2000, 5001]))