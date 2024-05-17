def voting_system():
    parties = ["BJP", "AAP", "BSP", "SP", "NCP"]
    votes = [0, 0, 0, 0, 0]
    n = 10

    for i in range(n):
        print("Vote for a party:")
        for j in range(len(parties)):
            print(f"{j + 1}. {parties[j]}")
        vote = int(input())
        if vote >= 1 and vote <= 5:
            votes[vote - 1] += 1
        else:
            print("Invalid vote. Try again.")

    print("Votes for each party:")
    for i in range(len(parties)):
        print(f"{parties[i]}: {votes[i]} votes")
    
    # Determine the winning party
    max_votes = max(votes)
    winners = [parties[i] for i in range(len(parties)) if votes[i] == max_votes]

    if len(winners) > 1:
        print("There is a tie between the following parties:")
        for winner in winners:
            print(winner)
    else:
        print(f"The winning party is {winners[0]}")

voting_system()