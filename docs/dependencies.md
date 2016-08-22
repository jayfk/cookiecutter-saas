# Dependencies
Todo 

## Dependencies

### Django
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

Environment: `development`, `production`   
Link: [djangoproject.com](https://www.djangoproject.com/)

### psycopg2
Psycopg is the most popular PostgreSQL adapter for the Python programming language. At its core it fully implements the Python DB API 2.0 specifications. Several extensions allow access to many of the features offered by PostgreSQL.

Environment: `development`, `production`   
Link: [initd.org/psycopg/](http://initd.org/psycopg/)

### django-environ
Django-environ allows you to utilize 12factor inspired environment variables to configure your Django application.

Environment: `development`, `production`   
Link: [github.com/joke2k/django-environ](https://github.com/joke2k/django-environ)

### django-braces
Reusable, generic mixins for Django.

Environment: `development`, `production`   
Link: [github.com/brack3t/django-braces](https://github.com/brack3t/django-braces)

### django-crispy-forms
django-crispy-forms provides you with a |crispy filter and {% crispy %} tag that will let you control the rendering behavior of your Django forms in a very elegant and DRY way. Have full control without writing custom form templates. All this without breaking the standard way of doing things in Django, so it plays nice with any other form application.

Environment: `development`, `production`   
Link: [github.com/maraujop/django-crispy-forms](https://github.com/maraujop/django-crispy-forms)

### django-model-utils
Django model mixins and utilities.

Environment: `development`, `production`   
Link: [github.com/carljm/django-model-utils](https://github.com/carljm/django-model-utils)

### Pillow
Pillow is the friendly PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors.

Environment: `development`, `production`   
Link: [pillow.readthedocs.io](https://pillow.readthedocs.io)

### django-allauth
Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.

Environment: `development`, `production`   
Link: [github.com/pennersr/django-allauth](https://github.com/pennersr/django-allauth)

### unicode-slugify
Unicode Slugify is a slugifier that generates unicode slugs. It was originally used in the Firefox Add-ons web site to generate slugs for add-ons and add-on collections. Many of these add-ons and collections had unicode characters and required more than simple transliteration.

Environment: `development`, `production`   
Link: [pypi.python.org/pypi/unicode-slugify](https://pypi.python.org/pypi/unicode-slugify)

### django-autoslug
Django-autoslug is a reusable Django library that provides an improved slug field which can automatically:

- populate itself from another field,
- preserve uniqueness of the value and
- use custom slugify() functions for better i18n.

The field is highly configurable.

Environment: `development`, `production`   
Link: [pypi.python.org/pypi/django-autoslug](https://pypi.python.org/pypi/django-autoslug)

### pytz
pytz brings the Olson tz database into Python. This library allows accurate and cross platform timezone calculations using Python 2.4 or higher. It also solves the issue of ambiguous times at the end of daylight saving time, which you can read more about in the Python Library Reference (datetime.tzinfo).

Environment: `development`, `production`   
Link: [pythonhosted.org/pytz/](http://pythonhosted.org/pytz/)

### django-redis
Full featured redis cache backend for Django.

Environment: `development`, `production`   
Link: [github.com/niwinz/django-redis](https://github.com/niwinz/django-redis)

### redis
The Python interface to the Redis key-value store.

Environment: `development`, `production`   
Link: [pypi.python.org/pypi/redis](https://pypi.python.org/pypi/redis)

### celery
Celery is an asynchronous task queue/job queue based on distributed message passing.	It is focused on real-time operation, but supports scheduling as well.
The execution units, called tasks, are executed concurrently on a single or more worker servers using multiprocessing, Eventlet,	or gevent. Tasks can execute asynchronously (in the background) or synchronously (wait until ready).

Environment: `development`, `production`   
Link: [www.celeryproject.org/](http://www.celeryproject.org/)

### django_compressor
Django Compressor processes, combines and minifies linked and inline Javascript or CSS in a Django template into cacheable static files.

It supports compilers such as coffeescript, LESS and SASS and is extensible by custom processing steps.

Django Compressor is compatible with Django 1.8 and newer.

Environment: `development`, `production`   
Link: [github.com/django-compressor/django-compressor](https://github.com/django-compressor/django-compressor)


### pinax-stripe
pinax-stripe is a payments Django app for Stripe.

This app allows you to process one off charges as well as signup users for recurring subscriptions managed by Stripe.

Environment: `development`, `production`   
Link: [github.com/pinax/pinax-stripe](https://github.com/pinax/pinax-stripe)

### PyJWT
JSON Web Token implementation in Python.

Environment: `development`, `production`   
Link: [github.com/jpadilla/pyjwt](https://github.com/jpadilla/pyjwt)

### django-celery-email
A Django email backend that uses a Celery queue for out-of-band sending of the messages.

Environment: `development`, `production`   
Link: [github.com/pmclanahan/django-celery-email](https://github.com/pmclanahan/django-celery-email)

### mailchimp
A Python API client for v2 of the MailChimp API.

Environment: `development`, `production`   
Link: [bitbucket.org/mailchimp/mailchimp-api-python/](https://bitbucket.org/mailchimp/mailchimp-api-python/)

### django-loginas
"Login as user" for the Django admin.

Environment: `development`, `production`   
Link: [github.com/stochastic-technologies/django-loginas](https://github.com/stochastic-technologies/django-loginas)

### django-webpack-loader `react == yes`
Django webpack loader consumes the output generated by webpack-bundle-tracker and lets you use the generated bundles in django.

Environment: `development`, `production`   
Link: [github.com/owais/django-webpack-loader](https://github.com/owais/django-webpack-loader)

### djangorestframework `react==yes`
Django REST framework is a powerful and flexible toolkit for building Web APIs.

Some reasons you might want to use REST framework:

- The Web browsable API is a huge usability win for your developers.
- Authentication policies including packages for OAuth1a and OAuth2.
- Serialization that supports both ORM and non-ORM data sources.
- Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
- Extensive documentation, and great community support.
- Used and trusted by internationally recognised companies including Mozilla, Red Hat, Heroku, and Eventbrite.


Environment: `development`, `production`   
Link: [www.django-rest-framework.org](http://www.django-rest-framework.org/)

### django-tinymce `blog==yes`
django-tinymce is a Django application that contains a widget to render a form field as a TinyMCE editor.

Environment: `development`, `production`   
Link: [github.com/aljosa/django-tinymce](https://github.com/aljosa/django-tinymce)

## Development Dependencies

### coverage
Coverage.py measures code coverage, typically during test execution. It uses the code analysis tools and tracing hooks provided in the Python standard library to determine which lines are executable, and which have been executed.

Environment: `development`   
Link: [pypi.python.org/pypi/coverage](https://pypi.python.org/pypi/coverage)

### django-coverage-plugin
A plugin for coverage.py to measure Django template execution

Environment: `development`   
Link: [github.com/nedbat/django_coverage_plugin](https://github.com/nedbat/django_coverage_plugin)

### django-extensions
Django Extensions is a collection of custom extensions for the Django Framework.

Environment: `development`   
Link: [github.com/django-extensions/django-extensions](https://github.com/django-extensions/django-extensions)

### Werkzeug
Werkzeug started as a simple collection of various utilities for WSGI applications and has become one of the most advanced WSGI utility modules. It includes a powerful debugger, fully featured request and response objects, HTTP utilities to handle entity tags, cache control headers, HTTP dates, cookie handling, file uploads, a powerful URL routing system and a bunch of community contributed addon modules.

Environment: `development`   
Link: [werkzeug.pocoo.org](http://werkzeug.pocoo.org/)

### django-test-plus
Let’s face it, writing tests isn’t always fun. Part of the reason for that is all of the boilerplate you end up writing. django-test-plus is an attempt to cut down on some of that when writing Django tests.

Environment: `development`   
Link: [github.com/revsys/django-test-plus](https://github.com/revsys/django-test-plus/)

### factory-boy
factory_boy is a fixtures replacement based on thoughtbot's factory_girl.

As a fixtures replacement tool, it aims to replace static, hard to maintain fixtures with easy-to-use factories for complex object.

Environment: `development`   
Link: [github.com/FactoryBoy/factory_boy](https://github.com/FactoryBoy/factory_boy)

### django-debug-toolbar
The Django Debug Toolbar is a configurable set of panels that display various debug information about the current request/response and when clicked, display more details about the panel's content.

Environment: `development`   
Link: [github.com/jazzband/django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)

### ipdb
ipdb exports functions to access the IPython debugger, which features tab completion, syntax highlighting, better tracebacks, better introspection with the same interface as the pdb module.

Environment: `development`   
Link: [github.com/gotcha/ipdb](https://github.com/gotcha/ipdb)
## Production Dependencies

### uWSGI
The uWSGI project aims at developing a full stack for building hosting services.

Application servers (for various programming languages and protocols), proxies, process managers and monitors are all implemented using a common api and a common configuration style.

Thanks to its pluggable architecture it can be extended to support more platforms and languages.

Currently, you can write plugins in C, C++ and Objective-C.

The “WSGI” part in the name is a tribute to the namesake Python standard, as it has been the first developed plugin for the project.

Versatility, performance, low-resource usage and reliability are the strengths of the project (and the only rules followed).

Environment: `production`   
Link: [github.com/unbit/uwsgi](https://github.com/unbit/uwsgi)

### django-anymail
Django email backends and webhooks for Mailgun, Postmark, SendGrid, SparkPost and more

Environment: `production`   
Link: [github.com/anymail/django-anymail](https://github.com/anymail/django-anymail)

### raven
Raven is a Python client for Sentry. It provides full out-of-the-box support for many of the popular frameworks, including Django, and Flask. Raven also includes drop-in support for any WSGI-compatible web application.

Environment: `production`   
Link: [github.com/getsentry/raven-python](https://github.com/getsentry/raven-python)

### newrelic
New Relic's Python agent monitors your application to help you identify and solve performance issues. You can also extend the agent's performance monitoring to collect and analyze business data to help you improve the customer experience and to make data-driven business decisions. With flexible options for custom instrumentation and agent-specific APIs, New Relic's Python agent offers multiple building blocks to customize the data you need for your app.

Environment: `production`   
Link: [New Relic Docs](https://docs.newrelic.com/docs/agents/python-agent/getting-started/new-relic-python)
