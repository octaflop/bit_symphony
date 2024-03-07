# Bit Symphony

Data Orchestration: What is it, and how do I do it in Python?

## Setup

This repo is intended to be copied to your machine and have its python packages installed to `.venv`.

Basically, install python 3.12, then:

`python3.12 -m venv .venv`

`. .venv/bin/activate`

`pip install -e ".[dev]"`

### And the trickiest bit is all the API logins

So first copy `.env.example` to `.env`

`cp .env.example .env`

Then you will need to make an account for each of these accounts, copy the tokens and configs into this file.

## Running Dagster

Go ahead and run

`dagster dev`

Then browse to your [localhost](https://127.0.0.1:3000) deployment.