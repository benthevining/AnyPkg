# ========================================
#  ____  _     ___  _ ____  _  __ _____
# /  _ \/ \  /|\  \///  __\/ |/ //  __/
# | / \|| |\ || \  / |  \/||   / | |  _
# | |-||| | \|| / /  |  __/|   \ | |_//
# \_/ \|\_/  \|/_/   \_/   \_|\_\\____\
# ========================================

include_guard (GLOBAL)

cmake_minimum_required (VERSION 3.22 FATAL_ERROR)

if (ORANGES_IN_GRAPHVIZ_CONFIG)
    return ()
endif ()

project (
    AnyPkgDocs
    VERSION "${AnyPkg_VERSION}"
    DESCRIPTION "AnyPkg documentation"
    HOMEPAGE_URL "${AnyPkg_HOMEPAGE_URL}"
    LANGUAGES NONE)

#

find_program (SPHINX_EXECUTABLE NAMES sphinx-build
              DOC "Sphinx Documentation Builder (sphinx-doc.org)")

find_program (MAKEINFO_EXECUTABLE NAMES makeinfo DOC "makeinfo tool")

#[[
Note: on my Mac, the following commands were needed to get the Latex build working:

brew install basictex
sudo tlmgr install latexmk tex-gyre fncychap wrapfig capt-of framed needspace varwidth titlesec
]]

find_program (LATEX_EXECUTABLE NAMES pdflatex DOC "pdflatex tool")

find_program (LATEXMK_EXECUTABLE NAMES latexmk DOC "latexmk tool")

if (NOT SPHINX_EXECUTABLE)
    if (AnyPkg_IS_TOP_LEVEL)
        message (WARNING "SPHINX_EXECUTABLE (sphinx-build) not found, AnyPkg docs cannot be built.")
    endif ()

    return ()
endif ()

if (NOT TARGET Python3::Interpreter)
    if (AnyPkg_IS_TOP_LEVEL)
        message (WARNING "Python interpreter cannot be found, AnyPkg docs cannot be built!")
    endif ()

    return ()
endif ()

#

set (conf_path "${CMAKE_CURRENT_LIST_DIR}")
set (scripts_path "${AnyPkg_SOURCE_DIR}/scripts")
set (templates_path "${AnyPkg_SOURCE_DIR}/templates")
set (conf_version "${AnyPkg_VERSION_MAJOR}.${AnyPkg_VERSION_MINOR}.${AnyPkg_VERSION_PATCH}")

configure_file (conf.py conf.py @ONLY NEWLINE_STYLE UNIX)

unset (conf_path)
unset (conf_version)
unset (scripts_path)

set (docs_output "${AnyPkg_SOURCE_DIR}/doc")
set (logfiles_dir "${CMAKE_CURRENT_BINARY_DIR}/logs")

if (MAKEINFO_EXECUTABLE)
    set (info_flag info)
endif ()

if (LATEX_EXECUTABLE AND LATEXMK_EXECUTABLE)
    set (latex_flag latexpdf)
endif ()

# cmake-format: off
foreach (format IN ITEMS html singlehtml man text linkcheck ${info_flag} ${latex_flag})
# cmake-format: on
    set (doc_format_output "oranges_doc_format_${format}")
    set (format_warnings_file "${logfiles_dir}/${format}")

    if ("${format}" STREQUAL info OR "${format}" STREQUAL latexpdf)
        # cmake-format: off
        add_custom_command (
            OUTPUT "${doc_format_output}"
            COMMAND
                "${SPHINX_EXECUTABLE}"
                    -M "${format}"
                    "${ORANGES_DOCS_BUILD_TREE}"
                    "${docs_output}/${format}"
                    -c "${CMAKE_CURRENT_BINARY_DIR}"
                    -d "${CMAKE_CURRENT_BINARY_DIR}/doctrees"
                    -w "${format_warnings_file}"
            DEPENDS "${ORANGES_DOCS_BUILD_TREE}/index.rst"
                    ${doc_format_last}
                    conf.py
            COMMENT "AnyPkg docs - building format ${format}..."
            VERBATIM USES_TERMINAL)
        # cmake-format: on
    else ()
        # cmake-format: off
        add_custom_command (
            OUTPUT "${doc_format_output}"
            COMMAND
                "${SPHINX_EXECUTABLE}"
                    -c "${CMAKE_CURRENT_BINARY_DIR}"
                    -d "${CMAKE_CURRENT_BINARY_DIR}/doctrees"
                    -b "${format}"
                    -w "${format_warnings_file}"
                    "${ORANGES_DOCS_BUILD_TREE}"
                    "${docs_output}/${format}"
            DEPENDS "${ORANGES_DOCS_BUILD_TREE}/index.rst"
                    ${doc_format_last}
                    conf.py
            COMMENT "AnyPkg docs - building format ${format}..."
            VERBATIM USES_TERMINAL)
        # cmake-format: on
    endif ()

    set_property (SOURCE "${doc_format_output}" PROPERTY SYMBOLIC 1)
    list (APPEND doc_format_outputs "${doc_format_output}")
    set (doc_format_last "${doc_format_output}")
