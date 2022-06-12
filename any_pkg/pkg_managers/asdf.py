#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines the interface for the asdf package manager.
"""

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

from package_manager import PackageManager

class ASDF(PackageManager):
	"""
	This class represents the interface to the asdf package manager.
	"""

	def get_name() -> str:
		"""
		Returns 'asdf'.
		"""
		return "asdf"

	def is_installed() -> bool:
		"""
		Returns true if asdf is installed on the system.
		"""
		return False

	def install_self(self) -> bool:
		"""
		Installs asdf on the system.
		"""
		raise NotImplementedError()

	def update_all_pkgs(self) -> None:
		"""
		Updates the asdf package registry and upgrades any outdated packages.
		"""
		raise NotImplementedError()

	def search_for_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		"""
		Updates the asdf package registry and returns true if the given package can be found in the registry.
		"""
		raise NotImplementedError()

	def install_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		"""
		Attempts to install the package using asdf.
		"""
		raise NotImplementedError()

	def accepts_config_files() -> bool:
		"""
		Returns true.
		"""
		return True

	def process_config_file(self, filepath) -> bool:
		"""
		Processes a .tool-versions file.
		"""
		return False
