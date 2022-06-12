#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines the interface for the Chocolatey package manager.
"""

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

from package_manager import PackageManager

class Choco(PackageManager):
	"""
	This class represents the interface to the Chocolatey package manager.
	"""

	def get_name() -> str:
		"""
		Returns 'choco'.
		"""
		return "choco"

	def is_installed() -> bool:
		"""
		Returns true if Chocolatey is installed on the system.
		"""
		return False

	def install_self(self) -> bool:
		"""
		Installs Chocolatey on the system.
		"""
		raise NotImplementedError()

	def update_all_pkgs(self) -> None:
		"""
		Updates the Chocolatey package registry and upgrades any outdated packages.
		"""
		raise NotImplementedError()

	def search_for_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		"""
		Updates the Chocolatey package registry and returns true if the given package can be found in the registry.
		"""
		raise NotImplementedError()

	def install_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		"""
		Attempts to install the package using Chocolatey.
		"""
		raise NotImplementedError()
