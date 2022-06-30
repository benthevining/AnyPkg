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
from utils.shell import execute

class NPM(PackageManager):
	"""
	This class represents the interface to the npm package manager.
	"""

	def get_name() -> str:
		"""
		Returns 'npm'.
		"""
		return "npm"

	def install_self() -> bool:
		"""
		Installs npm on the system.
		"""
		raise NotImplementedError()

	def update_all_pkgs() -> None:
		"""
		Updates the npm package registry and upgrades any outdated packages.
		"""
		execute("npm update -g")
		execute("npm update")

	def refresh_registry() -> None:
		"""
		Refreshes the npm package index.
		"""
		execute("npm ping")

	def search_for_pkg(pkg_name: str, pkg_version: str=None) -> bool:
		"""
		Updates the npm package registry and returns true if the given package can be found in the registry.
		"""
		refresh_registry()

		if pkg_version is None:
			pkg_spec = pkg_name
		else:
			pkg_spec = f"{pkg_name}@{pkg_version}"

		output = execute(f"npm search {pkg_spec}")

		return not output.startswith("No matches found for")

	def is_pkg_installed(pkg_name: str, pkg_version: str=None) -> bool:
		"""
		Returns true if the given package is installed.
		"""
		# npm ls is specific to one directory and fails if any requirements are missing
		raise NotImplementedError()

	def install_pkg(pkg_name: str, pkg_version: str=None) -> None:
		"""
		Attempts to install the package using npm.
		"""
		if pkg_version is None:
			pkg_spec = pkg_name
		else:
			pkg_spec = f"{pkg_name}@{pkg_version}"

		execute(f"npm install {pkg_spec}")

	def accepts_config_files() -> bool:
		"""
		Returns true.

		npm accepts package.json files.
		"""
		return True

	def process_config_file(filepath) -> None:
		"""
		Processes a package.json file.
		"""
		execute("npm install", workdir=os.path.realpath(os.dirname(filepath)))

	def clean_up() -> None:
		"""
		Does nothing; npm has no such command.
		"""
		pass
