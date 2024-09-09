#!/usr/bin/env python3
"""Test for utils.py"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize

from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"])
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map exception
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, expected):
        """test that utils.get_json returns the expected result"""
        mock = Mock()
        mock.json.return_value = expected
        with patch('requests.get', return_value=mock):
            self.assertEqual(get_json(test_url), expected)


class TestMemoize(unittest.TestCase):
    """Test memoize
    """
    def test_memoize(self):
        """Test memoize
        """
        class TestClass:
            """A testing class"""

            def a_method(self):
                """a method"""
                return 42

            @memoize
            def a_property(self):
                """a memoized method"""
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            self.assertEqual(test_obj.a_property, 42)
            self.assertEqual(test_obj.a_property, 42)
            mock_method.assert_called_once()
