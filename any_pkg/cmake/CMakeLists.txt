# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

cmake_minimum_required (VERSION 3.22 FATAL_ERROR)

project (Test_@PKG_NAME@ LANGUAGES C CXX)

find_package (@PKG_NAME@ @PKG_VERSION@ REQUIRED)

if (NOT @PKG_NAME@_FOUND)
    message (FATAL_ERROR "Not found!")
endif ()

set (pkg_targets @PKG_TARGETS@)

foreach (target IN LISTS pkg_targets)
    if (NOT TARGET "${target}")
        message (FATAL_ERROR "Missing target '${target}'")
    endif ()
endforeach ()
