# Tue 2013-05-07 06:13:37 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.

"""Classes for running a tournament between players."""

__author__ = 'Ken Guyton'


class Entry(object):
  """An entry into a tournament with a player type."""

  def __init__(self, player_class):
    """Initialize the entry with a player class type.

    Args:
      player_class. Player.  A class of the Player type.
    """

    self.player_class = player_class
    self.scores = {}
    self.wins = 0

  def play(self, game):
    """Play for this player until the player wins.

    Args:
      game: Game.
    """

    player = self.player_class(game)
    score = len(list(player.play()))

    if score in self.scores:
      self.scores[score] += 1
    else:
      self.scores[score] = 1

    return score
