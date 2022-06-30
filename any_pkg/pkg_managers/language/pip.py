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
from interpreters.python import Python

class Pip(PackageManager):
	"""
	This class represents the interface to the pip Python package manager.
	"""

	def get_name() -> str:
		"""
		Returns 'pip'.
		"""
		return "pip"

	def get_command() -> str:
		"""
		Returns the command for pip.
		"""
		return f"{Python().get_command()} -m pip"

	def is_installed() -> bool:
		"""
		Returns true if pip is installed on the system.
		"""
		try:
			Python().run_module("pip", ["--version"])
		except:
			return False
		else:
			return True

	def install_self() -> None:
		"""
		Installs pip on the system.
		"""
		if not is_installed():
			Python().run_module("ensurepip", ["--upgrade"])

	def update_all_pkgs(self) -> None:
		"""
		Updates the pip package registry and upgrades any outdated packages.
		"""
		import pip

		packages = [dist.project_name for dist in pip.get_installed_distributions()]

		Python().run_module("pip", ["install", "--upgrade", ' '.join(packages)])

	def refresh_registry() -> None:
		"""
		Does nothing; pip has no such command.
		"""
		pass

	def search_for_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		"""
		Updates the pip package registry and returns true if the given package can be found in the registry.
		"""
		# search feature has been removed from pip, need to find an alternate way...
		raise NotImplementedError

	def is_pkg_installed(pkg_name: str, pkg_version: str=None) -> bool:
		"""
		Returns true if the given package is installed.
		"""
		installed_pkgs = [x.partition(' ').strip() for x in Python().run_module("pip", ["list"])[2:] if not x.startswith("WARNING:")]

		return pkg_name in installed_pkgs

	def install_pkg(self, pkg_name: str, pkg_version: str=None) -> None:
		"""
		Attempts to install the package using pip.
		"""
		if pkg_version is None:
			pkg_spec = pkg_name
		else:
			# TO DO: check if version string starts with ==, >=, etc
			pkg_spec = f"{pkg_name}{pkg_version}"

		Python().run_module("pip", ["install", "--compile", {pkg_spec}])

	def accepts_config_files() -> bool:
		"""
		Returns true.

		pip accepts requirements.txt files.
		"""
		return True

	def process_config_file(filepath) -> bool:
		"""
		Processes a requirements.txt file.
		"""
		Python().run_module("pip", ["install", "-r", filepath])

	def clean_up() -> None:
		"""
		Does nothing; pip has no such command.
		"""
		pass
