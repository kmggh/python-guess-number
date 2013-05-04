#!/usr/bin/env python
# Fri 2013-05-03 23:49:55 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.


"""A game for guessing a number.  Used as a Python class example.

We randomly choose a number then the user enters guesses.  The game says
it's high or low.
"""

__author__ = 'Ken Guyton (monolith149.com)'


import random
import argparse

MAX_DEFAULT = 100
MIN_DEFAULT = 0

MAP = {-1: 'low', 1: 'high'}


class Game(object):
  """The game which includes setting the number and tracking guesses."""

  def __init__(self, min_val=MIN_DEFAULT, max_val=MAX_DEFAULT,
               random_mod=random):
    """Set limits on the number to guess.

    Args:
      min_val: int.
      max_val: int.
      random: module.  Only provided so a fake module can be substituded
        during testing.
    """

    self.random = random_mod
    self.min = min_val
    self.max = max_val
    self.num_to_guess = self.random.randrange(min_val, max_val)

    self.won = False
    self.count = 0

  def direction(self, guess):
    """Convert the difference into a -1, 0, 1 to easily indicate  high/low.

    Args:
      guess: int.
    Returns:
      A -1, 0 or 1.  The -1 means the guess was low.  A 1 means it was high.
      Of course, 0 means correct.
    """

    diff = guess - self.num_to_guess

    if diff == 0:
      return diff
    else:
      return diff / abs(diff)

  def evaluate(self, guess):
      """Evaluate the guess and return a str message.

      Args:
        guess: int.  The number we are guessing.
      Returns:
        A str which is a message indicating too low, too high or correct!
      """

      result = self.direction(guess)
      self.count += 1

      if result == 0:
        self.won = True
        return '{0} is correct!  You won!'.format(guess)
      else:
        return '{0} is {1}.'.format(guess, MAP[result])


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-m', '--max', help='Max guess amount', type=int)
  args = parser.parse_args()

  if args.max:
    game = Game(max_val=args.max)
  else:
    game = Game()

  while not game.won:
    guess = raw_input(
      'Please enter a number from {0} to {1}: '.format(game.min, game.max))
    print game.evaluate(int(guess))

  print 'You guessed {0} times.'.format(game.count)


if __name__ == '__main__':
  main()
