### [Edx IBM TDD Course](https://www.edx.org/learn/software-development/ibm-test-and-behavior-driven-development-tdd-bdd?index=product&queryId=b605814505df63a936d38b971f341eff&position=1)

#### Test Fixtures

An overview on the use of fixtures when setting up consistant test states. For more details please review the [course](COURSE.md) document.

<br />

#### Deviations from The Course


**_Test Framework_**

The course, being legendary, is also dated. As such, the frameworks in use follow suite. As a consequence, **_[nose](nose.readthedocs.io.en/latest)_** has ceased development, suggesting that `(n)ew projects should consider user Nose2, py.tet, or just plain unittest/unittest2`

**_[nose2](github.com/nose-devs/nose2)_**, a fork of _nose_ `encourage(s) users to consider it for new projects`.

**_[pytest](docs.pytest.org/en/stable)_**, amongst other strengths, has an explicity `fixture` decorator which helps emphasis the implementation of fixtures. Quite the treat for this lab.

<br />

**_Test Coverage_**

The suggested library **_[coverage](pypi.org/project/coverage)_** has been replace by **_[pytest-cov](pypi.org/project/pytest-cov)_**. Be aware, coverage only covers the number of lines executed during testing, not the varied cases the code may be subject to. That is should code read as follows:

```
with open( file_path ) as file:
    data = json.load( file )
```

Coverage only considers whether or not the lines come into use and does not consider edge cases such as:
- The file being read in not being present or available
- The inability for `json` to load the file

<br />

**_Step 1: Database Initialization_**

Of note, the database in use, _/instance/test.db_, though named `test.db` actually operated as the production database. Thus using it for testing should be a **no-no**.

At this point of the course, we are executing unit tests; the decision has been made to mock database calls. This allows us to both avoid using the production database, `test.db`, as well as actually making actuall database calls during unit testing. This we can save for the _BDD_ stage of the course.

<br />

**_Step 2: Loading Test Data_**

Two idea are are addressed here.

1. The test data is in the global scope. This is generally frowned upon and is addressed by making it into a test fixture.

2. The course suggests setting this up before the entire session, making it subject to changes between tests. The applied solution sets the data's scope as the entire test session. The data is also converted to `Account` instances, the scope of these is the duration of individual tests and is used in mock database sessions.

<br />

**_Step 5: Clear out hte tables before each test_**

As mentioned previously, the mocked database sessions only last per test. As a redundancy, the is a deliberate rollback and session closure after each test.

<br /> database is mocked

**_Other_**

I have taken the liberty to write tests for the program without concern for the desired outcomes of the lab. Instead, the goal was to achieve _100%_ test coverage. This deviation has lead to both completing this project and possibly touching `lab 04`. Likewise, changes have been made to `Account` to accomodate tests and any functional variations I deemed worth addressing.

<br />
