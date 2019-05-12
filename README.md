# Anima Beyond Fantasy 2E dice roller

[![CircleCI](https://circleci.com/gh/AlvaroRuizDelgado/Anima_Beyond_Fantasy_dice_roller.svg?style=svg)](https://circleci.com/gh/AlvaroRuizDelgado/Anima_Beyond_Fantasy_dice_roller)

Script to roll dice for the 2nd editions of the roleplaying game.

## How to use

Make the script executable:
```shell
chmod u+x roll.py
```

For a d100 roll the format is: ./roll.py d100 modifier -d difficulty
If difficulty is not specified the result will be considered a "SUCCESS", but you will need to talk to the GM to see if it actually succeeds or not.
```shell
./roll.py d100 40 -d 60
Roll type: d100 / Modifier: 40 / Difficulty: 60 / Fail modifier: 0
 82  -->  SUCCESS (level 22)

./roll.py d100 40 -d 60 -m
Roll type: d100 / Modifier: 40 / Difficulty: 60 / Fail modifier: -1
 69  -->  SUCCESS (level 9)

./roll.py d100 40 -d 60 -c
Roll type: d100 / Modifier: 40 / Difficulty: 60 / Fail modifier: 0
 61  -->  SUCCESS (level 1)

./roll.py d100 60
Roll type: d100 / Modifier: 60 / Difficulty: 0 / Fail modifier: 0
 85  -->  SUCCESS (level 0) 

./roll.py d100 -d 40
Roll type: d100 / Modifier: 0 / Difficulty: 40 / Fail modifier: 0
 64  -->  SUCCESS (level 24)

./roll.py d100 -20 -d 50
Roll type: d100 / Modifier: -20 / Difficulty: 50 / Fail modifier: 0
 -8  -->  FAIL! (level -58)
```

For a d10 roll (difficulty 10 by default): ./roll.py d10 modifier
```shell
./roll.py d10 8
Roll type: d10 / Modifier: 8 / Difficulty: 0 / Fail modifier: 0
 14  -->  SUCCESS (level 4)

./roll.py d10 7 -d 10
Roll type: d10 / Modifier: 7 / Difficulty: 10 / Fail modifier: 0
 14  -->  SUCCESS (level 4)
```

Options:
```
    -d, --difficulty, sets the difficulty
    -m, --master, fumble threshold is reduced by 1 (i.e. '3' is not a fumble)
    -c, --closed, does not use open roll (no extra-roll on 90+)
```

## Container use

```shell
docker build -t anima_dice .
docker run --rm -it anima_dice
```

## Run the tests

```shell
python3 test_roll.py
```

Or if you install [coverage.py](https://coverage.readthedocs.io/en/latest/):
```shell
coverage run test_roll.py
coverage report -m
coverage html
open htmlcov/index.html
```

Then, instead of './roll d100 40 -d 60' --> 'docker run --rm -it anima_dice d100 40 -d 60'.

You can also pull the container from dockerhub:
https://hub.docker.com/r/alpacarider/anima_dice/
