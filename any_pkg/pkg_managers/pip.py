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


class Pip(PackageManager):

	def get_name() -> str:
		return "pip"

	def install_self(self) -> bool:
		# python -m ensurepip --upgrade
		raise NotImplementedError()

	def update_all_pkgs(self) -> None:
		raise NotImplementedError()

	def search_for_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		raise NotImplementedError()

	def install_pkg(self, pkg_name: str, pkg_version: str) -> bool:
		raise NotImplementedError()

	def process_requirements_txt(requirements_txt: str) -> bool:
		# python3 -m pip install -r requirements_txt
		pass
