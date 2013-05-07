#!/usr/bin/env python
# Copyright (c) 2012, 2013 by Ken Guyton. All Rights Reserved.

"""Run all tests."""

import os

TESTS = ('guess_num2', 'player', 'tournament')


def run_test(test_name):
  """Run a particular test."""

  print 'Running test_%s...' % test_name
  os.system('./test_%s.py' % test_name)
  print


def main():
  """Run all tests."""

  for test_name in TESTS:
    run_test(test_name)


if __name__ == '__main__':
  main()
