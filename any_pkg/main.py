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
from argparse import ArgumentParser
import os
from sys import argv as script_arg_count

from pkg_managers.system.factory import SYSTEM_PKG_MGR_NAMES, PREFERRED_SYS_PKG_MGR
from pkg_managers.package_manager import PKG_MGR_INIT_UPDATES, PackageManager
from pkg_managers.factory import create_and_initialize_package_manager

from packages.packages import PackageSet, get_all_pkg_sets_in_file

#


def install_packages(config_file: str,
                     pkg_set: str=None,
                     log_file: str = None,
                     sys_pkg_mgr: str = None,
                     no_updates: bool = False) -> None:
	# initialize log file

	if no_updates:
		PKG_MGR_INIT_UPDATES = False

	if sys_pkg_mgr is not None:
		PREFERRED_SYS_PKG_MGR = sys_pkg_mgr

	if not os.path.isabs(config_file):
		config_file = os.path.join(os.getcwd(), config_file)

	# create an array of PackageSet objects describing every package set in the config file
	pkg_sets: Final[list[PackageSet]] = get_all_pkg_sets_in_file(config_file)

	# determine the root package set to install - if the user specified one, or if the config file specifies a default
	root_pkg_set: Final[PackageSet] = get_root_pkg_set(pkg_sets=pkg_sets,
		config_file=config_file,
		pkg_set=pkg_set)

	# resolve transitively the list of all package sets to be installed
	ps_list: Final[list[PackageSet]] = list(set(root_pkg_set.resolve_dependencies(pkg_sets, config_file)))

	# now construct a list of names of package managers that the package sets to be installed will need
	pm_list: list[str] = []

	for ps in ps_list:
		pm_list.append(ps.get_list_of_package_managers())
	pm_list = list(set(pm_list))

	# now construct an array of actual PackageManager instances based on the list of names
	package_mgrs: list[PackageManager] = []

	for pm_name in pm_list:
		package_mgrs.append(create_and_initialize_package_manager(pm_name))

	# install each package set
	for ps in ps_list:
		ps.install(package_mgrs)

#

def update_all_packages() -> None:
	pass

#


def __create_parser() -> ArgumentParser:
	"""
	Creates the argument parser for this script.

	:meta private:
	"""
	parser = ArgumentParser()

	parser.add_argument("--config",
	                    "-c",
	                    action="store",
	                    dest="config_file",
	                    required=False,
	                    default=os.path.join(os.getcwd(), ""),
	                    help="The config file to read for processing.")

	parser.add_argument(
	    "--set",
	    "-s",
	    action="store",
	    dest="pkg_set",
	    required=False,
	    default=None,
	    help=
	    "The package set to install. If not specified, defaults to the package set marked as the default in the config file being processed."
	)

	parser.add_argument(
	    "--log",
	    "-l",
	    action="store",
	    dest="log_file",
	    required=False,
	    default=None,
	    help=
	    "Path to a log file to write output to during processing. Output will still be written to stdout."
	)

	parser.add_argument(
	    "--system-pkg",
	    action="store",
	    dest="sys_pkg_mgr",
	    required=False,
	    default=None,
	    help=
	    f"Name of the preferred system package manager. Valid names are: {SYSTEM_PKG_MGR_NAMES}"
	)

	parser.add_argument(
	    "--no-update",
	    "-n",
	    action="store_true",
	    dest="no_updates",
	    required=False,
	    default=False,
	    help=
	    "Don't update each package manager's installed packages before installing new ones. The default behavior is to update all packages before installing new ones."
	)

	return parser


#


def main():
	my_parser = __create_parser()

	if len(script_arg_count) < 2:
		my_parser.print_help()
	else:
		args = my_parser.parse_args()

		install_packages(config_file=args.config_file,
		                 pkg_set=args.pkg_set,
		                 log_file=args.log_file,
		                 sys_pkg_mgr=args.sys_pkg_mgr,
		                 no_updates=args.no_updates)


#

if __name__ == "__main__":
	main()
