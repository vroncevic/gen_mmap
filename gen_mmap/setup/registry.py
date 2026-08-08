# -*- coding: UTF-8 -*-

'''
Module
    registry.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_mmap is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_mmap is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Encapsulates core gen_mmap components for simplification of gen_mmap bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from gen_mmap.core.service.iservice import IService
from gen_mmap.core.service.isubprocessor import ISubProcessor
from gen_mmap.infrastructure.cli.icli import ICLI
from gen_mmap.setup.bundle import GenMmapBundle
from gen_mmap.setup.validator import GenMmapBundleValidator
from gen_mmap.setup.keys import GenMmapBundleKeys
from gen_mmap.setup.dependencies import GenMmapBundleDependencies
from gen_mmap.setup.dep_validator import GenMmapBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_mmap'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_mmap/blob/dev/LICENSE'
__version__ = '1.0.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenMmapBundleRegistry:
    '''
        Encapsulates core gen_mmap components for simplification of gen_mmap bundle.

        It defines:

            :methods:
                | create_bundle - Creates the gen_mmap bundle.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenMmapBundleDependencies) -> GenMmapBundle:
        '''
            Creates the gen_mmap bundle.

            :param dependencies: The gen_mmap bundle dependencies.
            :return: The gen_mmap bundle.
            :exceptions:
                | ATSValueError: The gen_mmap bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_mmap bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_mmap bundle must be provided and have proper values.
                | ATSTypeError:  The gen_mmap bundle must be an instance of GenMmapBundle and
                |                its attributes must be instances of their respective types.
        '''
        GenMmapBundleDependenciesValidator.validate(dependencies)

        base: BaseBundle | None = dependencies.get(GenMmapBundleKeys.DEPENDENCY_BASE) if dependencies else None
        service: IService | None = dependencies.get(GenMmapBundleKeys.DEPENDENCY_SERVICE) if dependencies else None
        subprocessor: ISubProcessor | None = dependencies.get(GenMmapBundleKeys.DEPENDENCY_SUBPROCESSOR) if dependencies else None
        cli: ICLI | None = dependencies.get(GenMmapBundleKeys.DEPENDENCY_CLI) if dependencies else None

        bundle: GenMmapBundle = GenMmapBundle(base=base, service=service, subprocessor=subprocessor, cli=cli)

        GenMmapBundleValidator.validate(bundle)

        return bundle
