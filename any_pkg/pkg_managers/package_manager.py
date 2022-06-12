#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

#

PKG_MGR_INIT_UPDATES: bool = True


class PackageManager:

	def get_name() -> str:
		raise NotImplementedError()

	def install_self(self) -> bool:
		raise NotImplementedError()

	def update_all_pkgs(self) -> None:
		raise NotImplementedError()

	def search_for_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		raise NotImplementedError()

	def install_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		raise NotImplementedError()

	def install_pkgs(self, pkgs: list[tuple[str, str]]) -> bool:
		for pair in pkgs:
			if not install_pkg(pair[0], pair[1]):
				raise RuntimeError(
				    f"System package manager {get_name()}: Package {pair[0]} @ {pair[1]} failed to install!"
				)

	def accepts_config_files() -> bool:
		return False

	def process_config_file(self, filepath) -> bool:
		return False


#


def init_package_manager(pkg_mgr: PackageManager) -> None:

	print(f"Initializing package manager {pkg_mgr.get_name()}...")

	pkg_mgr.install_self()

	if PKG_MGR_INIT_UPDATES:
		pkg_mgr.update_all_pkgs()
