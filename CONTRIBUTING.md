# Miyagi | Contibution program and guidelines

## Guidelines
Any contribution is welcome.
The TODO list below is a general plan of what I (we!) intend to do next. You can find the actual planned activities looking  in the [Issues](https://github.com/Hrabal/Miyagi/issues) of this repo.

If you want to propose (or ask for) a new feature, if you want to propose a refactoring of some part of the code, or if you find a bug, please open a new issue with your idea.

Every contribution *should* have its tests and will have to pass already written tests. Tests are important, and no merge will be made without some test coverage.
Miyagi tests are written with [Unittest](https://docs.python.org/3/library/unittest.html), every PR you make will be analysed by [Travis CI](https://travis-ci.org/Hrabal/Miyagi).

### Code Style
This project does not have a coding style guideline (except [PEP8](https://www.python.org/dev/peps/pep-0008/) and [PEP20](https://www.python.org/dev/peps/pep-0020/) of course) , just code as you like to code!

## Workflow
Every development is tracked using Issues. If you want to work on a specific issue, ask for assignement. And if you don't find an issue for what you want to work on, open a new issue with your proposed development.

Small (2/3 commits, 1 contributor) contributions should follow this simple workflow:
- Ask to be assigned to the issue
- Fork this repo: [GitHub guide on forking](https://help.github.com/articles/fork-a-repo/)
- Do the coding on the forked repo in the master branch
- Make a Pull Request: [GitHub guide on making a PR](https://help.github.com/articles/about-pull-requests/)
Some CI and code quality services will be triggered and 5/10 mins after your PR you'll see in the PR page if your contribution is breaking some tests, if it contain some code that can be made better and if it have a good test coverage.
I'll check the PR and merge, or review your code if I have suggestions on something you wrote.

Bigger developments (i.e: a new widget, a new complex feature, a deep refactor, more than one person working on the feature) etc..) will follow a different workflow:
- Discuss the development strategy on the Issue
- Discuss particular problems in the Slack channel
- I'll make a new branch dedicated to this feature with no CI
- When the feature is ready I'll perform the merge into the master branch

## TODO plan:
Planned evolution of this project:
- [ ] command line interface to complete.
- [ ] json api to complete.
- [ ] web GUI to complete using websockets.
- [ ] Better exception handling.
- [ ] Writing docstrings.
- [ ] Requests logging.
- [ ] Audit trail implementation.
- [ ] Writing tests.

See [open issues](https://github.com/Hrabal/Miyagi/issues) for a complete list of contribution opportunities on bugs.
