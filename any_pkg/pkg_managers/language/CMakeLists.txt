# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

set (language_files gem.py npm.py pip.py)

list (TRANSFORM language_files PREPEND language/)

set (language_files ${language_files} PARENT_SCOPE)
