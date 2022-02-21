# Lab: Serverless Functions

## Overview

Deploy a serverless function to the cloud.

## Feature Tasks and Requirements

- Sign up with [Vercel](https://vercel.com/docs/get-started){:target="_blank"}.
- Create a repository on Github and link it to Vercel account.
- Create a serverless function following Vercel's steps.
  - The function should handle a `GET` http request.
  - The function should accomplish some useful task.
  - The function should parse the url path's query string.

## Stretch Goals

- Handle HTTP methods beyond `GET`.
- Create a simple html front end to interact with serverless function.
- Use `venv` & `pip install` instead of `poetry`
- Use [requests](https://docs.python-requests.org/en/latest/){:target="_blank"} library to interact with a separate API.

## Implementation Notes

- Vercel has a free plan. No credit card is required.
- The [Vercel CLI](https://vercel.com/docs/concepts/deployments/overview#vercel-cli){:target="_blank"} is useful (but not required) for local testing.
- Vercel expects a `requirements.txt` file listing any dependencies.
  - See [poetry export command](https://python-poetry.org/docs/cli/#export){:target="_blank"} docs to export dependencies.

### User Acceptance Tests

- Project `README.md` should include steps to manually test.

## Configuration

- Name your Github project `serverless`.
- File structure should match Vercel's [Python requirements](https://vercel.com/docs/concepts/functions/supported-languages#python){:target="_blank"}.
  - Refer to demo for details.
