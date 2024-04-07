#!/usr/bin/env python3
""" unittests for  utils.py """

import unittest
from typing import Any, Mapping, Sequence, Dict
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ unittest Test access_nested_map method """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping,
        path: Sequence,
        expected: Any
    ):
        """ test access nested map function """
        self.assertEqual(access_nested_map(nested_map, path), expected)
