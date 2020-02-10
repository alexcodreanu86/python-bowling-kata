## Python template

### Installation

##### Make sure you have `pip` installed on your machine.

If you have pip installed
```
pip install -r requirements.txt
```

If you have pip3 installed
```
pip3 install -r requirements.txt
```

### Running tests

The following command should run all your tests
```
pytest
```

Presentation:

Talk about what TDD is.
- All new code is added to fix a failing test, and only enough code is added to fix that test.

Common misconception: Write all tests before you write any code.


TDD cycle

Write a failing test: Red - color of what you usually see in your test runner
compiler/build failures are also valid failures


Write just enough code to make the test pass: Green
Don't focus too much on making the code clean at this stage, just focus on resolving the failing test


Refactor:
One the test passes you can do a quick scan if there's anything that needs cleaning up:
Extract function helper, improve some name, remove duplication.
!!! Tests are also code, so see if you can clean up the tests as well.


Test structure:
I like following the tripple "A" Rule (AAA):
Assemble - test setup

Act - the action that triggers that behavior that we are testing

Assert - all assertion ran on the result of the action


During demo:
IMO tests can tolerage a higher amount of duplication, if it improves test understanding.
Things to highlight in a test:
What is special about the test, not just in the test name, but also in the setup. Try to remove noise that may distract from the test

Always start from the simplest case scenario, and build in complexity.

A test should be as self contained as possible. No order dependency between tests

Final toughts:
I think TDD encourages you to think of all the failure scenarios first. Because in a lot of cases we bail out of a function at the first encountered failure
With TDD you don't have to spend a certain amount of time writing tests after you've completed the feature.
The feedback loop is most of the time tighter than restarting an app.
