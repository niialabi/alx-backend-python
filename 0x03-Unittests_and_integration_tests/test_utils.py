#!/usr/bin/env python3
""" unittests for  utils.py """

import unittest
from typing import Any, Mapping, Sequence, Dict
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, Mock
import requests


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping,
        path: Sequence
    ):
        """ test exceptions for access nested map fun """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ unittest test get json  method """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict):
        """ test method if expected results is returned """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response) as mock_get:
            output = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(output, test_payload)


class TestMemoize(unittest.TestCase):
    """ unittest for  test_memoize method """

    def test_memoize(self):
        """ test memoize decorator on """
        class TestClass:
            """ class for testing """
            def a_method(self) -> int:
                """ returns int """
                return 42

            @memoize
            def a_property(self) -> int:
                """ test property """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked_method:
            mocked_method.return_value = 42
            dummy = TestClass()
            result_1 = dummy.a_property
            result_2 = dummy.a_property

        dummy = TestClass()
        result_1 = dummy.a_property
        result_2 = dummy.a_property

        mocked_method.assert_called_once()
        self.assertEqual(result_1, 42)
        self.assertEqual(result_2, 42)
