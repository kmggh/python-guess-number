"""Computer players to play using various guessing strategies."""

import random


class Player(object):
  """A player that plays the game until it wins.
  """

  def __init__(self, game, random_mod=random):
    """Initialize with a Game.

    Args:
      game: Game.  The game object should be initialized.  The player will
        play it.
      random: module.  Only provided so a fake module can be substituded
        during testing.
    """

    self.game = game
    self.random = random_mod

  def guess(self, current_min, current_max):
    """Generate a guess by splitting the range.

    It's intended that this method be overridden in the subclasses.

    Args:
      min_val: int.
      max_val: int.
    Returns:
      The int that is the guess.
    """

    raise NotImplementedError

  def play(self):
    """Play the game.  Yield guess, result pairs until the win.

    Yields:
      A tuple pair of a guess and its result, -1, 0, 1.
    """

    current_min = self.game.min
    current_max = self.game.max

    guess = self.guess(current_min, current_max)
    result = self.game.direction(guess)
    while result != 0:
      yield guess, result

      if result == -1:
        current_min = guess
      elif result == 1:
        current_max = guess

      guess = self.guess(current_min, current_max)
      result = self.game.direction(guess)

    yield guess, result


class BinaryPlayer(Player):
  """This player executes a binary search in the search range."""

  def split_range(self, min_val, max_val):
    """Find the mid value of this range and return it.

    Args:
      min_val: int.
      max_val: int.
    Returns:
      The int that is halfway between the two values.  If the range is even
      the lower value is returned.
    """

    val_range = max_val - min_val

    return int(val_range / 2.0 + min_val + 0.5)

  def guess(self, current_min, current_max):
    """Generate a guess by splitting the range.

    Args:
      min_val: int.
      max_val: int.
    Returns:
      The int that is the guess.
    """

    return self.split_range(current_min, current_max)


class RandomPlayer(Player):
  """A player that randomly guesses in the range."""

  def guess(self, current_min, current_max):
    """Generate a guess by selecting a random value on the range.

    Args:
      min_val: int.
      max_val: int.
    Returns:
      The int that is the guess.
    """

    return self.random.randrange(current_min, current_max)
