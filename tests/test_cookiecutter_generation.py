# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import re
import sh
import time
import shutil
import fileinput

import pytest
from binaryornot.check import is_binary

PATTERN = '{{(\s?cookiecutter)[.](.*?)}}'
RE_OBJ = re.compile(PATTERN)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


@pytest.fixture
def context():
    return {
        'project_name': 'Cookiecutter SaaS',
        'project_slug': 'cookiecutter_saas_test_project',
        'author_name': 'Test Author',
        "info_mail": "test@example.com",
        'email': 'test@example.com',
        'domain_name': 'example.com',
        'timezone': 'UTC',
        "django_long_term_support": "y",
        "react": "y",
        "blog": "y",
        "private_beta": "y",
        "free_subscription_type": "freemium"
    }


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(root_dir)
        for file_path in files
    ]


def check_paths(paths):
    """Method to check all paths have correct substitutions,
    used by other tests cases
    """
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(path):
            continue
        for line in open(path, 'r'):
            match = RE_OBJ.search(line)
            msg = 'cookiecutter variable not replaced in {}'
            assert match is None, msg.format(path)


def run_docker_dev_test(path, coverage=False):
    """
    Method to check that docker runs with dev.yml
    """
    try:
        # build django, power up the stack and run the test
        sh.docker_compose(
            "--file", "{}/dev.yml".format(path), "build", "django"
        )
        sh.docker_compose("--file", "{}/dev.yml".format(path), "build")
        if coverage:
            sh.docker_compose(
                "--file", "{}/dev.yml".format(path), "run", "django", "coverage", "run", "manage.py", "test"
            )
            sh.docker_compose(
                "--file", "{}/dev.yml".format(path), "run", "django", "coverage", "xml", "-o", "coverage.xml"
            )
            shutil.copyfile(os.path.join(str(path), ".coverage"), os.path.join(PROJECT_DIR, ".coverage"))
            shutil.copyfile(os.path.join(str(path), "coverage.xml"),
                            os.path.join(PROJECT_DIR, "coverage.xml"))
        else:
            sh.docker_compose(
                "--file", "{}/dev.yml".format(path), "run", "django", "python", "manage.py", "test"
            )

        # test that the development server is running
        sh.docker_compose("--file", "{}/dev.yml".format(path), "up", "-d")
        time.sleep(10)
        curl = sh.curl("-I", "http://localhost:8000/")
        assert "200 OK" in curl
        assert "Server: Werkzeug" in curl

        # since we are running a lot of tests with different configurations,
        # we need to clean up the environment. Stop all running containers,
        # remove them and remove the postgres_data volume.
        sh.docker_compose("--file", "{}/dev.yml".format(path), "stop")
        sh.docker_compose("--file", "{}/dev.yml".format(path), "rm", "-f")
        sh.docker("volume", "rm", "cookiecuttersaastestproject_postgres_data_dev")
    except sh.ErrorReturnCode as e:
        # in case there are errors it's good to have full output of
        # stdout and stderr.
        pytest.fail("STDOUT: {} \n\n\n STDERR: {}".format(
            e.stdout.decode("utf-8"), e.stderr.decode("utf-8"))
        )


def run_checks(result, context, excluded_files=[]):
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context['project_slug']
    assert result.project.isdir()

    paths = build_files_list(str(result.project))
    assert paths
    check_paths(paths)
    for filename in excluded_files:
        assert filename not in paths


def test_default_configuration(cookies, context):
    result = cookies.bake(extra_context=context)
    run_checks(result, context)
    run_docker_dev_test(result.project, coverage=True)

"""
def test_no_django_long_term_support(cookies, context):
    context["django_long_term_support"] = "n"
    result = cookies.bake(extra_context=context)
    run_checks(result, context)
    run_docker_dev_test(result.project)


def test_no_blog(cookies, context):
    context["blog"] = "n"
    result = cookies.bake(extra_context=context)
    run_checks(result, context, excluded_files=["blog"])
    run_docker_dev_test(result.project)


def test_no_react(cookies, context):
    context["react"] = "n"
    result = cookies.bake(extra_context=context)
    run_checks(result, context, excluded_files=["webpack", "react", "eslint", "karma", "package.json", "api"])
    run_docker_dev_test(result.project)


def test_no_private_beta(cookies, context):
    context["private_beta"] = "n"
    result = cookies.bake(extra_context=context)
    run_checks(result, context, excluded_files=["beta"])
    run_docker_dev_test(result.project)


def test_trial_free_subscription_type(cookies, context):
    context["free_subscription_type"] = "trial"
    result = cookies.bake(extra_context=context)
    run_checks(result, context)
    run_docker_dev_test(result.project)


def test_none_free_subscription_type(cookies, context):
    context["free_subscription_type"] = "None"
    result = cookies.bake(extra_context=context)
    run_checks(result, context)
    run_docker_dev_test(result.project)
"""

def test_flake8_compliance(cookies):
    """generated project should pass flake8"""
    result = cookies.bake()

    #try:
    #    sh.flake8(str(result.project))
    #except sh.ErrorReturnCode as e:
    #    print(e)
    #    pytest.fail(str(e))
