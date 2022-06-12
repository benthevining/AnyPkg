# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

add_subdirectory (conditionals)
add_subdirectory (macros)
add_subdirectory (packages)
add_subdirectory (pkg_managers)

set (anypkg_sources main.py ${conditionals_files} ${macros_files} ${packages_files}
                    ${pkg_managers_files})

add_custom_target (
    AnyPkg ALL
    COMMAND Python3::Interpreter -m build
    WORKING_DIRECTORY "${AnyPkg_SOURCE_DIR}"
    COMMENT "Building AnyPkg..."
    VERBATIM USES_TERMINAL
    SOURCES ${anypkg_sources})

install (CODE "${Python3_EXECUTABLE} -m pip install dist/AnyPkg-${PROJECT_VERSION}.whl"
         COMPONENT anypkg)

include (CPackComponent)

cpack_add_component (anypkg DISPLAY_NAME AnyPkg DESCRIPTION "A package manager manager")

source_group (TREE "${CMAKE_CURRENT_LIST_DIR}" PREFIX any_pkg FILES ${anypkg_sources})
