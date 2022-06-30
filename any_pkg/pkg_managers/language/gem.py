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

from shutil import which
from multiprocessing import cpu_count
from package_manager import PackageManager
from utils.shell import execute
from interpreters.ruby import Ruby

class Gem(PackageManager):
	"""
	This class represents the interface to the Ruby gems package manager.
	"""

	def get_name() -> str:
		"""
		Returns 'gem'.
		"""
		return "gem"

	def install_self() -> None:
		"""
		gem is included with the Ruby interpreter, so this is the same as calling Ruby().install_self().
		"""
		Ruby().install_self()

	def update_all_pkgs() -> None:
		"""
		Updates the gem registry and upgrades any outdated gems.
		"""
		cmd = "gem update --no-document --env-shebang --both"

		execute(cmd)
		execute(f"{cmd} --system")

	def refresh_registry() -> None:
		"""
		Does nothing; gem has no such command.
		"""
		pass

	def search_for_pkg(pkg_name: str, pkg_version: str=None) -> bool:
		"""
		Updates the gem registry and returns true if the given gem can be found in the registry.

		pkg_name may be a regex.
		"""
		cmd = f"gem search {pkg_name}"

		if pkg_version is not None:
			cmd += f" --version {pkg_version}"

		matches = [x for x in execute(cmd).splitlines() if x.strip() and not x.startswith("***")]

		return len(matches) > 0

	def is_pkg_installed(pkg_name: str, pkg_version: str=None) -> bool:
		"""
		Returns true if the given gem is installed.
		"""
		cmd = f"gem search {pkg_name} --installed"

		if pkg_version is not None:
			cmd += f" --version {pkg_version}"

		output = execute(cmd)

		return output.strip() == "true"

	def install_pkg(pkg_name: str, pkg_version: str=None) -> None:
		"""
		Attempts to install the gem.
		"""
		if is_pkg_installed(pkg_name=pkg_name, pkg_version=pkg_version):
			return

		cmd = "gem install --no-document --env-shebang --both"

		if pkg_version is not None:
			cmd += f" --version {pkg_version}"

		execute(f"{cmd} {pkg_name}")

	def accepts_config_files() -> bool:
		"""
		Returns true.

		gem accepts Gemfiles (which are technically processed by bundler).
		"""
		return True

	def process_config_file(filepath) -> None:
		"""
		Processes a Gemfile.

		Calling this function installs the bundler gem, if it's not already installed.
		"""
		install_pkg(pkg_name="bundler")

		execute(f"bundle install --gemfile={filepath} --jobs={cpu_count()}")

	def clean_up() -> None:
		"""
		Cleans up any build artefacts or temporary files the package manager may have lying around.
		"""
		execute("gem cleanup")
