#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

from macros.macros import replace_macros


class Package:

	def __init__(self, name: str, version: str, url: str):
		self.name = name
		self.version = version
		self.url = url


#


class ConfigFile:

	def __init__(self, pkg_mgr: str, filepath: str):
		self.pkg_mgr = pkg_mgr
		self.filepath = filepath


#


class PackageManagerSpecification:

	def __init__(self, pkg_mgr_name: str, pkgs: list[Package],
	             configs: list[ConfigFile]):
		self.pkg_mgr_name = pkg_mgr_name
		self.pkgs = pkgs
		self.configs = configs

	def install(self):
		for config in self.configs:
			pass

		for pkg in self.pkgs:
			pass


#


class InitCommand:

	def __init__(self, command: str):
		self.command = replace_macros(command)

	def perform(self) -> bool:
		pass


#


class PackageSet:

	def __init__(self,
	             name: str,
	             description: str,
	             pkg_mgr_specs: list[PackageManagerSpecification],
	             init_commands: list[InitCommand],
	             set_deps: list[str],
	             is_default: bool = False,
	             is_advanced: bool = False):
		self.name = name
		self.description = replace_macros(description)
		self.pkg_mgr_specs = pkg_mgr_spec
		self.init_commands = init_commands
		self.set_deps = set_deps
		self.is_default = is_default
		self.is_advanced = is_advanced

	# resolve pkg mappings
	# conditionals

	def install(self):
		for dep in self.set_deps:
			pass

		for pkg_mgr_spec in self.pkg_mgr_specs:
			pkg_mgr_spec.install()

		for command in self.init_commands
			command.perform()

	def print_info():
		pass

	def print_package_list():
		pass
