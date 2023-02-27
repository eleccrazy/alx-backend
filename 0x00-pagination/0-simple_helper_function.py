#!/usr/bin/env python3
"""
File: 0-simple_helper_function.py
Desc: This module contains a python code related to backend
      pagination.
Author: Gizachew Bayness
Date Created: Feb 20, 2022
"""


def index_range(page, page_size):
    """Helper function"""
    last_page = page_size * page
    return (last_page - page_size, last_page)
