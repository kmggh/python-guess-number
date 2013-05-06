#!/usr/bin/env python
# Fri 2013-05-03 23:49:55 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.

"""A game for guessing a number.  Used as a Python class example.

A computer player plays the game.
"""

__author__ = 'Ken Guyton'

import player
import guess_num2
import argparse

MAX_DEFAULT = 100
MIN_DEFAULT = 0

MAP = {-1: 'low', 1: 'high'}


def parse_args():
  """Parse the command line args for main."""
  
  parser = argparse.ArgumentParser()
  parser.add_argument('-m', '--max', help='Max guess amount', type=int,
                      default=100)
  parser.add_argument('-b', '--binary', action='store_true',
                      help='Use the binary player')
  parser.add_argument('-r', '--random', action='store_true',
                      help='Use the random player')

  return parser.parse_args()


def main():
  args = parse_args()
  game = guess_num2.Game(max_val=args.max)

  if args.binary:
    the_player = player.BinaryPlayer(game)
  elif args.random:
    the_player = player.RandomPlayer(game)
  else:
    the_player = player.BinaryPlayer(game)

  print 'Guessing from {0} to {1}: '.format(game.min, game.max)

  for guess, direction in the_player.play():
    print game.evaluate(guess, direction)

  print 'You guessed {0} times.'.format(game.count)


if __name__ == '__main__':
  main()
