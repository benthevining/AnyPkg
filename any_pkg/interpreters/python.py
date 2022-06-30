#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines the Interpreter interface class.
"""

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

import os
from sys import executable as EXEC_PATH
from interpreter import Interpreter
from utils.shell import execute

class Python(Interpreter):
	"""
	This class is the interface to the Python interpreter.

	This class will always prefer to execute new scripts using the same interpreter executable that AnyPkg is currently running under.
	"""

	def get_name() -> str:
		"""
		Returns 'python'.
		"""
		return "python"

	def get_command() -> str:
		"""
		Returns the absolute path to the Python interpreter that AnyPkg is currently running under.
		"""
		if EXEC_PATH.endswith("python"):
			return EXEC_PATH

		path = os.path.join(os.__file__.split("lib/")[0], "bin", "python3")

		if os.path.exists(path):
			return path

		return "python3"

	def is_installed() -> bool:
		"""
		Returns true.
		"""
		return True

	def install_self() -> None:
		"""
		Does nothing.
		"""
		pass

	def run_script(script_path:str, args:list[str]=[]) -> str:
		"""
		Runs a Python script.

		A new Python process is launched with the same interpreter that AnyPkg is currently running under.
		"""
		return execute(f"{get_command()} {script_path} {' '.join(args)}")

	def run_module(module_name:str, args:list[str]=[]) -> str:
		"""
		Executes a python module with -m.
		"""
		return execute(f"{get_command()} -m {module_name} {' '.join(args)}")
