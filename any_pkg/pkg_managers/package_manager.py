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

#


# - clean up
# - refresh package registry
class PackageManager:
	"""
	This class is a common interface to any kind of package manager.
	"""

	def get_name() -> str:
		"""
		Returns the name of the package manager.
		"""
		raise NotImplementedError()

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
		raise NotImplementedError()

	def install_self(self) -> bool:
		"""
		Installs the package manager.
		"""
		raise NotImplementedError()

	def update_all_pkgs(self) -> None:
		"""
		Updates all the packages this package manager manages.
		"""
		raise NotImplementedError()

	def search_for_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		"""
		Returns true if a matching package can be found in this package manager's registry.
		"""
		raise NotImplementedError()

	def install_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		"""
		Installs the requested package.
		"""
		raise NotImplementedError()

	def install_pkgs(self, pkgs: list[tuple[str, str]]) -> bool:
		"""
		Installs multiple packages at once.
		"""
		for pair in pkgs:
			if not install_pkg(pair[0], pair[1]):
				raise RuntimeError(
				    f"System package manager {get_name()}: Package {pair[0]} @ {pair[1]} failed to install!"
				)

	def accepts_config_files() -> bool:
		"""
		Returns true if this package manager can be fed an external configuration file (like a Brewfile, requirements.txt, package.json, etc).
		"""
		return False

	def process_config_file(self, filepath) -> bool:
		"""
		Processes an external configuration file.
		"""
		return False


#


def init_package_manager(pkg_mgr: PackageManager) -> None:
	"""
	Installs the package manager, if it isn't already installed.
	"""

	print(f"Initializing package manager {pkg_mgr.get_name()}...")

	if not pkg_mgr.is_installed():
		pkg_mgr.install_self()
