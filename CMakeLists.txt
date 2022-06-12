# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

include_guard (GLOBAL)

cmake_minimum_required (VERSION 3.22 FATAL_ERROR)

project (
    AnyPkg
    VERSION 1.0.0
    DESCRIPTION "Package manager manager"
    HOMEPAGE_URL "www.github.com/benthevining/AnyPkg"
    LANGUAGES NONE)

if (PROJECT_IS_TOP_LEVEL)
    # enable at least one language for GNUInstallDirs
    enable_language (CXX)

    # cmake-format: off
    set_property (
        GLOBAL PROPERTY
            USE_FOLDERS YES
            PREDEFINED_TARGETS_FOLDER Targets
            REPORT_UNDEFINED_PROPERTIES "${CMAKE_BINARY_DIR}/undefined_properties.log")
    # cmake-format: on

    # set (CMAKE_FIND_PACKAGE_SORT_ORDER NATURAL)
    set (CMAKE_INSTALL_MESSAGE LAZY)
    set (CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION ON)
endif ()

option (ANYPKG_BUILD_DOCS "Build the documentation" "${PROJECT_IS_TOP_LEVEL}")

mark_as_advanced (ANYPKG_BUILD_DOCS)

enable_testing ()

find_package (Python3 3.9 REQUIRED COMPONENTS Interpreter)

add_subdirectory (any_pkg)

if (ANYPKG_BUILD_DOCS)
    add_subdirectory (docs)
endif ()
