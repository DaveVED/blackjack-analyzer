# blackjack-analyzer
Project I usesed to learn some more reinforcement machine learning appraches, as well as tackle a quesiton posted on twitter, see `Probelm Statement` below.

## Problem Statement
For the rest of your life if the option presented it's self would you rather be delt 18 every hand in blackjack or play your normal style.

## Solution Overivew

## Getting Started (Learning)

### Are you Crazy?
This is a `brute force` implementaiton, and to start we will use the most basic implementaion of this and grow on it. If you've never worked with `gym` before you should walk through these.

#### Version 1
The most basic implementaiton of this will have the following acceptance criteria.

- [x] Player will hit until score is `>17`, once `>17` player will stay.

To execute this you can run the below and you should see an output like mine below were my `Average payout of a player after 500 rounds is -54.497` this seems bad, and if you run it a few times, you would see that the number sorta stays in the range.

```
% ./blackjack/are_you_crazy/are_you_crazy_v1.py --rounds 500 --num_players 2000
```
![Are you Crazy Version 1](/images/are_you_crazy_v1.png)