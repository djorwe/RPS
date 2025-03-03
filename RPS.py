import random

def player(prev_play, opponent_history=[], play_order={}):
    if prev_play:
        opponent_history.append(prev_play)
    
    # Track opponent's move sequence and predict the next move
    last_five = "".join(opponent_history[-5:])
    if last_five in play_order:
        play_order[last_five] += 1
    else:
        play_order[last_five] = 1
    
    # Predict opponent's next move
    possible_plays = [last_five[1:] + move for move in "RPS"]
    prediction = max(possible_plays, key=lambda k: play_order.get(k, 0))[-1]
    
    # Counter predicted move
    ideal_response = {"R": "P", "P": "S", "S": "R"}
    return ideal_response.get(prediction, random.choice("RPS"))
