# Deploying to Production

This is still a work in progress, see [#35](https://github.com/jayfk/cookiecutter-saas/issues/35)

*In order to deploy Cookiecutter SaaS to production, you need to buy the [production addon](https://gumroad.com/l/CgvLn).*

## 1.) Create a Server with Docker Machine
	
	docker-machine create <name> --driver=digitalocean --digitalocean-access-token=<TOKEN> --digitalocean-region=fra1


	docker-machine ip {{ cookiecutter.project_slug }}

## 2.) Set up DNS Records

Before we start to deploy our project to production, we need to set up the DNS records.  

## 3.) Start the Stack

Start it

     docker-compose -f prod.yml up -d
     
Take a look at the logs

     docker-compose -f prod.yml logs
     
Once you see a constant stream of messages from `django` and `django-failover` (this is the health check), your app is ready.
    
Now, create a superuser:

    docker-compose -f prod.yml run django python manage.py createsuperuser
    
## Zero Downtime Deployments 

Todo
