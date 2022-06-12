#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines the interface for the npm package manager.
"""

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

from package_manager import PackageManager

class NPM(PackageManager):
	"""
	This class represents the interface to the npm package manager.
	"""

	def get_name() -> str:
		"""
		Returns 'npm'.
		"""
		return "npm"

	def is_installed() -> bool:
		"""
		Returns true if npm is installed on the system.
		"""
		return False

	def install_self(self) -> bool:
		"""
		Installs npm on the system.
		"""
		raise NotImplementedError()

	def update_all_pkgs(self) -> None:
		"""
		Updates the npm package registry and upgrades any outdated packages.
		"""
		raise NotImplementedError()

	def search_for_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		"""
		Updates the npm package registry and returns true if the given package can be found in the registry.
		"""
		raise NotImplementedError()

	def install_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		"""
		Attempts to install the package using npm.
		"""
		raise NotImplementedError()

	def accepts_config_files() -> bool:
		"""
		Returns true.
		"""
		return True

	def process_config_file(self, filepath) -> bool:
		"""
		Processes a package.json file.
		"""
		return False
