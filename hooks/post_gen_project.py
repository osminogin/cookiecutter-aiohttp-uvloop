import subprocess


def run(command):
    try:
        subprocess.run(command, stdout=subprocess.PIPE)
    except subprocess.CalledProcessError as error:
        print('{}: {}\n{}'.format(error.returncode, error.cmd, error.output))
        raise error


def which(command):
    try:
        import shutil
        assert hasattr(shutil, 'which')
        full_path = shutil.which(command)
        assert full_path
        return full_path
    except AssertionError:
        raise RuntimeError('Command {} not installed'.format(command))


def setup_git_repo():
    git = which('git')
    run([git, 'init'])
    run([git, 'add', '.'])
    run([git, 'status'])
    run([git, 'commit', '-m', 'Initial commit'])


def install_dependencies():
    """
    Install project dependencies.
    """
    pip3 = which('pip3')
    env = which('env')
    run([pip3, 'install', '--upgrade', 'pipenv'])
    run([env, 'pipenv', 'install', '--dev'])


def cleanup():
    """
    Removing unnecessary files from project directory.
    """
    if '{{ cookiecutter.use_heroku }}' == 'n':
        run(['rm', '-f', 'Procfile', 'app.json', 'runtime.txt'])
    if '{{ cookiecutter.use_postgres }}' == 'n':
        run(['rm', '-rf', 'contrib'])
    if '{{ cookiecutter.use_docker }}' == 'n':
        run(['rm', '-f', 'Dockerfile', '.dockerignore', 'docker-compose.yml'])


if __name__ == '__main__':
    install_dependencies()
    cleanup()
    setup_git_repo()
    print('\n{{cookiecutter.project_slug}} setup successfully!\n\n')
