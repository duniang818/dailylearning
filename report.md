# I choose the Option 1
```
Develop a custom heuristic (must not be one of the heuristics from lectures, and cannot only be a combination of the number of liberties available to each agent)
```
# And I have developed a simple custom heuristic search for the knight, here are the key idea.
- If I am the first player, I will choose the center location, says 57, as the first move.
- If I am the second player, and in this situation I will choose the open liberties from the opponent, at most have 8 candidates. The more liberties they have the higher probability might be chosen.
- At other moves, the main thought is I split the board into 4 quadrants, (*e.g. I, II, III, IV*), the program will judge the self player current locate in which quadrant, and his correspond liberties will fall into the same quadrant score higher. The aim is to force the opponent move into the other quadrants and moves ahead one direction. Namely as the opponent always chooses the NNE direction, then his road will become narrower and narrower.
- The total score are the sum of length and each legal liberties' score  

# There are results of matches.




 