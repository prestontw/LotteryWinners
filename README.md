# LotteryWinners
Explores the 100 lottery winners riddle

## Riddle Description
One hundred participants sign up for a lottery event.
Each participant is assigned a unique number, from 1 to 100.
Corresponding to each participant is a lottery ticket with their number in a box in another room.
However, the boxes are randomly ordered.
If each participant finds their number, each of them wins a million dollars.
If even one of them does not find their number, none of them gets any money.

### Specific Details
Each participant faces the exact same room.
For example, one participant cannot leave some boxes open,
rearrange the boxes, leave a message, etc.
Additionally, once a participant has entered the room,
they are not allowed to communicate with any participant who has not tried to find their number.

### The Question
What is the best strategy for the participants that maximizes their probability of each finding their number?

### A Caveat
To avoid this being an awful probability problem,
we allow a 'beneficiary' to go into the room once before all participants go.
This beneficiary is allowed to open all of the boxes,
switch two boxes,
then the participants continue as normal.

What is the strategy for the participants and the beneficiary?
I claim that once the beneficiary goes,
if they optimally switch two boxes,
then the each participant will always get their number.
The probability without the beneficiary for 100 prisoners is ~33%.
