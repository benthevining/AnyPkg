#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

from typing import Final


class Brew(PackageManager):

	def get_name() -> str:
		return "brew"

	def install_self(self) -> bool:
		raise NotImplementedError()

	def update_all_pkgs(self) -> None:
		#brew update
		#brew upgrade
		#brew cleanup
		raise NotImplementedError()

	def search_for_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		raise NotImplementedError()

	def install_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		raise NotImplementedError()

	def process_brewfile(brewfile: str) -> bool:
		pass
