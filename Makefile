default: generate

generate:
	@cookiecutter --replay -f -o ../ .

clean:
	@rm -rf ../{{cookiecutter.project_slug}}

.PHONY: default generate clean
