# Contributing

Before contributing, please either ask to claim an existing open issue or create
a new issue to discuss your proposed changes with the owner(s) of this repo
before making any changes.

*Any pull requests without an approved issue associated with them will be
closed*

## Bug reports

Found a bug but do not have time or do not wish to contribute a fix? Please
submit an issue for our awareness. Your feedback drives the continued
development of the project!

## Fork

Create your own fork of this repo that you will make your changes on.

## Creating your feature

Always base your changes off the `main` branch unless otherwise asked.

## Pull Request

All pull requests must:

- Pass all linting and formatting checks
- Have tests that cover all branches of the added feature
- If the PR is a bug fix there must be a test that duplicates the bug, proving
  it is fixed

## Code Style

Follow the patterns seen in the code. Walk where others have walked.

The majority of code style nits will be met when passing `pre-commit` checks
prior to submitting a pull request.

## Tests

  - Smaller tests are easier to work with
  - Mock at a minimum
  - No test should be dependent on another
  - No test should be dependent on secrets/tokens
