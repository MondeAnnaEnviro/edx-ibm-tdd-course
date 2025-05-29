### [Edx IBM TDD Course](https://www.edx.org/learn/software-development/ibm-test-and-behavior-driven-development-tdd-bdd?index=product&queryId=b605814505df63a936d38b971f341eff&position=1)

#### Stack Kata

A test driven implementation of the Stack Kata wherein the developer creates a version of the abstract **stack** data structure.

<br />

#### Running Tests

Ensure the ability to run tests for the provided **Python** source filess. The following packages are expected to be functional:
* nose
* pinocchio
* coverage

Where desired, other test packages may also be used

<br />

# Lab: Running tests with nose

#### Nose Test Framework Configuration

**File:** `setup.cfg`

```
[nosetests]
verbosity=2
with-spec=1
spec-color=1
with-coverage=1
cover-erase=1
cover-package=triangle

[coverage:report]
show_missing = True
```
