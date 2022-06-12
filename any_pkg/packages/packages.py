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

import pkg_managers.system
from pkg_managers.factory import create_and_initialize_package_manager
from pkg_managers.package_manager import PackageManager

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

	def install(self, pkg_mgr:PackageManager):
		assert(self.pkg_mgr_name == pkg_mgr.get_name())

		for pkg in self.pkgs:
			pkg_mgr.install_pkg(pkg.name, pkg.version)

		for config in self.configs:
			if not pkg_mgr.accepts_config_files():
				raise RuntimeError(f"Package manager {self.pkg_mgr_name} is not campatible with config file {config.filepath}!")

			pkg_mgr.process_config_file(config.filepath)

			if not config.pkg_mgr == self.pkg_mgr_name:
				raise RuntimeError(f"Package manager {self.pkg_mgr_name} is not campatible with config file {config.filepath}!")


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

	def install(self, pkg_mgrs:list[PackageManager]):
		for pkg_mgr_spec in self.pkg_mgr_specs:
			for pm in pkg_mgrs:
				if pm.get_name() == pkg_mgr_spec.pkg_mgr_name:
					pkg_mgr_spec.install(pm)

			raise(f"No package manager instance matches spec for {pkg_mgr_spec.pkg_mgr_name}")

		for command in self.init_commands:
			command.perform()

	def print_info():
		pass

	def print_package_list():
		pass

	def resolve_dependencies(self, pkg_sets:list[PackageSet], config_file:str) -> list[PackageSet]:

		all_sets: list[PackageSet] = [self]

		for set_dep in self.set_deps:
			for ps in pkg_sets:
				if ps.name == set_dep:
					all_sets.append(ps.resolve_dependencies(pkg_sets, config_file))
			raise RuntimeError(f"Package set {self.name} specifies a dependency on package set {set_dep}, but no such package set is defined in config file {config_file}!")

		# remove duplicates
		return list(set(all_sets))

	def get_list_of_package_managers(self) -> list[str]:
		pkg_mgrs: list[str] = []

		for pkg_mgr_spec in self.pkg_mgr_specs:
			pkg_mgrs.append(pkg_mgr_spec.pkg_mgr_name)

		pkg_mgrs = list(set(pkg_mgrs))

		return pkg_mgrs



#

def get_all_pkg_sets_in_file(filepath: str) -> list[PackageSet]:
	pass

#

def get_root_pkg_set (pkg_sets:list[PackageSet], config_file:str, pkg_set:str=None) -> PackageSet:
	if pkg_set is not None:
		for ps in pkg_sets:
			if ps.name == pkg_set:
				return ps
		raise RuntimeError(f"No package set named {pkg_set} in configuration file {config_file}!")

	for ps in pkg_sets:
		if ps.is_default:
			return ps

	raise RuntimeError(f"No package set specified, and no default named in configuration file {config_file}!")
