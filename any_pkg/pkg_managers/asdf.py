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


class ASDF(PackageManager):

	def get_name() -> str:
		return "asdf"

	def install_self(self) -> bool:
		raise NotImplementedError()

	def update_all_pkgs(self) -> None:
		raise NotImplementedError()

	def search_for_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		raise NotImplementedError()

	def install_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		raise NotImplementedError()

	def process_tool_versions(tool_versions: str) -> bool:
		pass