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

from interpreter import Interpreter
from utils.shell import execute

class Ruby(Interpreter):
	"""
	This class is the interface for the Ruby interpreter.
	"""

	def get_name() -> str:
		"""
		Returns 'ruby'.
		"""
		return "ruby"

	def install_self() -> None:
		"""
		Installs the Ruby interpreter.
		"""
		if is_installed(): return

		raise NotImplementedError

	def run_script(script_path:str, args:list[str]=[]) -> str:
		"""
		Runs a Ruby script.
		"""
		return execute(f"ruby {script_path} {' '.join(args)}")
