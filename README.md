### [Edx IBM TDD Course](https://www.edx.org/learn/software-development/ibm-test-and-behavior-driven-development-tdd-bdd?index=product&queryId=b605814505df63a936d38b971f341eff&position=1)

#### Practicing TDD

In this lab, one will write test cases based on the requirements given below, and then one will write the code to make the test cases pass.

<br />

#### Requirements

Assume you have been asked to create a web service that can keep track of multiple counters. The web service has the following requirements:

    • The API must be RESTful.
    • The endpoint must be called /counters.
    • When creating a counter, you must specify the name in the path.
    • Duplicate names must return a conflict error code.
    • The service must be able to update a counter by name.
    • The service must be able to get a counter’s current value.
    • The service must be able to delete a counter.

The last three requirements have not been implemented. You have been asked to implement them using TDD principles by writing the test cases first, and then writing the code to make the test cases pass.

<br />

#### API Guideline

There are guidelines for creating REST APIs that enable you to write the test cases for this lab:

| Action   |  Method  | Status Code | Informational |       URL        |
| :------- | :------- | ----------: | ------------: | ---------------: |
| Create   |    POST  |         201 |       CREATED | /counters/<name> |
| Read     |     GET  |         200 |            OK | /counters/<name> |
| Update   |     PUT  |         200 |            OK | /counters/<name> |
| Delete   |  DELETE  |         204 |        DELETE | /counters/<name> |

Following these guidelines, you can make assumptions about how to call the web service and assert what it should return.

<br />
