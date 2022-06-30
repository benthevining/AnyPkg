#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains utilities for executing shell commands.
"""

# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

import subprocess
from os import path, makedirs

def execute(cmd:str, log_file:str=None, quiet:bool=True, fatal:bool=True, workdir:str=None) -> str:
	cp = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, shell=True, capture_output=True, cwd=workdir)

    if not quiet:
		print(cp.stdout)
		print(cp.stderr)

	if log_file is not None:
    	# make sure the log file directory exists
    	log_dir = path.abspath (path.dirname(log_file))
		if not path.exists(log_dir): makedirs (log_dir)

		# delete file if it existed
		if os.path.exists(log_file): os.remove(log_file)

		# make sure the file exists
		with open (log_file, 'w') as f:
			f.write (f"\r\nOriginal command line: {cmd}")
			f.write (f"\r\nExit code: {cp.returncode}")
			if cp.stderr: f.write (f"\r\nErrors: \r\n {cp.stderr}")
			f.write (f"\r\nstdout: \r\n {cp.stdout} \r\n")

    if cp.returncode != 0:
    	if not quiet: print(f"Command {cmd} failed - exit code: {cp.returncode}")
        if fatal: raise ChildProcessError

    return cp.stdout
