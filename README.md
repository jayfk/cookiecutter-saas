[![Updates](https://pyup.io/repos/github/jayfk/cookiecutter-saas/shield.svg)](https://pyup.io/repos/github/jayfk/cookiecutter-saas/)
[![Build Status](https://travis-ci.org/jayfk/cookiecutter-saas.svg?branch=master)](https://travis-ci.org/jayfk/cookiecutter-saas) 
[![codecov](https://codecov.io/gh/jayfk/cookiecutter-saas/branch/master/graph/badge.svg)](https://codecov.io/gh/jayfk/cookiecutter-saas)
[![Documentation Status](https://readthedocs.org/projects/cookiecutter-saas/badge/?version=latest)](http://cookiecutter-saas.readthedocs.io/en/latest/?badge=latest)


# Features

- 100% test coverage
- react & redux integration (optional)
- private beta mode (optional)
- user registration and authentication
- subscriptions with stripe, invoicing and VAT collection with Octobat
- error reporting with sentry
- newsletter sign ups with mailchimp
- application monitoring with new relic
- zero downtime deployments
- full docker for development and production
- HTTPs only with let's encrypt on production
- managed media and static files
- scalable
- emails

# Stack

- Django
- Celery task queue
- React & Redux (optional)
- Redis
- Postgres
- Caddy web server

# Installation

First, you need to install Cookiecutter:

    pip install cookiecutter

Now run it against this repo:

	cookiecutter https://github.com/jayfk/cookiecutter-saas
	
Cookiecutter will prompt you for some options on how the project should be generated for you. If you are doing this for the first time, check out the [prompts section](#todo-link-to-prompts) in the docs.

```
project_name [project_name]: Demo
project_slug [demo]:
author_name [Jannis Gebauer]:
email [ja.geb@me.com]:
info_mail [ja.geb@me.com]:
domain_name [example.com]: demo.cookiecutter-saas.com
timezone [UTC]:
Select django_long_term_support:
1 - yes
2 - no
Choose from 1, 2 [1]: 2
Select react:
1 - yes
2 - no
Choose from 1, 2 [1]: 1
Select blog:
1 - yes
2 - no
Choose from 1, 2 [1]: 1
Select private_beta:
1 - yes
2 - no
Choose from 1, 2 [1]: 1
Select free_subscription_type:
1 - freemium
2 - trial
3 - None
Choose from 1, 2, 3 [1]: 1
```

Once Cookiecutter finishes, enter the project directory and take a look around:

    cd demo/
    ls -la
