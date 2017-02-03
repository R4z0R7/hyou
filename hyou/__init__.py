# Copyright 2015 Google Inc. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import (
    absolute_import, division, print_function, unicode_literals)
from builtins import (  # noqa: F401
    ascii, bytes, chr, dict, filter, hex, input, int, list, map, next,
    object, oct, open, pow, range, round, str, super, zip)

from .client import Collection  # noqa: F401
from .client import Spreadsheet  # noqa: F401
from .client import Worksheet  # noqa: F401
from .client import WorksheetView  # noqa: F401

login = Collection.login

__all__ = [
    'Collection',
    'Spreadsheet',
    'Worksheet',
    'WorksheetView',
    'login',
]
