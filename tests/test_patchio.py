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

    """Tests for patch_args utility."""

    def setUp(self):
        self.new_args = ["some_arg", "another_arg"]
        self.original_args = sys.argv

    def test_args_change_and_change_back(self):
        """Using patch_args context manager temporarily changes sys.argv."""
        assert sys.argv != self.new_args
        with patch_args(self.new_args) as args:
            assert args is sys.argv is self.new_args
            assert sys.argv is not self.original_args
        assert sys.argv != self.new_args
        assert sys.argv is self.original_args

    def test_decorator(self):
        """Using patch_args decorator temporarily changes sys.argv."""
        @patch_args(self.new_args)
        def my_func():
            my_func.call_count += 1
            assert sys.argv is self.new_args
            assert sys.argv is not self.original_args
        my_func.call_count = 0
        assert sys.argv != self.new_args
        my_func()
        my_func()
        assert my_func.call_count == 2
        assert sys.argv != self.new_args
        assert sys.argv is self.original_args

    def test_reentrant_context_manager(self):
        cm = patch_args(self.new_args)
        with cm as args:
            assert args is sys.argv is self.new_args
            with cm as args:
                assert args is sys.argv is self.new_args
            assert sys.argv is not self.original_args
        assert sys.argv != self.new_args
        assert sys.argv is self.original_args

    def test_nestable(self):
        args1, args2 = ["first"], ["second"]
        with patch_args(args1) as args:
            assert args is sys.argv is args1
            with patch_args(args2) as args:
                assert args is sys.argv is args2
            assert sys.argv is not self.original_args
        assert sys.argv is self.original_args


if __name__ == '__main__':
    sys.exit(unittest.main())
