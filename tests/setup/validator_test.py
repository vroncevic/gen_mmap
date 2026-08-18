# -*- coding: UTF-8 -*-

'''
Module
    validator_test.py
Info
    Unit tests for GenMmapBundleValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from ats_utilities.base.setup.bundle import BaseBundle

from gen_mmap.core.service.iservice import IService
from gen_mmap.core.service.isubprocessor import ISubProcessor
from gen_mmap.infrastructure.cli.icli import ICLI
from gen_mmap.setup.bundle import GenMmapBundle
from gen_mmap.setup.validator import GenMmapBundleValidator


class DummyService:

    def execute(self, *, params: object) -> object:
        return None

    def is_initialized(self) -> bool:
        return True


class DummySubProcessor:

    def run(self, *, params: object) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True


class DummyCLI:

    def run(self) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True


class TestGenMmapBundleValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        bundle = GenMmapBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        GenMmapBundleValidator.validate(bundle)

    def test_validate_bundle_none(self) -> None:
        with self.assertRaises(Exception):
            GenMmapBundleValidator.validate(None)

    def test_validate_bundle_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenMmapBundleValidator.validate("invalid_bundle")

    def test_validate_missing_components(self) -> None:
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        with self.assertRaises(Exception):
            bundle = GenMmapBundle(
                base=None,
                service=dummy_service,
                subprocessor=dummy_subprocessor,
                cli=dummy_cli
            )
            GenMmapBundleValidator.validate(bundle)

    def test_validate_invalid_component_types(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        with self.assertRaises(Exception):
            bundle = GenMmapBundle(
                base="invalid",
                service=dummy_service,
                subprocessor=dummy_subprocessor,
                cli=dummy_cli
            )
            GenMmapBundleValidator.validate(bundle)

        with self.assertRaises(Exception):
            bundle = GenMmapBundle(
                base=mock_base,
                service="invalid",
                subprocessor=dummy_subprocessor,
                cli=dummy_cli
            )
            GenMmapBundleValidator.validate(bundle)

        with self.assertRaises(Exception):
            bundle = GenMmapBundle(
                base=mock_base,
                service=dummy_service,
                subprocessor="invalid",
                cli=dummy_cli
            )
            GenMmapBundleValidator.validate(bundle)

        with self.assertRaises(Exception):
            bundle = GenMmapBundle(
                base=mock_base,
                service=dummy_service,
                subprocessor=dummy_subprocessor,
                cli="invalid"
            )
            GenMmapBundleValidator.validate(bundle)

    def test_is_valid_success(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        bundle = GenMmapBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )
        self.assertTrue(GenMmapBundleValidator.is_valid(bundle))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenMmapBundleValidator.is_valid(None))
        self.assertFalse(GenMmapBundleValidator.is_valid("invalid"))
