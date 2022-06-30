#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines the PackageManager interface class.
"""

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

from shutil import which

#

class PackageManager:
	"""
	This class is a common interface to any kind of package manager.
	"""

	def get_name() -> str:
		"""
		Returns the name of the package manager.
		"""
		raise NotImplementedError

	def get_command() -> str:
		"""
		Returns the command for the package manager.

		This is usually the same as its name.
		"""
		return get_name()

	def is_installed() -> bool:
		"""
		Returns true if the package manager is installed.
		"""
		return which(get_command()) is not None

	def install_self() -> None:
		"""
		Installs the package manager.

		The implementation of this method must use the lowest-level system resources as possible, and would preferably be pure Python code with no external
		dependencies.
		"""
		raise NotImplementedError

	def update_all_pkgs() -> None:
		"""
		Updates all the packages this package manager manages.
		"""
		raise NotImplementedError

	def refresh_registry() -> None:
		"""
		Updates the package manager's package registry.
		"""
		raise NotImplementedError

	def search_for_pkg(pkg_name: str, pkg_version: str=None) -> bool:
		"""
		Returns true if a matching package can be found in this package manager's registry.
		"""
		raise NotImplementedError

	def is_pkg_installed(pkg_name: str, pkg_version: str=None) -> bool:
		"""
		Returns true if the given package is installed.
		"""
		raise NotImplementedError

	def install_pkg(pkg_name: str, pkg_version: str=None) -> None:
		"""
		Installs the requested package.
		"""
		raise NotImplementedError

	def install_pkgs(pkgs: list[tuple[str, str]]) -> None:
		"""
		Installs multiple packages at once.
		"""
		for pair in pkgs:
			install_pkg(pair[0], pair[1])

	def accepts_config_files() -> bool:
		"""
		Returns true if this package manager can be fed an external configuration file (like a Brewfile, requirements.txt, package.json, Gemfile, etc).
		"""
		return False

	def process_config_file(filepath) -> None:
		"""
		Processes an external configuration file.
		"""
		raise NotImplementedError

	def clean_up() -> None:
		"""
		Cleans up any build artefacts or temporary files the package manager may have lying around.
		"""
		raise NotImplementedError
