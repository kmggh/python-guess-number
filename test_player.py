#!/usr/bin/env python
# Fri 2013-05-03 23:44:30 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.

"""Test the guess binary player classes."""

__author__ = 'Ken Guyton'

import player
import unittest
import guess_num2

NUM_TO_GUESS = 42
HIGH_GUESS = 50
LOW_GUESS = 21

# Binary search.
EXPECTED_SEQUENCE = (
  (50, 1),
  (25, -1),
  (37, -1),
  (43, 1),
  (40, -1),
  (41, -1),
  (42, 0))

RANDOM_SEQUENCE = (
  (15, 1),
  (14, 1),
  (7, 1),
  (6, 1),
  (4, 0)
  )


class FakeRandom(object):
  """Fake the random module."""

  def randrange(self, min_val, max_val):
    """Return a known and predictable number for testing."""

    return NUM_TO_GUESS


class TestBinaryPlayer(unittest.TestCase):
  def setUp(self):
    self.game = guess_num2.Game(random_mod=FakeRandom())
    self.player = player.BinaryPlayer(self.game)

  def test_create(self):
    self.assertNotEqual(self.player, None)
    self.assertEqual(self.player.game, self.game)

  def test_sequence(self):
    play_list = list(self.player.play())
    expected_list = list(EXPECTED_SEQUENCE)
    self.assertEqual(play_list, expected_list)

  def test_split_range(self):
    self.assertEqual(self.player.split_range(0, 100), 50)
    self.assertEqual(self.player.split_range(25, 50), 37)
    self.assertEqual(self.player.split_range(38, 50), 44)
    self.assertEqual(self.player.split_range(38, 44), 41)
    self.assertEqual(self.player.split_range(41, 44), 42)
    self.assertEqual(self.player.split_range(41, 43), 42)
    self.assertEqual(self.player.split_range(0, 1), 0)
    self.assertEqual(self.player.split_range(0, 2), 1)
    self.assertEqual(self.player.split_range(0, 3), 1)

  def test_guess(self):
    self.assertEqual(self.player.guess(0, 100), 50)
    self.assertEqual(self.player.guess(25, 50), 37)
    self.assertEqual(self.player.guess(38, 50), 44)
    self.assertEqual(self.player.guess(38, 44), 41)
    self.assertEqual(self.player.guess(41, 44), 42)
    self.assertEqual(self.player.guess(41, 43), 42)
    self.assertEqual(self.player.guess(0, 1), 0)
    self.assertEqual(self.player.guess(0, 2), 1)
    self.assertEqual(self.player.guess(0, 3), 1)


class TestRandomPlayer(unittest.TestCase):
  def setUp(self):
    self.game = guess_num2.Game(random_mod=FakeRandom())
    self.player = player.RandomPlayer(self.game,
                                             random_mod=FakeRandom())

  def test_create(self):
    self.assertNotEqual(self.player, None)
    self.assertEqual(self.player.game, self.game)

  def test_guess(self):
    self.assertEqual(self.player.guess(0, 100), 42)
    self.assertEqual(self.player.guess(25, 50), 42)
    self.assertEqual(self.player.guess(38, 50), 42)
    self.assertEqual(self.player.guess(38, 44), 42)
    self.assertEqual(self.player.guess(41, 44), 42)
    self.assertEqual(self.player.guess(41, 43), 42)
    self.assertEqual(self.player.guess(0, 1), 42)
    self.assertEqual(self.player.guess(0, 2), 42)
    self.assertEqual(self.player.guess(0, 3), 42)

  def test_sequence(self):
    play_list = list(self.player.play())
    self.assertEqual(play_list, [(42, 0)])

if __name__ == '__main__':
  unittest.main()
