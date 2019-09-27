import subprocess
from pathlib import Path


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
    print(git)
    run([git, 'init'])
    run([git, 'add', '.'])
    run([git, 'status'])
    run([git, 'commit', '-m', 'Initial commit'])


def setup_virtualenv(python):
    python = which(python)
    try:
        # First try bundled venv module
        import venv     # noqa
        run([python, '-m', 'venv', './env'])
    except ImportError:
        # Second try use virtualenv
        try:
            virtualenv = which('virtualenv')
            run([virtualenv, '-p', python, './venv'])
        except AssertionError:
            raise RuntimeError('Python venv module or virtualenv required')


def install_dependencies():
    """
    Install project dependencies inside venv.
    """
    python = which('python')
    env = which('env')
    run([python, '-m', 'ensurepip', 'install', '-U', 'pipenv'])
    run([env, 'pipenv', 'install'])


def cleanup():
    """
    Removing unnecessary files from project directory.
    """
    # if '{{ cookiecutter.use_heroku }}' == 'n':
    #     run(['rm', '-f', 'Procfile', 'app.json', 'runtime.txt'])
    if '{{ cookiecutter.use_docker }}' == 'n':
        run(['rm', '-f', 'Dockerfile', '.dockerignore', 'docker-compose.yml'])


if __name__ == '__main__':
    setup_git_repo()
    install_dependencies()
    print('\n{{cookiecutter.project_slug}} setup successfully!\n\n')
    cleanup()
