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

from shutil import which, rmtree
import os
from package_manager import PackageManager
from utils.shell import execute

class Brew(PackageManager):
	"""
	This class represents the interface to the Homebrew package manager.
	"""

	def get_name() -> str:
		"""
		Returns 'brew'.
		"""
		return "brew"

	def install_self() -> bool:
		"""
		Installs Homebrew on the system.
		"""
		if which("brew") is not None:
			return

		# install XCode command-line tools
		execute("xcode-select --install")

		workdir = os.path.join(os.getcwd(), "homebrew")

		os.makedirs(workdir)

		execute(f"curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C {workdir}")

		rmtree(workdir, ignore_errors=True)

	def update_all_pkgs() -> None:
		"""
		Updates the Homebrew package registry and upgrades any outdated packages.
		"""
		refresh_registry()
		execute("brew upgrade")

	def refresh_registry() -> None:
		"""
		Updates the package manager's package registry.
		"""
		execute("brew update")

	def search_for_pkg(pkg_name: str, pkg_version: str=None) -> bool:
		"""
		Updates the Homebrew package registry and returns true if the given package can be found in the registry.
		"""
		output = [x.partition(' ')[0].strip() for x in execute(f"brew search {pkg_name}") if not x.startswith("==>")]
		return pkg_name in output

	def is_pkg_installed(pkg_name: str, pkg_version: str=None) -> bool:
		"""
		Returns true if the given package is installed.
		"""
		output = [x.partition(' ')[0].strip() for x in execute("brew list -1") if not x.startswith("==>")]
		return pkg_name in output or f"{pkg_name}@{pkg_version}" in output

	def install_pkg(pkg_name: str, pkg_version: str=None) -> None:
		"""
		Attempts to install the package using Homebrew.
		"""
		execute(f"brew install {pkg_name}")

	def accepts_config_files() -> bool:
		"""
		Returns true.

		brew accepts Brewfiles or Caskfiles.
		"""
		return True

	def process_config_file(filepath) -> bool:
		"""
		Processes a Brewfile or Caskfile.
		"""
		execute("brew bundle", workdir=os.path.realpath(os.path.dirname(filepath)))

	def clean_up() -> None:
		"""
		Cleans up any build artefacts or temporary files the package manager may have lying around.
		"""
		execute("brew cleanup")
