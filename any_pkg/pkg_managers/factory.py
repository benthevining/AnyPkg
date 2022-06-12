#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

from typing import Final

from system.factory import create_system_pkg_manager, create_and_initialize_system_pkg_manager
from package_manager import PackageManager, init_package_manager
from asdf import ASDF
from gem import Gem
from npm import NPM
from pip import Pip


PKG_MGR_VALID_TYPES: Final[list[str]] = ["system", "pip", "gem", "asdf", "npm"]

#


def create_package_manager(name):
	if name == "system":
		return create_system_pkg_manager()

	if name == "pip":
		return Pip()

	if name == "gem":
		return Gem()

	if name == "asdf":
		return ASDF()

	if name == "npm"
		return NPM()

	raise RuntimeError(
		    f"Unknown package manager type {name} requested! Valid types are {", \
                                                ".join(PKG_MGR_VALID_TYPES)}")

#


def create_and_initialize_package_manager(name):
	if name == "system":
		return create_and_initialize_system_pkg_manager()

	pkg_mgr: PackageManager = create_package_manager(name)

	init_package_manager(pkg_mgr)

	return pkg_mgr
