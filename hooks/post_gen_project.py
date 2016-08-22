"""
Does the following:

1. rename env.example to .env
2. replace password with random strings
    - POSTGRES_PASSWORD
    - SECRET_KEY
3. remove react files if react isn't going to be used
4. remove beta files if the private beta isn't going to be used
"""
from __future__ import print_function
import os
import random
import shutil

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

# Use the system PRNG if possible
try:
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    using_sysrandom = False


def get_random_string(
        length=50,
        allowed_chars='abcdefghijklmnopqrstuvwxyz0123456789!@#%^&*(-_=+)'):
    """
    Returns a securely generated random string.
    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits
    """
    if using_sysrandom:
        return ''.join(random.choice(allowed_chars) for i in range(length))
    print(
        "Cookiecutter SaaS couldn't find a secure pseudo-random number generator on your system."
        " Please change change your SECRET_KEY variables in conf/settings/local.py and env.example"
        " manually."
    )
    return "CHANGEME!!"


def replace_with_random_string(path, string):
    full_path = os.path.join(PROJECT_DIRECTORY, path)
    with open(full_path) as f:
        file_ = f.read()
    file_ = file_.replace(string, get_random_string(),1)
    with open(full_path, 'w') as f:
        f.write(file_)


def remove_content(content):
    for rel_path in content:
        full_path = os.path.join(PROJECT_DIRECTORY, rel_path)
        if os.path.exists(full_path):
            if os.path.isdir(full_path):
                shutil.rmtree(full_path)
            else:
                os.remove(full_path)


def hook():
    # 1. rename env.example to .env
    os.rename(os.path.join(PROJECT_DIRECTORY, "env.example"),
              os.path.join(PROJECT_DIRECTORY, ".env"))

    # 2. replace password with random strings
    replace_with_random_string('.env', 'CHANGEME_POSTGRES_PASSWORD')
    replace_with_random_string('.env', 'CHANGEME_SECRET_KEY')

    # 3. remove react files if react isn't going to be used
    if '{{ cookiecutter.react }}'.lower() == 'n':
        remove_content([
            ".babelrc",
            ".eslintignore",
            ".eslintrc",
            "karma.conf.js",
            "package.json",
            "webpack.config.js",
            os.path.join("{{ cookiecutter.project_slug }}", "config", "webpack.base.config.js"),
            os.path.join("{{ cookiecutter.project_slug }}", "config", "webpack.local.config.js"),
            os.path.join("{{ cookiecutter.project_slug }}", "config", "webpack.production.config.js"),
            os.path.join("{{ cookiecutter.project_slug }}", "config", "webpack.test.config.js"),
            os.path.join("{{ cookiecutter.project_slug }}", "api"),
            "{{ cookiecutter.project_slug }}-react"
        ])

    # 4. remove blog files if the blog isn't going to be used
    if '{{ cookiecutter.blog }}'.lower() == 'n':
        remove_content([
            os.path.join("{{ cookiecutter.project_slug }}", "blog")
        ])

    # 5. remove beta files if the private beta isn't going to be used
    if '{{ cookiecutter.private_beta }}'.lower() == 'n':
        remove_content([
            os.path.join("{{ cookiecutter.project_slug }}", "beta")
        ])

hook()
