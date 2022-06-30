#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines the interface for the apt package manager.
"""

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

from shutil import which
from package_manager import PackageManager
from utils.shell import execute

class Apt(PackageManager):
	"""
	This class represents the interface to the apt package manager.
	"""

	def get_name() -> str:
		"""
		Returns 'apt'.
		"""
		return "apt"

	def install_self() -> None:
		"""
		Installs apt on the system.
		"""
		if which("apt") is None:
			# TODO: download from http://mirrors.edge.kernel.org/ubuntu/pool/main/a/apt/apt_1.6.8_amd64.deb
			execute("pkexec dpkg -i apt.deb")

	def update_all_pkgs() -> None:
		"""
		Updates the apt package registry and upgrades any outdated packages.
		"""
		refresh_registry()
		execute("apt upgrade")

	def refresh_registry() -> None:
		"""
		Updates the package manager's package registry.
		"""
		execute("apt update")

	def search_for_pkg(pkg_name: str, pkg_version: str=None) -> bool:
		"""
		Updates the apt package registry and returns true if the given package can be found in the registry.
		"""
		refresh_registry()
		output = [x.partition(' ').strip() for x in execute(f"apt search {pkg_name}").splitlines()]
		return pkg_name in output

	def is_pkg_installed(pkg_name: str, pkg_version: str=None) -> bool:
		"""
		Returns true if the given package is installed.
		"""
		raise NotImplementedError

	def install_pkg(pkg_name: str, pkg_version: str=None) -> None:
		"""
		Attempts to install the package using apt.
		"""
		refresh_registry()

		if pkg_version is None:
			pkg_spec = pkg_name
		else:
			pkg_spec = f"{pkg_name}={pkg_version}"

		execute(f"apt install {pkg_spec}")

	def accepts_config_files() -> bool:
		"""
		Returns true if this package manager can be fed an external configuration file (like a Brewfile, requirements.txt, package.json, Gemfile, etc).
		"""
		return False

	def process_config_file(filepath) -> None:
		"""
		Raises a NotImplementedError.
		"""
		raise NotImplementedError

	def clean_up() -> None:
		"""
		Does nothing; apt has no such command.
		"""
		pass
