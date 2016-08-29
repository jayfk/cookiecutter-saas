# Things to Change

*This document is still a work in progress, see [#45](https://github.com/jayfk/cookiecutter-saas/issues/45).*

## Logo & Favicon
The logo is at `static/images/logo.png` and the favicon at `static/images/favicon.png`. Replace them with your own.

### Privacy Policy
Add your privacy policy in `templates/pages/privacy_policy.html`.

### Terms and Conditions
Add your own terms and conditions in `templates/pages/terms_and_conditions.html`.

## Templates
Cookiecutter SaaS uses a total of three base templates. They are based on bootstrap with basic styles from bootswatch.com's flatly theme. You typically want to replace them all with your own base templates and styling.

### Base Template
Located at: `templates/base.html`

The base template for every page outside of the application. For example the startpage, the features page, the pricing page etc.
Todo add image here

### Blank Base Template
Located at: `templates/base_blank.html`

Base template for all pages with very little content and a call to action. For example, user sign ups, email verification, error pages.
Todo add image here

### App Base Template
Located at: `templates/app/base.html`

This is the base template for your app.
Todo add image here