endforeach ()

unset (doc_format_last)
unset (info_flag)
unset (latex_flag)

#

if (AnyPkg_IS_TOP_LEVEL)
    set (all_flag ALL)
endif ()

add_custom_target (AnyPkgDocs ${all_flag} DEPENDS "${doc_format_outputs}"
                   COMMENT "Building AnyPkg documentation...")

set_property (TARGET AnyPkgDocs APPEND PROPERTY ADDITIONAL_CLEAN_FILES "${logfiles_dir}"
                                                "${ORANGES_DOCS_BUILD_TREE}" "${docs_output}")

unset (all_flag)

set_target_properties (AnyPkgDocs PROPERTIES FOLDER Utility LABELS "AnyPkg;Utility;Documentation"
                                             XCODE_GENERATE_SCHEME OFF)

unset (doc_format_outputs)

#

install (DIRECTORY "${docs_output}/html" COMPONENT anypkg_doc_html
         DESTINATION "${CMAKE_INSTALL_DOCDIR}" PATTERN .buildinfo EXCLUDE)

cpack_add_component (anypkg_doc_html DISPLAY_NAME "AnyPkg HTML docs"
                     DESCRIPTION "Install the AnyPkg HTML documentation" GROUP anypkg_docs)

install (DIRECTORY "${docs_output}/singlehtml" COMPONENT anypkg_doc_singlehtml
         DESTINATION "${CMAKE_INSTALL_DOCDIR}" PATTERN .buildinfo EXCLUDE)

cpack_add_component (
    anypkg_doc_singlehtml DISPLAY_NAME "AnyPkg single-page HTML docs"
    DESCRIPTION "Install the AnyPkg single-page HTML documentation" GROUP anypkg_docs)

install (FILES "${docs_output}/man/oranges.1" COMPONENT anypkg_doc_man
         DESTINATION "${CMAKE_INSTALL_MANDIR}")

cpack_add_component (anypkg_doc_man DISPLAY_NAME "AnyPkg man pages"
                     DESCRIPTION "Install the AnyPkg man pages" GROUP anypkg_docs)

if (MAKEINFO_EXECUTABLE)
    install (FILES "${docs_output}/info/texinfo/anypkg.info" COMPONENT anypkg_doc_info
             DESTINATION "${CMAKE_INSTALL_INFODIR}")

    cpack_add_component (anypkg_doc_info DISPLAY_NAME "AnyPkg info pages"
                         DESCRIPTION "Install the AnyPkg info pages" GROUP anypkg_docs)
endif ()

if (LATEX_EXECUTABLE AND LATEXMK_EXECUTABLE)
    install (FILES "${docs_output}/latexpdf/latex/anypkg.pdf" COMPONENT anypkg_doc_pdf
             DESTINATION "${CMAKE_INSTALL_DOCDIR}")

    cpack_add_component (anypkg_doc_pdf DISPLAY_NAME "AnyPkg PDF documentation"
                         DESCRIPTION "Install the AnyPkg PDF documentation" GROUP anypkg_docs)
endif ()

cpack_add_component_group (
    anypkg_docs DISPLAY_NAME "AnyPkg documentation" DESCRIPTION "Install all AnyPkg documentation"
    PARENT_GROUP anypkg INSTALL_TYPES Developer)
