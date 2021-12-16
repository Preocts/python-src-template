# Contributing

Before contributing, please either ask to claim an existing open issue or create a new issue to discuss your proposed changes with the owner(s) of this repo before making any changes.

*Any pull requests without an approved issue associated with them will be closed*

## Bug reports

Found a bug but do not have time or do not wish to contribute a fix? Please submit an issue for our awareness. Your feedback drives the continued development of the project!

## Fork

Create your own fork of this repo that you will make your changes on.

## Creating your feature

Always base your changes off the `main` branch, it is the most up to date.

## Pull Request

Once the feature is tested and ready, open a pull request to the `main` branch.

Please ensure your tests are passing in your local environment and any new features are have appropriate tests added.  Untested code will not be approved.

## Code Style

Follow the patterns seen in the code. Walk where others have walked.

The majority of code style nits will be met simply by passing `pre-commit` checks prior to submitting a pull request.

- ### Do
  - snake_case modules, variables, methods, and functions
  - PascalCase classes
  - Type-hint function/method signatures
  - Use verbs for getters/setters (`get_`, `fetch_`, `pull_`, `save_`, `put_`)
  - Use singular form for objects
  - Use plural form for lists/sequences
- ### Do Not
  - Fight `black` formatting
- ### Comments
  - Keep comments short and to the point
  - Let code explain "what" and comments explain "why"
  - All modules, functions, class, and methods must have a doc-string
  - Doc-strings are optional in tests when the test name explains "what"
- ### Tests
  - Smaller tests are easier to work with
  - Mock at a minimum
  - No test should be dependent on another
  - No test should be dependent on secrets/tokens
