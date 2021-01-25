# REDNAFI
# This only works with embedded venv not virtualenv
# Install venv: python3.8 -m venv venv
# Activate venv: source venv/bin/activate

# Usage (line =black line length, path = action path, ignore= exclude folders)
# ------
# make pylinter [make pylinter line=88 path=.]
# make pyupgrade

path := .
line := 88
ignore := *env

all:
	@echo

.PHONY: checkvenv
checkvenv:
# raises error if environment is not active
ifeq ("$(VIRTUAL_ENV)","")
	@echo "Venv is not activated!"
	@echo "Activate venv first."
	@echo
	exit 1
endif

.PHONY: pyupgrade
pyupgrade: checkvenv
# checks if pip-tools is installed
ifeq ("$(wildcard venv/bin/pip-compile)","")
	@echo "Installing Pip-tools..."
	@pip install pip-tools
endif

ifeq ("$(wildcard venv/bin/pip-sync)","")
	@echo "Installing Pip-tools..."
	@pip install pip-tools
endif

# pip-tools
	# @pip-compile --upgrade requirements-dev.txt
	@pip-sync requirements-dev.txt


.PHONY: pylinter
pylinter: checkvenv
# checks if black is installed
ifeq ("$(wildcard venv/bin/black)","")
	@echo "Installing Black..."
	@pip install black
endif

# checks if isort is installed
ifeq ("$(wildcard venv/bin/isort)","")
	@echo "Installing Isort..."
	@pip install isort
endif

# checks if flake8 is installed
ifeq ("$(wildcard venv/bin/flake8)","")
	@echo -e "Installing flake8..."
	@pip install flake8
	@echo
endif

# black
	@echo "Applying Black"
	@echo "----------------\n"
	@black --line-length $(line) --exclude $(ignore) $(path)
	@echo

# isort
	@echo "Applying Isort"
	@echo "----------------\n"
	@isort --atomic --profile black $(path)
	@echo

# flake8
	@echo "Applying Flake8"
	@echo "----------------\n"
	@flake8 --max-line-length "$(line)" \
			--max-complexity "18" \
			--select "B,C,E,F,W,T4,B9" \
			--ignore "E203,E266,E501,W503,F403,F401,E402" \
			--exclude ".git,__pycache__,old, build, \
						dist, venv, .tox" $(path)
