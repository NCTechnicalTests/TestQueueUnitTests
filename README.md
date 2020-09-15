# TestQueueUnitTests
The goal of this tests is to write code for a basic class and then write the appropriate unit tests to cover different methods of the class

The queue can be implemented using any other object in python.  The input and output of the methods are predefined.

This queue class is similar to a regular to a regular queue with following differences:
- On initialisation, we can force the queue to only accept positive integers
- The add method only accept integers and need to raise exception when other input types are provided
- The pop method needs to raise exception if queue is empty
- The dump_to_db method simulate a write to an external system using a DbWriter object

For this test, the DbWriter class doesn't need to be modified.

#Test instruction

1. Please add code in TheQueue class and create required unit tests
   - Unit tests are executed using pytest
   - Make sure unit tests are passing :)
2. Commit and push your code and unit tests (push to your own branch)
3. Create pull request of the final code/branch
