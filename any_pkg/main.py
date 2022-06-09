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
from pkg_managers.package_manager import PKG_MGR_INIT_UPDATES

#


def install_packages(config_file: str,
                     pkg_set: str,
                     log_file: str = None,
                     sys_pkg_mgr: str = None,
                     no_updates: bool = False) -> None:
	if no_updates:
		PKG_MGR_INIT_UPDATES = False

	if sys_pkg_mgr is not None:
		PREFERRED_SYS_PKG_MGR = sys_pkg_mgr


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
