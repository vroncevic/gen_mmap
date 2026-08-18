# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenMmapBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_mmap.setup.keys import GenMmapBundleKeys


class TestGenMmapBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenMmapBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenMmapBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenMmapBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenMmapBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenMmapBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenMmapBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenMmapBundleKeys.OPTION_INFO_FILE, opts)
