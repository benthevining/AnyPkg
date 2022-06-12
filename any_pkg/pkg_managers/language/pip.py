#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines the interface for the pip package manager.
"""

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

from package_manager import PackageManager

class Pip(PackageManager):
	"""
	This class represents the interface to the pip package manager.
	"""

	def get_name() -> str:
		"""
		Returns 'pip'.
		"""
		return "pip"

	def get_command() -> str:
		"""
		Returns 'python3 -m pip'.
		"""
		return "python3 -m pip"

	def is_installed() -> bool:
		"""
		Returns true if pip is installed on the system.
		"""
		return False

	def install_self(self) -> bool:
		"""
		Installs pip on the system.
		"""
		# python -m ensurepip --upgrade
		raise NotImplementedError()

	def update_all_pkgs(self) -> None:
		"""
		Updates the pip package registry and upgrades any outdated packages.
		"""
		raise NotImplementedError()

	def search_for_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		"""
		Updates the pip package registry and returns true if the given package can be found in the registry.
		"""
		raise NotImplementedError()

	def install_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		"""
		Attempts to install the package using pip.
		"""
		raise NotImplementedError()

	def accepts_config_files() -> bool:
		"""
		Returns true.
		"""
		return True

	def process_config_file(self, filepath) -> bool:
		"""
		Processes a requirements.txt file.
		"""
		return False
