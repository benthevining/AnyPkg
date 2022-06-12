# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

add_subdirectory (system)

set (
    pkg_managers_files
    ${system_files}
    asdf.py
    factory.py
    gem.py
    npm.py
    package_manager.py
    pip.py)

list (TRANSFORM pkg_managers_files PREPEND pkg_managers/)

set (pkg_managers_files ${pkg_managers_files} PARENT_SCOPE)
