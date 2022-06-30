#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module is a factory for PackageManager objects.
"""

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

from typing import Final

from system.factory import create_system_pkg_manager
from package_manager import PackageManager
from language.gem import Gem
from language.npm import NPM
from language.pip import Pip
from language.cargo import Cargo
from asdf import ASDF


PKG_MGR_VALID_TYPES: Final[list[str]] = ["system", "pip", "gem", "npm", "cargo", "asdf"]
"""
The list of valid package manager names.
"""

#


def create_package_manager(name:str) -> PackageManager:
	"""
	Creates a PackageManager object for the package manager with the given name.
	"""

	if name == "system":
		return create_system_pkg_manager()

	if name == "pip":
		return Pip()

	if name == "gem":
		return Gem()

	if name == "npm":
		return NPM()

	if name == "cargo":
		return Cargo()

	if name == "asdf":
		return ASDF()

	raise RuntimeError(
		    f"Unknown package manager type {name} requested! Valid types are {', \
                                                '.join(PKG_MGR_VALID_TYPES)}")

#


def create_and_initialize_package_manager(name:str):
	"""
	Creates and initializes a PackageManager object for the package manager with the given name.
	"""

	pkg_mgr: PackageManager = create_package_manager(name)

	if not pkg_mgr.is_installed():
		pkg_mgr.install_self()

	return pkg_mgr
