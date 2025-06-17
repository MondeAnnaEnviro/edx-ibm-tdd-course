### [Edx IBM TDD Course](https://www.edx.org/learn/software-development/ibm-test-and-behavior-driven-development-tdd-bdd?index=product&queryId=b605814505df63a936d38b971f341eff&position=1)

#### Mocking Objects

In order to test cases where internet call need be made, we venture into the world of mocking. For more details please review the [course](COURSE.md) document.

<br />

#### Deviations from The Course


**_Tests_**

The primary deviation is using _AccountFactory_ in the _accounts_ fixture. As a side-note, this simple switch hightlights one of the benefits of modular code, a la _fixtures_. Lab 03 had used the read in data as is within tests; in this revision, the data is extracted from each created _Account_ without using the function _to_dict_.

<br />

**_Step 3 to end_**

As a consequence of the deviations made in **Lab 03**, step 3 onward has been rendered null.

<br />
