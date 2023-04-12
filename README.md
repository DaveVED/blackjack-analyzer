# blackjack-analyzer
Project I usesed to learn some more reinforcement machine learning appraches, as well as tackle a quesiton posted on twitter, see `Probelm Statement` below.

## Problem Statement
You can reference this [post](https://twitter.com/barstoolsports/status/1645507908954669059?s=20), for a full video, but in short the quesiton at hand is.
> For the rest of you life you can either always be delt a 18 in blackjack, or, you can be dealt your regular hands.

So naturally, this seemed like a fun thing to work through, with a real world example.

## Solution Overivew
Took a few appraches to sovle this, starting small, and working our way up to what seems to be a pratical solution. Outlined below are each iteration I took.

### Approach 1 - Are you crazy?
This is a `brute force` implementaiton, which will start small, and grow to support most basic rules. If you've never worked with `gym` before you should walk through these.

#### Version 1
The most basic implementaiton of this will have the following acceptance criteria.

- [x] Player will hit until score is `>=18`, once `>=18` player will stay.

To execute this you can run the below and you should see an output like mine below were my `Average payout of a player after 500 rounds is -54.497` this seems bad, and if you run it a few times, you would see that the number sorta stays in the range, i've included a chart showing me running it 10 times as well.


```
% ./blackjack/are_you_crazy/are_you_crazy_v1.py --rounds 500 --num_players 2000
```
![Are you Crazy Version 1](/images/are_you_crazy_v1.png)

| v1 | v2 | v3 | v4 | v5 | v6 | v7 | v8 | v9 | v10 | Average | 
|---| ---| ---| ---| ---| ---| ---| ---| ---| --- | --- | 
| `-53.7` | `-54.497` | `-53.966` | `-54.1205` | `-54.0535` | `-54.377` | `-54.591` | `-53.996` | `-54.3105` | `-54.246` | `-54.38575`

#### Version 2
Here we added in some more basic Black Jack logic, to hopefully ehance our odds. This implementaiton has the following acceptance criteria.

- [x] The Player will hit under *one* of the following conditions.
    - [x] If the Player's hand is a soft 17 (i.e., contains an Ace that counts as 11).
    - [x] If the dealer's face-up card is 7 or higher, and the player's hand is 12-16, the player will hit. Otherwise, the player will stay.
    - [x] If the Players hand is `<17` ***AND*** dealers hand is `>=17`.
- [x] Auto loss if Dealer is showing Ace check if total for Dealer is 21.
- [x] Player will risk `2x` or *double down* ***iff** dealers hand is `<= 16` and `>= 13`, and players hand is `[9, 10, 11]`