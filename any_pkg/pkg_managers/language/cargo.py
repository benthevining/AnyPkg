#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines the interface for the Cargo Rust package manager.
"""

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

from package_manager import PackageManager
from multiprocessing import cpu_count

class Cargo(PackageManager):
	"""
	This class is the interface to Cargo, the Rust package manager.
	"""

	def get_name() -> str:
		"""
		Returns 'cargo'.
		"""
		return "cargo"

	def install_self() -> None:
		"""
		Installs cargo.
		"""
		raise NotImplementedError

	def update_all_pkgs() -> None:
		"""
		Updates all installed crates.
		"""
		raise NotImplementedError

	def refresh_registry() -> None:
		"""
		Updates the cargo package registry.
		"""
		raise NotImplementedError

	def search_for_pkg(pkg_name: str, pkg_version: str=None) -> bool:
		"""
		Updates the cargo registry and returns true if the given crate can be found in the registry.
		"""
		refresh_registry()

		raise NotImplementedError

	def is_pkg_installed(pkg_name: str, pkg_version: str=None) -> bool:
		"""
		Returns true if the given crate is installed.
		"""
		raise NotImplementedError

	def install_pkg(pkg_name: str, pkg_version: str=None) -> None:
		"""
		Attempts to install the package using cargo.
		"""
		cmd = f"cargo install --jobs {cpu_count()}"

		if pkg_version is not None:
			cmd += f" --version {pkg_version}"

		execute(f"{cmd} {pkg_name}")

	def accepts_config_files() -> bool:
		"""
		Returns true.

		cargo accepts Cargo.toml files.
		"""
		return True

	def process_config_file(filepath) -> None:
		"""
		Processes a Cargo.toml file.
		"""
		raise NotImplementedError

	def clean_up() -> None:
		"""
		Cleans up any build artefacts or temporary files the package manager may have lying around.
		"""
		raise NotImplementedError
