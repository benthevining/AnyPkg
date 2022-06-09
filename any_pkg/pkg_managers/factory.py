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


PKG_MGR_VALID_TYPES: Final[list[str]] = ["system", "pip", "gem", "asdf"]

#


def create_package_manager(name):
	if not name in PKG_MGR_VALID_TYPES:
		raise RuntimeError(
		    f"Unknown package manager type {name} requested! Valid types are {", \
                        ".join(PKG_MGR_VALID_TYPES)}")

	if name == "system":
		return create_system_pkg_manager()


#


def create_and_initialize_package_manager(name):
	if name == "system":
		return create_and_initialize_system_pkg_manager()

	pkg_mgr: PackageManager = create_package_manager(name)

	init_package_manager(pkg_mgr)

	return pkg_mgr
