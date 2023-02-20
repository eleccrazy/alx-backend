#!/usr/bin/env python3
"""
File: 0-simple_helper_function.py
Desc: This module contains a python code related to backend
      pagination.
Author: Gizachew Bayness
Date Created: Feb 20, 2022
"""


def index_range(page, page_size):
    """ return a tuple of size two containing a start index and an
    end index corresponding to the range of indexes to return in
    a list for those particular pagination parameters."""
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
