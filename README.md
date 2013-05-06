Guess Num
=========

This is the classic number guessing game, often used as an exercise in
programming classes. 

In this case I wrote this as an example of using a class in the
solution, written using test-driven development.  It's also an example
of styles and documentation that are helpful when writing code,
particularly for larger projects.  For the most part this code is PEP8
and pylint compliant.

To run
======

    ./test_guess_num2.py
    ./guess_num2.py
    ./guess_num2.py --max=200


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


Author
======

Ken Guyton
2013-05-04
