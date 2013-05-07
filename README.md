Guess Num
=========

This is the classic number guessing game, often used as an exercise in
programming classes. 

In this case I wrote this as an example of using a class in the
solution, written using test-driven development.  It's also an example
of styles and documentation that are helpful when writing code,
particularly for larger projects.  For the most part this code is PEP8
and pylint compliant.

In it's recent edition, the program is object-oriented with
functionality broken out into classes and it supports player
algorithms for automated play and tournaments.

To run
======

The interactive game
--------------------

    ./test_guess_num2.py
    ./guess_num2.py
    ./guess_num2.py --max=200


With automated players
----------------------

For the binary player and random player, respectively.

    ./guess_num_player.py -b
    ./guess_num_player.py -r


Tournament
----------

Pit the automated player algorithms against each other in a tournament.

    ./run_tournament --help
    usage: run_tournament.py [-h] [-m MAX] [-n NUMGAMES]

    optional arguments:
      -h, --help            show this help message and exit
      -m MAX, --max MAX     Max guess amount
      -n NUMGAMES, --numgames NUMGAMES
                            Number of games to play.

    ./run_tournament -n 100000

Typical results:

    Binary wins: 70646
    Random wins: 20142
    Ties: 9212


Release Notes
=============

Release 1.0
-----------

*2013-05-04*

The initial, working version.

Release 1.1
-----------

*2013-05-05*

Player classes were added that play the game.  The game itself was
refactored slightly so that the evaluate() method takes a direction
parameter instead of computing it on its own.

There are two player classes.  One uses a simple binary search to find
the answer.  The other randomly chooses an answer in the remaining
range, based on the response from the game.

The second random player is a subclass of the other, since they were
added one at a time.

Release 1.2
-----------

*2013-05-05*

The Player class was made abstract with sub classes for RandomPlayer
and BinaryPlayer.

Release 1.3
-----------

*2013-05-07*

There is now a tournament module with a TournamentEntry class that can
be used to have various player classes compete with each other over a
series of games.  Each player plays the same, randomly generated
game.  The tournament entry objects track the scores.

This version also fixes a bug in the previous versions where the
BinaryPlayer would always choose, on the range (0, 1) a value of 1.
The only correct answer in that case is 0.  The ranges are always
exclusive on the maximum side.


Bugs
====

This version is still limited to a fixes number of player objects
(two).  A more generalized version for an arbitrary number of players
would be nice.


Author
======

Ken Guyton
2013-05-04
