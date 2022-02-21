# Lab: DjangoX

## Overview

It is quite common to set up your Django projects the same way every time.

Some of those common tasks are...

- Create a custom user
- Configure static assets
- Add authentication
- Set up styling
- Install common libraries
- Wire up 3rd party development tools

Repeating these steps over and over violates the DRY (Don't Repeat Yourself) rule. So pro developers usually create a skeleton application they use to start off their projects.

Luckily for us, there's already a great example of such a skeleton - [DjangoX](https://github.com/wsvincent/djangox){:target="_blank"}

## Feature Tasks and Requirements

- Create a website using DjangoX as a template.
  - Click the `Use this template` button on home page of DjangoX repository.
- Name your repo whatever you like.
- Create a Django app of your choosing.
- The specific functionality of the site is up to you but should have a model that makes use of `get_user_model`

## Implementation Notes

DjangoX does not use poetry out of the box. So you'll need to look at the files DjangoX does use to see which dependencies are used.

- View `Pipfile` and note the [packages] section.
  - Install packages listed in Pipfile
- Delete the configuration files if not using `pipenv` and other files not needed.
  - Pipfile
  - Pipfile.lock
  - Dockerfile
  - docker-compose.yml
  - requirements.txt

### User Acceptance Tests

- Verify that your pages render as expected.

## Configuration

- Clone your newly created repo.
- Create a virtual environment.
- Add dependencies (see Implemetation Notes)
- Remove unnecessary configuration files (see Implementation Notes)

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.

## Stretch

- Add social authentication.
- Add images to your site.
