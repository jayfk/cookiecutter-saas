# Beta Instructions

If you are reading this, you should've received a link to a zip file containing the Cookiecutter SaaS project.

## Installation

First, you need to install Cookiecutter:

    pip install cookiecutter

Download the zipfile, unzip it anywhere you want and note down the directory.

Now run cookiecutter against this directory:

	cookiecutter /your/path/to/cookiecutter-saas
	
Cookiecutter will prompt you for some options on how the project should be generated for you. If you are doing this for the first time, check out the [prompts section](prompts.html) in the docs.

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

Once finished, continue with [Developing Locally](development.html).


