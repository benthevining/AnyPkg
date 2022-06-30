#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines the interface for the Chocolatey package manager.
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

class Choco(PackageManager):
	"""
	This class represents the interface to the Chocolatey package manager.
	"""

	def get_name() -> str:
		"""
		Returns 'choco'.
		"""
		return "choco"

	def install_self() -> None:
		"""
		Installs Chocolatey on the system.
		"""
		if which("choco") is not None:
			return

		ps_cmd = """Set-ExecutionPolicy Bypass -Scope Process -Force;
		[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;
		iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"""

		execute(f"powershell.exe {ps_cmd}")

	def update_all_pkgs() -> None:
		"""
		Updates the Chocolatey package registry and upgrades any outdated packages.
		"""
		execute("choco upgrade all")

	def refresh_registry() -> None:
		"""
		Does nothing; choco has no such command.
		"""
		pass

	def search_for_pkg(pkg_name: str, pkg_version: str=None) -> bool:
		"""
		Updates the Chocolatey package registry and returns true if the given package can be found in the registry.
		"""
		raise NotImplementedError()

	def is_pkg_installed(pkg_name: str, pkg_version: str=None) -> bool:
		"""
		Returns true if the given package is installed.
		"""
		raise NotImplementedError

	def install_pkg(pkg_name: str, pkg_version: str=None) -> None:
		"""
		Attempts to install the package using Chocolatey.
		"""
		cmd = f"choco install {pkg_name} -y"

		if pkg_version is not None:
			cmd += f" --version {pkg_version}"

		execute(cmd)

	def accepts_config_files() -> bool:
		"""
		Returns true.

		Chocolatey accepts nuspec or nupkg files.
		"""
		return True

	def process_config_file(filepath) -> None:
		"""
		Processes a nuspec or nupkg file.
		"""
		execute(f"choco install {filepath}")

	def clean_up() -> None:
		"""
		Does nothing; choco has no such command.
		"""
		pass
