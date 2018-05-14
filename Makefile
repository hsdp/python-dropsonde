PROTO_PATH := build/dropsonde-protocol
OUTPUT_DIR := .
BUILD_DIR := build
MODULE_NAME := dropsonde

VENV := virtualenv
GIT := git
BUILD_PY := build.py
DROPSONDE_REPO_URL := https://github.com/cloudfoundry/dropsonde-protocol
DROPSONDE_REPO_REF := ce0e609a7a57f041b74e661f13d32e5f7a673a5d

PY2_LANG := python
PY2_NAME := pb
PY2_NSPATH := $(MODULE_NAME)/$(PY2_NAME)
PY2_NSMOD := $(MODULE_NAME).$(PY2_NAME)
PY2_OUTDIR := $(OUTPUT_DIR)/$(MODULE_NAME)/$(PY2_NAME)
PY2_ENV := env
PY2_ACT := . $(PY2_ENV)/bin/activate &&
PY2_EXE := python
PY2_VENV := $(VENV)

PY3_LANG := python3
PY3_NAME := py3
PY3_NSPATH := $(MODULE_NAME)/$(PY3_NAME)
PY3_NSMOD := $(MODULE_NAME).$(PY3_NAME)
PY3_OUTDIR := $(OUTPUT_DIR)/$(MODULE_NAME)/$(PY3_NAME)
PY3_ENV := env3
PY3_ACT := . $(PY3_ENV)/bin/activate &&
PY3_EXE := python3
PY3_VENV := $(VENV) -p python3

.PHONY: clone
clone:
	mkdir -p $(BUILD_DIR)
	[[ ! -d $(PROTO_PATH) ]] && $(GIT) clone $(DROPSONDE_REPO_URL) $(PROTO_PATH) || :
	cd $(PROTO_PATH) && $(GIT) checkout $(DROPSONDE_REPO_REF)

.PHONY: clean-clone
clean-clone:
	[[ -d $(PROTO_PATH) ]] && rm -rf $(PROTO_PATH) || :

.PHONY: compile-py2
compile-py2: clean-compile-py2
	python3 build.py \
		--source-dir "$(PROTO_PATH)/events" \
		--namespace-path $(PY2_NSPATH) \
		--namespace-module $(PY2_NSMOD) \
		--lang $(PY2_LANG) \
		--output-dir $(OUTPUT_DIR) \
		--build-dir $(BUILD_DIR) \
		clone refactor protoc
	echo > $(PY2_OUTDIR)/__init__.py

.PHONY: compile
compile: compile-py2

.PHONY: clean-compile-py2
clean-compile-py2:
	[[ -d $(PY2_OUTDIR) ]] && rm -r $(PY2_OUTDIR) || :

.PHONY: clean-compile
clean-compile: clean-compile-py2

.PHONY: install-py2
install-py2:
	[[ ! -d $(PY2_ENV) ]] && $(PY2_VENV) $(PY2_ENV) || :
	$(PY2_ACT) pip install -r requirements.txt
	$(PY2_ACT) pip install -r requirements-dev.txt

.PHONY: install-py3
install-py3:
	[[ ! -d $(PY3_ENV) ]] && $(PY3_VENV) $(PY3_ENV) || :
	$(PY3_ACT) pip install -r requirements.txt
	$(PY3_ACT) pip install -r requirements-dev.txt

.PHONY: install
install: clone install-py2 install-py3

.PHONY: clean-env-py2
clean-env-py2:
	[[ -d $(PY2_ENV) ]] && rm -r $(PY2_ENV) || :

.PHONY: clean-env-py3
clean-env-py3:
	[[ -d $(PY3_ENV) ]] && rm -r $(PY3_ENV) || :

.PHONY: clean-env
clean-env: clean-env-py2 clean-env-py3

.PHONY: clean
clean: clean-clone clean-compile clean-env

.PHONY: test-py2
test-py2: install-py2
	$(PY2_ACT) nose2 -v	

.PHONY: test-py3
test-py3: install-py3
	$(PY3_ACT) nose2 -v

.PHONY: test
test: test-py2 test-py3

.PHONY: package
package:
	$(PY3_ACT) $(PY3_EXE) setup.py sdist

.PHONY: build
build: clone compile test package

.PHONY: deploy
deploy: clean clone compile test
	$(PY3_ACT) $(PY3_EXE) setup.py sdist upload
