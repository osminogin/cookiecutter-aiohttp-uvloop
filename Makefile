KUBECTL := $(shell /usr/bin/env kubectl 2> /dev/null)

default: generate

generate:
	@cookiecutter --replay -f -o ../ .

clean:
	@rm -rf ../{{cookiecutter.project_slug}}

deps:
ifndef KUBECTL
	@echo "Warning: You must install `kubectl` utility"
endif

info: deps
	kubectl config current-context

.PHONY: default generate clean info deps
