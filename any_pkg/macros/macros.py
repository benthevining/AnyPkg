#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains functions for expanding macros present in the input files.
"""

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

from sys import platform as system_name
from os import environ
from re import finditer

#

def replace_tokens(text: str, tokens:list[tuple[str, str]]) -> str:
	"""
	This generic function replaces all occurrences of a set of tokens with another set of tokens.
	"""
	for pair in tokens:
		text = text.replace(pair[0], pair[1])
	return text

#

def replace_environment_variables(text:str) -> str:
	"""
	This function finds each occurrence of '$ENV<variableName>' in the input text and replaces it with the value of the environment variable
	'variableName'.
	"""

	def __replace_environment_variable(text: str, macro: str) -> str:
		env_var = macro[5:-1]
		return replace_tokens(text, [(macro, environ[env_var])])

	#

	text = [__replace_environment_variable(text, text[i:i+len("$ENV<")]) for i in finditer("$ENV<", text)]

	return text

#

def replace_macros(text: str) -> str:
	"""
	This function replaces and evaluates all macros present in the input text.
	"""
	text = replace_tokens(text,
		[("$<ProjectName>", "")
		 ("$<ProjectVersion>", ""),
		 ("$<ProjectRoot>", ""),
		 ("$<ProjectConfigFile>", ""),
		 ("$<OSName>", system_name)])

	return replace_environment_variables(text)
