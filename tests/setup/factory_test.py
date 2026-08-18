# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenMmapBundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_mmap.setup.bundle import GenMmapBundle
from gen_mmap.setup.factory import GenMmapBundleFactory


class TestGenMmapBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenMmapBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenMmapBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_mmap/infrastructure/config/gen_mmap.cfg'}
        bundle = GenMmapBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenMmapBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenMmapBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenMmapBundleFactory.get_version(), '1.0.5')
