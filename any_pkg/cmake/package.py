#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines data structures for CMake packages.
"""

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

class Package:
	"""
	This class represents metadata about a CMake package.
	"""

	def __init__(self, name:str, version:str, git_repo:str):
		self.name = name
		self.version = version
		self.git_repo = git_repo
