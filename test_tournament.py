#!/usr/bin/env python
# Tue 2013-05-07 06:09:34 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.

"""Test the tournament classes."""

__author__ = 'Ken Guyton'

import guess_num2
import tournament
import unittest

FAKE_RESULT = [(50, 1), (25, 1), (12, 0)]


class FakePlayer(object):
  """A fake player for testing."""

  def __init__(self, game):
    """Fake init with a game.

    Args:
      game: Game. Or a fake one.
    """

    self.game = game

  def play(self):
    """Fake play.  Return a list of guess and direction.

    Returns:
      A list of tuple pairs, each of two int.  The first is a score and the
      second is a direction which is an int in (-1, 0, 1).
    """

    return FAKE_RESULT


class TestEntry(unittest.TestCase):
  def setUp(self):
    self.entry = tournament.Entry(FakePlayer)

  def test_create(self):
    self.assertNotEqual(self.entry, None)
    self.assertEqual(self.entry.player_class, FakePlayer)
    self.assertEqual(self.entry.scores, {})
    self.assertEqual(self.entry.wins, 0)

  def test_play(self):
    game = guess_num2.Game()
    score = self.entry.play(game)
    self.assertEqual(score, len(FAKE_RESULT))


if __name__ == '__main__':
  unittest.main()
