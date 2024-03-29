#!/usr/bin/env python3
"""
Created on Tue Aug 11 11:50:14 2020

@author: Tristan Muscat
"""
import unittest  # For unit testing
from unittest.mock import patch

import inputmanager as im
from inputmanager import InputException


class TestTerminal(unittest.TestCase):
    @patch("builtins.input", return_value="Hello")
    def test_readline(self, input):
        self.assertEqual(im.read_line("Input", bl_case=False, set_values=None), "Hello")

    @patch("builtins.input", return_value=None)
    def test_readline_none(self, input):
        with self.assertRaises(InputException):
            im.read_line("Input", bl_case=False, set_values=None)

    @patch("builtins.input", return_value="hello")
    def test_readline_case(self, input):
        with self.assertRaises(InputException):
            im.read_line("Input", bl_case=True, set_values=["Hello"])

    @patch("builtins.input", return_value="other")
    def test_readline_intput_not_in_expected_values(self, input):
        with self.assertRaises(InputException):
            im.read_line("Input", bl_case=True, set_values=["Hello"])

    @patch("builtins.input", return_value="y")
    def test_yesno(self, input):
        self.assertTrue(im.read_yes_no("Input"))

    @patch("builtins.input", return_value=15)
    def test_read_numeric_isequal(self, input):
        self.assertEqual(im.read_numeric("Input"), 15)

    @patch("builtins.input", return_value=15)
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

    @patch("builtins.input", return_value=10)
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

    @patch("builtins.input", return_value=-5)
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

    @patch("builtins.input", return_value=0)
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

    @patch("builtins.input", return_value='TEST')
    def test_read_numeric_str_for_int(self, input):
        with self.assertRaises(InputException):
            im.read_numeric(
                "Input",
                bl_int=True,
                num_lb=0,
                num_ub=10,
                bl_inc_lb=True,
                bl_inc_ub=True,
            )

    @patch("builtins.input", return_value='TEST')
    def test_read_numeric_str_for_float(self, input):
        with self.assertRaises(InputException):
            im.read_numeric(
                "Input",
                bl_int=False,
                num_lb=0,
                num_ub=10,
                bl_inc_lb=True,
                bl_inc_ub=True,
            )

    @patch("builtins.input", return_value="Hello")
    def test_force_read(self, input):
        self.assertEqual(
            im.force_read(im.read_line, "Input", bl_case=False, set_values=None),
            "Hello",
        )

    @patch("builtins.input", side_effect=['TEST', 7])
    def test_force_read_error(self, input):
        self.assertEqual(
            im.force_read(im.read_numeric, "Input", bl_int=True, num_lb=0, num_ub=10),
            7,
        )


if __name__ == "__main__":
    unittest.main()
