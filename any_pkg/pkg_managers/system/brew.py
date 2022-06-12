#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines the interface for the Homebrew package manager.
"""

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

from package_manager import PackageManager

class Brew(PackageManager):
	"""
	This class represents the interface to the Homebrew package manager.
	"""

	def get_name() -> str:
		"""
		Returns 'brew'.
		"""
		return "brew"

	def is_installed() -> bool:
		"""
		Returns true if Homebrew is installed on the system.
		"""
		return False

	def install_self(self) -> bool:
		"""
		Installs Homebrew on the system.
		"""
		raise NotImplementedError()

	def update_all_pkgs(self) -> None:
		"""
		Updates the Homebrew package registry and upgrades any outdated packages.
		"""
		#brew update
		#brew upgrade
		#brew cleanup
		raise NotImplementedError()

	def search_for_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		"""
		Updates the Homebrew package registry and returns true if the given package can be found in the registry.
		"""
		raise NotImplementedError()

	def install_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		"""
		Attempts to install the package using Homebrew.
		"""
		raise NotImplementedError()

	def accepts_config_files() -> bool:
		"""
		Returns true.
		"""
		return True

	def process_config_file(self, filepath) -> bool:
		"""
		Processes a Brewfile or Caskfile.
		"""
		return False
