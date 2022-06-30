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

from shutil import which

#

class Interpreter:
	"""
	This class is a common interface for any type of scripting language interpreter.
	"""

	def get_name() -> str:
		"""
		Returns the name of the interpreter.
		"""
		raise NotImplementedError

	def get_command() -> str:
		"""
		Returns the command for the interpreter.

		This is usually the same as its name.
		"""
		return get_name()

	def is_installed() -> bool:
		"""
		Returns true if the interpreter is installed.
		"""
		return which(get_command()) is not None

	def install_self() -> None:
		"""
		Installs the interpreter.

		The implementation of this method must use the lowest-level system resources as possible, and would preferably be pure Python code with no external
		dependencies.
		"""
		raise NotImplementedError

	def run_script(script_path:str, args:list[str]=[]) -> str:
		"""
		Uses the interpreter to run a script.
		"""
		raise NotImplementedError
