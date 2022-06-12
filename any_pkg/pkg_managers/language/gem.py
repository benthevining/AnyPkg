#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines the interface for the Ruby gems package manager.
"""

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

from package_manager import PackageManager

class Gem(PackageManager):
	"""
	This class represents the interface to the Ruby gems package manager.
	"""

	def get_name() -> str:
		"""
		Returns 'gem'.
		"""
		return "gem"

	def is_installed() -> bool:
		"""
		Returns true if gem is installed on the system.
		"""
		return False

	def install_self(self) -> bool:
		"""
		Installs gem on the system.
		"""
		raise NotImplementedError()

	def update_all_pkgs(self) -> None:
		"""
		Updates the gem registry and upgrades any outdated gems.
		"""
		raise NotImplementedError()

	def search_for_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		"""
		Updates the gem registry and returns true if the given gem can be found in the registry.
		"""
		raise NotImplementedError()

	def install_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		"""
		Attempts to install the gem.
		"""
		raise NotImplementedError()

	def accepts_config_files() -> bool:
		"""
		Returns true.
		"""
		return True

	def process_config_file(self, filepath) -> bool:
		"""
		Processes a Gemfile.
		"""
		return False
