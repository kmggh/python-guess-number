#!/usr/bin/env python
# Sun 2013-05-05 23:13:57 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.

"""Play the number guessing with various software players.

This version pits the binary player vs. the random player.
"""

__author__ = 'Ken Guyton'

import argparse
import guess_num2
import player
import sys
import tournament


def parse_args():
  """Parse the command line args for main."""

  parser = argparse.ArgumentParser()
  parser.add_argument('-m', '--max', help='Max guess amount', type=int,
                      default=100)
  parser.add_argument('-n', '--numgames', help='Number of games to play.',
                      default=1000, type=int)

  return parser.parse_args()


def compute_report_increment(args):
  """Compute the report increment.

  A number is printed out for every increment games that have been played.

  Args:
    args:  The args from args parse.
  Returns:
    An int.
  """

  report_increment = args.numgames / 100
  if report_increment >= 1000:
    report_increment *= 10

  return report_increment


def print_report_increment(i, report_increment):
  """Report on how many games have been played."""

  if not i % report_increment:
    print '{0}...'.format(i),
    sys.stdout.flush()


def count_scores(b_entry, r_entry, b_score, r_score, ties):
  """Increment the win or ties."""

  if b_score < r_score:
    b_entry.wins += 1
  elif r_score < b_score:
    r_entry.wins += 1
  else:
    ties += 1

  return ties


def report_scores(title, entry):
  """Report the scores for an entry.

  Args:
    title: str.  The title before the report.
    entry: Entry.  The entry object.
  """

  print
  print '{0}.'.format(title)
  print 'score', 'count'
  for score in sorted(entry.scores.keys()):
    print score, entry.scores[score]


def report_wins(b_entry, r_entry, ties):
  """Report on the counts of wins and ties."""

  print 'Binary wins:', b_entry.wins
  print 'Random wins:', r_entry.wins
  print 'Ties:', ties


def main():
  args = parse_args()
  report_increment = compute_report_increment(args)
  ties = 0

  print 'Playing {0} games.'.format(args.numgames)

  b_entry = tournament.Entry(player.BinaryPlayer)
  r_entry = tournament.Entry(player.RandomPlayer)

  for i in range(args.numgames):
    print_report_increment(i, report_increment)

    game = guess_num2.Game(max_val=args.max)
    b_score = b_entry.play(game.clone())
    r_score = r_entry.play(game.clone())

    ties = count_scores(b_entry, r_entry, b_score, r_score, ties)

  report_scores('Binary scores', b_entry)
  report_scores('Randmo scores', r_entry)
  report_wins(b_entry, r_entry, ties)


if __name__ == '__main__':
  main()
