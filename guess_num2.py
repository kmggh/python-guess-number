#!/usr/bin/env python
# Fri 2013-05-03 23:49:55 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.

"""A game for guessing a number, often used as a Python example.

In the binary ame , player, we randomly choose a number then the user enters
guesses.  The game says whether it's high or low.
"""

__author__ = 'Ken Guyton'

import random
import argparse

MAX_DEFAULT = 100
MIN_DEFAULT = 0
MAP = {-1: 'low', 1: 'high'}


class Game(object):
  """The game which includes setting the number and tracking guesses.

  This object encapsulates what we know about the game and it's methods.
  """

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

  def evaluate(self, guess, direction):
    """Evaluate the guess and return a str message.

    Args:
      guess: int.  The number we are guessing.
      direction: int. Which is 1, 0, -1 indicating high, correct, low.
    Returns:
      A str which is a message indicating too low, too high or correct!
    """

    self.count += 1

    if direction == 0:
      self.won = True
      return '{0} is correct!  You won!'.format(guess)
    else:
      return '{0} is {1}.'.format(guess, MAP[direction])


def parse_args():
  """Parse arguments for the program."""

  parser = argparse.ArgumentParser()
  parser.add_argument('-m', '--max', help='Max guess amount', type=int,
                      default=100)
  return parser.parse_args()


def main():
  args = parse_args()
  game = Game(max_val=args.max)

  while not game.won:
    guess = int(raw_input(
      'Please enter a number from {0} to {1}: '.format(game.min, game.max)))
    print game.evaluate(guess, game.direction(guess))

  print 'You guessed {0} times.'.format(game.count)


if __name__ == '__main__':
  main()
