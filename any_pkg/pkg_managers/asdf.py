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

	def install_self() -> None:
		"""
		Installs asdf on the system.
		"""
		raise NotImplementedError()

	def update_all_pkgs() -> None:
		"""
		Updates the asdf package registry and upgrades any outdated packages.
		"""
		raise NotImplementedError()

	def refresh_registry() -> None:
		"""
		Updates the package manager's package registry.
		"""
		raise NotImplementedError

	def search_for_pkg(pkg_name: str, pkg_version: str=None) -> bool:
		"""
		Updates the asdf package registry and returns true if the given package can be found in the registry.
		"""
		raise NotImplementedError()

	def is_pkg_installed(pkg_name: str, pkg_version: str=None) -> None:
		"""
		Returns true if the given package is installed.
		"""
		raise NotImplementedError

	def install_pkg(pkg_name: str, pkg_version: str=None) -> None:
		"""
		Attempts to install the package using asdf.
		"""
		raise NotImplementedError()

	def accepts_config_files() -> bool:
		"""
		Returns true.

		asdf accepts .tool-versions files.
		"""
		return True

	def process_config_file(filepath) -> None:
		"""
		Processes a .tool-versions file.
		"""
		return False

	def clean_up() -> None:
		"""
		Cleans up any build artefacts or temporary files the package manager may have lying around.
		"""
		raise NotImplementedError
