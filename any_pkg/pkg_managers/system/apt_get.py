#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines the interface for the apt-get package manager.
"""

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

from package_manager import PackageManager

class AptGet(PackageManager):
	"""
	This class represents the interface to the apt-get package manager.
	"""

	def get_name() -> str:
		"""
		Returns 'apt-get'.
		"""
		return "apt-get"

	def is_installed() -> bool:
		"""
		Returns true if apt-get is installed on the system.
		"""
		return False

	def install_self(self) -> bool:
		"""
		Installs apt-get on the system.
		"""
		raise NotImplementedError()

	def update_all_pkgs(self) -> None:
		"""
		Updates the apt-get package registry and upgrades any outdated packages.
		"""
		# apt-get update && apt-get upgrade
		raise NotImplementedError()

	def search_for_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		"""
		Updates the apt-get package registry and returns true if the given package can be found in the registry.
		"""
		# apt-get update
		raise NotImplementedError()

	def install_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		"""
		Attempts to install the package using apt-get.
		"""
		# apt-get update
		raise NotImplementedError()
