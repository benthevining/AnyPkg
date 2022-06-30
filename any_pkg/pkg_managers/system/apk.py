#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines the interface for the apk package manager.
"""

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

from package_manager import PackageManager

class APK(PackageManager):
	"""
	This class represents the interface to the apk package manager.
	"""

	def get_name() -> str:
		"""
		Returns 'apk'.
		"""
		return "apk"

	def install_self() -> None:
		"""
		Installs apk on the system.
		"""
		raise NotImplementedError()

	def update_all_pkgs() -> None:
		"""
		Updates the apk package registry and upgrades any outdated packages.
		"""
		raise NotImplementedError()

	def refresh_registry() -> None:
		"""
		Updates the package manager's package registry.
		"""
		raise NotImplementedError

	def search_for_pkg(pkg_name: str, pkg_version: str=None) -> bool:
		"""
		Updates the apk package registry and returns true if the given package can be found in the registry.
		"""
		raise NotImplementedError()

	def is_pkg_installed(pkg_name: str, pkg_version: str=None) -> bool:
		"""
		Returns true if the given package is installed.
		"""
		raise NotImplementedError

	def install_pkg(pkg_name: str, pkg_version: str=None) -> None:
		"""
		Attempts to install the package using apk.
		"""
		raise NotImplementedError()

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
