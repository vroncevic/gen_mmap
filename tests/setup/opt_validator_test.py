# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
Info
    Unit tests for GenMmapBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from gen_mmap.setup.opt_validator import GenMmapBundleOptionsValidator


class TestGenMmapBundleOptionsValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        options = {'info_file': 'some_path'}
        GenMmapBundleOptionsValidator.validate(options)

    def test_validate_none(self) -> None:
        with self.assertRaises(Exception):
            GenMmapBundleOptionsValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenMmapBundleOptionsValidator.validate("not_a_mapping")

    def test_validate_invalid_option_type(self) -> None:
        with self.assertRaises(Exception):
            options = {'info_file': 123}
            GenMmapBundleOptionsValidator.validate(options)

    def test_is_valid_success(self) -> None:
        options = {'info_file': 'some_path'}
        self.assertTrue(GenMmapBundleOptionsValidator.is_valid(options))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenMmapBundleOptionsValidator.is_valid(None))
        self.assertFalse(GenMmapBundleOptionsValidator.is_valid("not_a_mapping"))
        self.assertFalse(GenMmapBundleOptionsValidator.is_valid({'info_file': 123}))
