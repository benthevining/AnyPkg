#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module implements a built-in CMake package manager.
"""

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

from package import Package

#

def check_if_package_is_already_available(pkg:Package) -> bool:
	"""
	Returns true if the given package is already available on the system.
	"""

	# generate a CMakeLists.txt
		# @PKG_NAME@
		# @PKG_VERSION@
		# @PKG_TARGETS@

	# call cmake configure on the generated file

	pass

#

def install_package(pkg:Package) -> str:
	"""
	Installs the given CMake package.
	"""

	if check_if_package_is_already_available(pkg):
		return None

	# download the package from git
	# run cmake configure, build, install

	install_dir: str = None

	if not check_if_package_is_already_available(pkg):
		raise RuntimeError(f"Package {pkg.name} failed to install!")

	return install_dir

#

def install_packages(pkgs: list[Package]) -> list[str]:
	"""
	Installs multiple CMake packages at once.
	"""

	install_dirs: list[str] = []

	for pkg in pkgs:
		install_dir = install_package(pkg)

		if install_dir is not None:
			install_dirs.append(install_dir)

	# remove duplicates
	return list(set(install_dirs))
