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

from sys import platform as system_name

from os import environ

#

def replace_tokens(text: str, tokens:list[tuple[str, str]]) -> str:
	for pair in tokens:
		text = text.replace(pair[0], pair[1])
	return text

#

def replace_environment_variables(text:str) -> str:

	def __replace_environment_variable(text: str, macro: str) -> str:
		env_var = macro[5:-1]
		return replace_tokens(text, [(macro, environ[env_var])])

	#

	text = [__replace_environment_variable(text, text[i:i+len("$ENV<")]) for i in re.finditer("$ENV<", text)]

	return text

#

def replace_macros(text: str) -> str:
	text = replace_tokens(text,
		[("$<ProjectName>", "")
		 ("$<ProjectVersion>", ""),
		 ("$<ProjectRoot>", ""),
		 ("$<ProjectConfigFile>", ""),
		 ("$<OSName>", system_name)])

	return replace_environment_variables(text)
