#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:58:12 2019.

@author: Tristan Muscat
"""


# =====================================================================================================================
# Error class specific to typos
# =====================================================================================================================


class InputException(Exception):
    """Typing error."""

    def __init__(self, message):
        super(InputException, self).__init__(message)


# =====================================================================================================================
# Input management module
# =====================================================================================================================


class InputManager:
    """Manager user inputs."""

    def read_line(str_prompt, bl_case=False, lst_values=None):
        """Read an input from the user after a prompt.

        The function prompt a user to enter an input, then verifies that the input is valid.

        Parameters
        ----------
        str_prompt: str
            The prompt displayed while waiting for an input.
        bl_case: boolean, optinal
            Should the program check for case. Default is False.
        set_test: set, optinal
            set of valid values the input can be. If None then the input can be anything. Default is None.

        Returns
        -------
        str_input: str
            The input validated.
        """
        str_input = input(str_prompt)  # To prompt an input.

        # Gotta be sure.
        if str_input is None:
            raise InputException("Input error !")

        # First, if the case is not important, the string and the set of valid strings are transformed in lower case.
        # The input is stored in a temporary variable to keep the original case.
        str_test = str_input
        if not bl_case:
            str_test = str_input.lower()
            if lst_values is not None:
                lst_values = {x.lower() for x in lst_values}

        # if a set is given, then we check the input is in this set.
        if lst_values is not None and str_test not in lst_values:
            raise InputException("Input error !")

        return str_input

    def read_yes_no(str_prompt, lst_pos_vals=None, lst_neg_vals=None, bl_res_bolean=True):
        """Ask a yes or no question and get the answer.

        Compare the input to a set of accepted values. Returns the answer or an indicator that the answer is valid.

        Paramters
        ---------
        str_prompt: str
            The prompt displayed while waiting for an input.
        lst_pos_vals: list, optinal
            set of positive valid values the input can be. If None then a default set is used. Default is None.
        lst_neg_vals: list, optinal
            set of negative valid values the input can be. If None then a default set is used. Default is None.
        bl_res_bolean: bool, optinal
            Should the function return the answer or indicate if the answer is valid. Default is True.

        Returns
        -------
        res:
            the response, can be a string or a boolean.
        """
        # If no set is provided for the validation, we use a default set of values.
        # We use a or here, because if one is forgotten, might as well use default for both.
        if lst_pos_vals is None or lst_neg_vals is None:
            lst_pos_vals = ['yes', 'y', 'oui', 'o']
            lst_neg_vals = ['no', 'n', 'non']

        # Now we ask the question, get the answer and check it.
        res = InputManager.read_line(str_prompt, False, lst_pos_vals + lst_neg_vals)

        # If the expected returned value is a boolean we convert it.
        if bl_res_bolean:
            res = res in lst_pos_vals

        return res

    def read_numeric(str_prompt, bl_int=True, num_lb=None, num_ub=None, bl_inc_lb=True, bl_inc_ub=True):
        """Read a numeric (integer or not) value between bonds.

        Parameters
        ----------
        str_prompt: str
            The prompt displayed while waiting for an input.
        bl_int: bool, optional
            Should the input be an integer or can it be a float.
        num_lb: num, optional
            The lower bound. The default is None.
        num_ub: num, optional
            The upper bound. The default is None.
        bl_inc_lb: bool, optional
            Should the lower bound be included or not. The default is True.
        bl_inc_ub: num, optional
            Should the upper bound be included or not. The default is True.

        Returns
        -------
        num_input:
            The input, can be an integer or a float.
        """
        str_input = InputManager.read_line(str_prompt)  # Getting the input.

        if bl_int:
            try:
                num_input = int(str_input)
            except ValueError:
                raise InputException("Input must be an integer.")
        else:
            try:
                num_input = float(str_input)
            except ValueError:
                raise InputException("Input must be numeric.")

        if (num_ub is not None and ((bl_inc_ub and num_input > num_ub) or (not bl_inc_ub and num_input >= num_ub))):
            raise InputException("Expected a smaller input.")

        if (num_lb is not None and ((bl_inc_lb and num_input < num_lb) or (not bl_inc_lb and num_input <= num_lb))):
            raise InputException("Expected a bigger input.")

        return num_input

    def force_read(fun_reader, *argv, **kwargs):
        """Loop until it gets a valid inputs.

        Ask an input and ask again if their is an error. It allows a program not to crash because of a typo.

        Parameters
        ----------
        fun_reader: function
            The function used to read an input.
        *argv: list
            The arguments of the chosen function.
        **kwargs: dict
            The arguments of the chosen function.

        Returns
        -------
        res:
            The input. Can be several types.
        """
        bl_intput_ok = False
        # While the input is not ok.
        while not bl_intput_ok:
            try:
                # calling the input function.
                str_input = fun_reader(*argv, **kwargs)
                bl_intput_ok = True
            except InputException as e:
                print(e)

        return str_input
