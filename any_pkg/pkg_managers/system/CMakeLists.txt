# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

set (system_files apk.py apt_get.py apt.py brew.py choco.py factory.py)

list (TRANSFORM system_files PREPEND system/)

set (system_files ${system_files} PARENT_SCOPE)
