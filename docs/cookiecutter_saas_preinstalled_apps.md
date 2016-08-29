# Preinstalled Apps

This section is still incomplete, see [#38](https://github.com/jayfk/cookiecutter-saas/issues/38)

## Beta
*This app is optional.*

Adding the `beta` app allows you to run your site in private beta mode. This is extremely valuable if you plan to launch your site to a limited audience.

During the private beta:

- The default user registration is blocked
- Users interested in the private beta can request an invite
- Invites are managed through the admin interface
- Only users with an invite can create a new account

The workflow comes down to:

- User visits the site, clicks on create account
- User is redirected to a page where he can request an invite
- You get a mail with a link to send out an invite to the user
- If you choose to add the user, he gets a mail with a link and a special invite code.
- User clicks on the link and can now create an account.

To disable private beta mode, set `SAAS_PRIVATE_BETA` to `False`. 

To completely remove it:

- Remove the app from `LOCAL_APPS` in `conf/settings/common.py`.
- Remove the beta urls include in `conf/urls.py`.
- Remove the app from your project directory, located at `<project_name>/beta`.
- Remove the templates from your project directory, located at `<project_name>/templates/beta`.

## Blog
*This app is optional.*

Installs a very basic blog in `<project_name>/beta`.

To completely remove it:

- Remove the app from `LOCAL_APPS` in `conf/settings/common.py`.
- Remove the blog urls include in `conf/urls.py`.
- Remove the app from your project directory, located at `<project_name>/blog`.
- Remove the templates from your project directory, located at `<project_name>/templates/blog`.
