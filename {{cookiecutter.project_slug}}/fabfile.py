# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals
from fabric.api import env, local, prefix
import time
import re


def production():
    """
    Work on the production environment
    """
    env.compose_file = "production.yml"
    env.machine = "{{ cookiecutter.project_slug }}"


def docker_machine(machine):
    """
    Sets the environment to use a given docker machine.
    """
    _env = local('docker-machine env {}'.format(machine), capture=True)
    # Reorganize into a string that could be used with prefix().
    _env = re.sub(r'^#.*$', '', _env, flags=re.MULTILINE)  # Remove comments
    _env = re.sub(r'^export ', '', _env, flags=re.MULTILINE)  # Remove `export `
    _env = re.sub(r'\n', ' ', _env, flags=re.MULTILINE)  # Merge to a single line
    return _env


def restart_caddy():
    build_and_restart("caddy")


def deploy():
    """
    Pulls the latest changes from master, rebuilt and restarts the stack
    """

    docker_compose("run postgres backup")
    build_and_restart("node")
    build_and_restart("django")
    time.sleep(10)

    build_and_restart("django-failover")
    build_and_restart("celerybeat")
    build_and_restart("celeryworker")


def build_and_restart(service):
    docker_compose("build " + service)
    docker_compose("create " + service)
    docker_compose("stop " + service)
    docker_compose("start " + service)


def docker_compose(command):
    """
    Run a docker-compose command
    :param command: Command you want to run
    """
    if(env.machine):
        with prefix(docker_machine(env.machine)):
            return local(
                "docker-compose -f {file} {command}".format(
                    file=env.compose_file, command=command)
            )
    return local(
        "docker-compose -f {file} {command}".format(
            file=env.compose_file, command=command)
    )
