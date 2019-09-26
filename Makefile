default: generate

generate:
	@cookiecutter --replay -f -o ../ .

.PHONY: default generate
