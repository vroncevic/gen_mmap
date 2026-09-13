# -*- coding: UTF-8 -*-

'''
Module
    gen_mmap_command_test.py
Info
    Unit tests for GenMmapCommandDefinition and GenMmapCommandExecutor.
'''

from __future__ import annotations

from unittest import TestCase
from unittest.mock import Mock

from gen_mmap.core.service.iservice import IService
from gen_mmap.infrastructure.command.gen_mmap_command_definition import GenMmapCommandDefinition
from gen_mmap.infrastructure.command.gen_mmap_command_executor import GenMmapCommandExecutor


class TestGenMmapCommand(TestCase):

    def test_definition(self) -> None:
        definition = GenMmapCommandDefinition()
        self.assertEqual(definition.name, 'create')
        self.assertEqual(definition.help_text, 'Generate Mmap project skeleton')
        self.assertEqual(len(definition.options), 4)
        self.assertTrue(isinstance(str(definition), str))

    def test_executor_execute_success(self) -> None:
        definition = GenMmapCommandDefinition()
        executor = GenMmapCommandExecutor(definition)
        
        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = True
        mock_service.execute.return_value = {'returncode': 0}
        
        params = {'name': 'test', 'output': '.'}
        result = executor.execute(params=params, service=mock_service)
        
        self.assertEqual(result['returncode'], 0)
        mock_service.execute.assert_called_once_with(params=params)

    def test_executor_execute_not_initialized(self) -> None:
        definition = GenMmapCommandDefinition()
        executor = GenMmapCommandExecutor(definition)
        
        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = False
        
        result = executor.execute(params={}, service=mock_service)
        self.assertEqual(result['returncode'], 1)
        self.assertIn('service not initialized', result['stderr'])

    def test_executor_str_representation(self) -> None:
        definition = GenMmapCommandDefinition()
        executor = GenMmapCommandExecutor(definition)
        self.assertTrue(isinstance(str(executor), str))

    def test_executor_get_definition(self) -> None:
        definition = GenMmapCommandDefinition()
        executor = GenMmapCommandExecutor(definition)
        self.assertEqual(executor.get_definition(), definition)
