"""
This module defines classes and global functions for creating and managing
connection to the graphlab backend server.
"""

'''
Copyright (C) 2016 Turi
All rights reserved.

This software may be modified and distributed under the terms
of the BSD license. See the LICENSE file for details.
'''

from ..util.config import DEFAULT_CONFIG as _default_local_conf


""" The global client object """
__CLIENT__ = None

""" The global graphlab server object """
__SERVER__ = None

__UNITY_GLOBAL_PROXY__ = None
