# Cookiecutter SaaS Settings

This document is still a work in progress, see [#38](https://github.com/jayfk/cookiecutter-saas/issues/38)

## SAAS_PLANS

`SAAS_PLANS` is a 1:1 mapping to your plans on stripe.

To add a new plan, log into your stripe account and create a new plan.

Once created, run:
    docker-compose run django python manage.py sync_plans

and add the plan to `SAAS_PLANS`.

The key is the plan id, so a plan with the id `basic` would look like this:

```python
"basic": {
    "description": "Basic Plan Description",
    "features": [
        "Feature 1",
        "Feature 2",
    ]
},
```

If you have set `SAAS_SUBSCRIPTION_TYPE` to `trial` or `free`, you'll also need to add the plan here 
(Cookiecutter does this automatically during project setup). 

**freemium**:
Every new user will be subscribed to the `free` plan automatically if you set `SAAS_SUBSCRIPTION_TYPE` to `freemium`.

```python
"free": {
    "description": "Free Plan Description",
     "features": [
          "Feature 1",
     ]
},
```

**trial**:
Every new user will be subscribed to this plan automatically if you set `SAAS_SUBSCRIPTION_TYPE` to `trial`. 
The length of the trial is set with `SAAS_TRIAL_LENGTH` and defaults to 14 days.

```python
"trial": {
     "description": "Trial Plan Description",
     "features": [
        "Feature 1",
     ]
}
```

## SAAS_TRIAL_LENGTH

Sets the length of the trial for each new user, if `SAAS_SUBSCRIPTION_TYPE=='trial'`. Use a timedelta.

## SAAS_SUBSCRIPTION_TYPE

The `SAAS_SUBSCRIPTION_TYPE` sets the default plan for new users. 

Allowed values are:
- freemium: The user is subscribed to a free plan that never expires.
- trial: The user is subscribed to a trial plan that expires after `SAAS_TRIAL_LENGTH` which defaults to 14 days.
- None: The user is not subscribed to any plan and has to subscribe to a paid plan.

## SAAS_PRIVATE_BETA

Setting `SAAS_PRIVATE_BETA` to `True` sets the page in private beta mode:

- The default user registration is blocked
- Users interested in the private beta can request an invite
- Invites are managed through the admin interface
- Only users with an invite can create a new account

## SAAS_INFO_MAIL

This email receives info mails once a new account is created, or a user requests an invite to the site (if in private beta mode).
