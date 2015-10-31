#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_patchio
----------------------------------

Tests for `patchio` module.
"""

import unittest
import sys

from patchio import patch_args


class TestPatchArgs(unittest.TestCase):

    def setUp(self):
        self.args = ["some_arg", "another_arg"]

    def test_args_change_and_change_back(self):
        """Using patch_args context manager temporarily changes sys.argv."""
        original_args = sys.argv
        assert sys.argv != self.new_args
        with patch_args(self.new_args) as args:
            assert args is sys.argv is self.new_args
            assert sys.argv is not original_args
        assert sys.argv != self.new_args
        assert sys.argv is original_args

    def test_decorator(self):
        """Using patch_args decorator temporarily changes sys.argv."""
        @patch_args(self.new_args)
        def my_func(yay):
            my_func.call_count += 1
            assert sys.argv is self.new_args
            assert sys.argv is not original_args
        my_func.call_count = 0
        original_args = sys.argv
        assert sys.argv != self.new_args
        my_func()
        my_func()
        assert my_func.call_count == 2
        assert sys.argv != self.new_args
        assert sys.argv is original_args


if __name__ == '__main__':
    sys.exit(unittest.main())
