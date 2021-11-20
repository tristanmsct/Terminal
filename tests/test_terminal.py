#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:50:14 2020

@author: Tristan Muscat
"""

from terminal import InputManager as im
from terminal import InputException
import unittest  # For unit testing
from unittest.mock import patch


class TestTerminal(unittest.TestCase):
    @patch("builtins.input", return_value="Hello")
    def test_readline(self, input):
        self.assertEqual(im.read_line("Input", bl_case=False, lst_values=None), "Hello")

    @patch("builtins.input", return_value="hello")
    def test_readline_case(self, input):
        with self.assertRaises(InputException):
            im.read_line("Input", bl_case=True, lst_values=["Hello"])

    @patch("builtins.input", return_value="other")
    def test_readline_intput_not_in_expected_values(self, input):
        with self.assertRaises(InputException):
            im.read_line("Input", bl_case=True, lst_values=["Hello"])

    @patch("terminal.InputManager.read_line", return_value="y")
    def test_yesno(self, input):
        self.assertTrue(im.read_yes_no("Input"))

    @patch("terminal.InputManager.read_line", return_value=15)
    def test_read_numeric_isequal(self, input):
        self.assertEqual(im.read_numeric("Input"), 15)

    @patch("terminal.InputManager.read_line", return_value=15)
    def test_read_numeric_ub(self, input):
        with self.assertRaises(InputException):
            im.read_numeric(
                "Input",
                bl_int=True,
                num_lb=0,
                num_ub=10,
                bl_inc_lb=True,
                bl_inc_ub=True,
            )

    @patch("terminal.InputManager.read_line", return_value=10)
    def test_read_numeric_ub_2(self, input):
        with self.assertRaises(InputException):
            im.read_numeric(
                "Input",
                bl_int=True,
                num_lb=0,
                num_ub=10,
                bl_inc_lb=True,
                bl_inc_ub=False,
            )

    @patch("terminal.InputManager.read_line", return_value=-5)
    def test_read_numeric_lb(self, input):
        with self.assertRaises(InputException):
            im.read_numeric(
                "Input",
                bl_int=True,
                num_lb=0,
                num_ub=10,
                bl_inc_lb=True,
                bl_inc_ub=True,
            )

    @patch("terminal.InputManager.read_line", return_value=0)
    def test_read_numeric_lb_2(self, input):
        with self.assertRaises(InputException):
            im.read_numeric(
                "Input",
                bl_int=True,
                num_lb=0,
                num_ub=10,
                bl_inc_lb=False,
                bl_inc_ub=True,
            )


if __name__ == "__main__":
    unittest.main()
