When should BDD/acceptance tests be executed relative to unit tests? 
Should they always run together, or should they be treated differently (e.g., executed less frequently, in a separate CI stage)?

BDD tests should preferably be executed after unit tests, as unit tests focus more on the technical sides and BDD moreover on the behavior of the application.
They should be treated differently as they provide different purposes and are not one and the same.
For our project we recommend to use unit tests after code changes, and if the components work together then do BDD/acceptance tests as the more functionality is developed, the behaviour tests will get more time consuming and debugging will be easier when working with the code files in contrast to only seeing that a feature is broken when the behaviour test fails.
Execution time of unit tests are on average measured in seconds, while BDD tests can take minutes or hours, so it seems most time efficient if used in that order.
Therefore the order in which we plan to use these is first a stage of unit tests to evaluate the functionality of what has been implemented and then a stage of BDD/acceptance tests.

How the mockability of your external dependency affects this decision:
As the dependency will deliver certain responses that can be categorized, they can also be tested by these categories, which are recreatable without the dependency itself.
For example the responses can contain the current date, if there's a holiday, which season it is or that the dependency wasn't reachable.
These can be categorized into succesfull and unsuccesful. As the scenarios can vary from each other, you don't need to test every single one, but only the ones that differ in functionality.
We expect certain responses from the dependency and therefore can explicitly test these "artificially".
