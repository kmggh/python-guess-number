#!/usr/bin/env python
# Fri 2013-05-03 23:44:30 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.

"""Test the guess num game classes."""

__author__ = 'Ken Guyton'

import unittest
import guess_num2

NUM_TO_GUESS = 42
HIGH_GUESS = 50
LOW_GUESS = 21


class FakeRandom(object):
  """Fake the random module."""

  def randrange(self, min_val, max_val):
    """Return a known and predictable number for testing."""

    return NUM_TO_GUESS


class TestGame(unittest.TestCase):
  def setUp(self):
    self.game = guess_num2.Game(random_mod=FakeRandom())

  def test_create(self):
    self.assertNotEqual(self.game, None)
    self.assertEqual(self.game.num_to_guess, NUM_TO_GUESS)
    self.assertEqual(self.game.min, guess_num2.MIN_DEFAULT)
    self.assertEqual(self.game.max, guess_num2.MAX_DEFAULT)
    self.assertEqual(self.game.count, 0)

  def test_direction_low(self):
    self.assertEqual(self.game.direction(LOW_GUESS), -1)

  def test_direction_high(self):
    self.assertEqual(self.game.direction(HIGH_GUESS), 1)

  def test_direction_correct(self):
    self.assertEqual(self.game.direction(NUM_TO_GUESS), 0)

  def test_evaluate_guess_low(self):
    self.assertEqual(self.game.evaluate(LOW_GUESS, -1),
                     '{0} is low.'.format(LOW_GUESS))
    self.assertFalse(self.game.won)

  def test_evaluate_guess_high(self):
    self.assertEqual(self.game.evaluate(HIGH_GUESS, 1),
                     '{0} is high.'.format(HIGH_GUESS))
    self.assertFalse(self.game.won)

  def test_evaluate_correct_high(self):
    self.assertEqual(self.game.evaluate(NUM_TO_GUESS, 0),
                     '{0} is correct!  You won!'.format(NUM_TO_GUESS))
    self.assertTrue(self.game.won)

  def test_count(self):
    self.game.evaluate(LOW_GUESS, -1)
    self.game.evaluate(LOW_GUESS, -1)
    self.game.evaluate(LOW_GUESS, -1)
    self.assertEqual(self.game.count, 3)


if __name__ == '__main__':
  unittest.main()
