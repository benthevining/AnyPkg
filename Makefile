SHELL := /bin/sh
.ONESHELL:
.SHELLFLAGS: -euo
.DEFAULT_GOAL: help
.NOTPARALLEL:
.POSIX:

#

export VERBOSE ?= 1

# program aliases
CMAKE ?= cmake
RM = $(CMAKE) -E rm -rf  # force this one to use CMake
PRECOMMIT ?= pre-commit
GIT ?= git
ASDF ?= asdf
PYTHON ?= python3

# directory aliases
BUILD_DIR ?= $(ANYPKG_ROOT)/Builds
DOCS_DIR ?= $(ANYPKG_ROOT)/doc

# set build parallel level
ifeq ($(OS),Windows_NT)
	export CMAKE_BUILD_PARALLEL_LEVEL ?= $(NUMBER_OF_PROCESSORS)
else ifeq ($(shell uname -s),Darwin)
	export CMAKE_BUILD_PARALLEL_LEVEL ?= $(shell sysctl hw.ncpu | awk '{print $$2}')
	SUDO ?= sudo
else # Linux
	export CMAKE_BUILD_PARALLEL_LEVEL ?= $(shell grep -c ^processor /proc/cpuinfo)
	SUDO ?= sudo
endif

#

override ANYPKG_ROOT = $(patsubst %/,%,$(strip $(dir $(realpath $(firstword $(MAKEFILE_LIST))))))

#

.PHONY: help
help:  ## Print this message
	@grep -E '^[a-zA-Z_-]+:.*?\#\# .*$$' $(ANYPKG_ROOT)/Makefile | sort | awk 'BEGIN {FS = ":.*?\#\# "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

#

.PHONY: init
init:  ## Initializes the workspace and installs all dependencies
	@cd $(ANYPKG_ROOT) && \
		$(PRECOMMIT) install --install-hooks --overwrite && \
		$(PRECOMMIT) install --install-hooks --overwrite --hook-type commit-msg
	@cd $(ANYPKG_ROOT) && $(ASDF) install
	$(PYTHON) -m pip install -r $(ANYPKG_ROOT)/requirements.txt

#

$(BUILD_DIR):
	@cd $(ANYPKG_ROOT) && $(CMAKE) --preset default

.PHONY: config
config: $(BUILD_DIR) ## configure CMake

#

.PHONY: build
build: config ## runs CMake build
	@cd $(ANYPKG_ROOT) && $(CMAKE) --build --preset default

#

.PHONY: install
install: build ## runs CMake install
	$(SUDO) $(CMAKE) --install $(BUILD_DIR)

.PHONY: pack
pack: build ## Creates a CPack installer
	@$(CMAKE) --build $(BUILD_DIR) --target package

#

.PHONY: pc
pc:  ## Runs all pre-commit hooks over all files
	@cd $(ANYPKG_ROOT) && $(GIT) add . && $(PRECOMMIT) run --all-files

#

$(DOCS_DIR): config
	@cd $(ANYPKG_ROOT) && $(CMAKE) --build --preset docs

.PHONY: docs
docs: $(DOCS_DIR) ## Builds the documentation

#

.PHONY: uninstall
uninstall: ## Runs uninstall script
	@if [ -d $(BUILD_DIR) ]; then \
		echo "Uninstalling..."; \
		$(SUDO) $(CMAKE) -P $(BUILD_DIR)/uninstall.cmake; \
	else \
		echo "Cannot uninstall, builds directory doesn't exist!"; \
	fi

.PHONY: clean
clean: ## Cleans the source tree
	@echo "Cleaning..."
	@$(RM) $(BUILD_DIR) $(DOCS_DIR)
	@cd $(ANYPKG_ROOT) && $(PRECOMMIT) gc
