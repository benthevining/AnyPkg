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
from sys import platform

from apk import APK
from apt import Apt
from apt_get import AptGet
from brew import Brew
from choco import Choco
from package_manager import PackageManager


SYSTEM_PKG_MGR_NAMES: Final[list[str]] = [
    "apk", "apt", "apt-get", "brew", "choco"
]

PREFERRED_SYS_PKG_MGR: str = None

#


def __create_sys_pkg_mgr(name: str) -> PackageManager:
	if name == "apk":
		return APK()

	if name == "apt":
		return Apt()

	if name == "apt-get":
		return AptGet()

	if name == "brew":
		return Brew()

	if name == "choco":
		return Choco()

	raise RuntimeError(f"Unknown system package manager {name} requested. Valid options are {', '.join(SYSTEM_PKG_MGR_NAMES)}.")

#


def create_system_pkg_manager() -> PackageManager:

	# check if the user specified a specific one
	if PREFERRED_SYS_PKG_MGR is not None:
		if not PREFERRED_SYS_PKG_MGR in SYSTEM_PKG_MGR_NAMES:
			raise RuntimeError(
			    f"Unknown system package manager {PREFERRED_SYS_PKG_MGR} requested! Valid names are {',\
			    '.join(SYSTEM_PKG_MGR_NAMES)}")

		return __create_sys_pkg_mgr(PREFERRED_SYS_PKG_MGR)

	# return an appropriate pkg mgr for the platform
	if platform == "win32":
		return __create_sys_pkg_mgr("choco")

	if platform == "darwin":
		return __create_sys_pkg_mgr("brew")

	# apt, apk

	return __create_sys_pkg_mgr("apt-get")


#


def create_and_initialize_system_pkg_manager() -> PackageManager:

	pkg_mgr: PackageManager = create_system_pkg_manager()

	print(f"Using system package manager: {pkg_mgr.get_name()}")

	if not pkg_mgr.is_installed():
		pkg_mgr.install_self()

	return pkg_mgr
