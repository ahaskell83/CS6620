
# CI/CD pipeline part 2




References: 
https://medium.com/@AlexanderObregon/how-to-build-a-simple-rest-api-with-flask-in-python-9adcd56cf3da

https://flask.palletsprojects.com/en/stable/testing/

https://www.geeksforgeeks.org/python/flask-creating-rest-apis/




# CI/CD pipeline part 1

When working on a software team, different programmers need to add features and fixes to the same code base without breaking anything. Typically the team maintains guarantees around consistency and quality in the form of automated testing. When a contributor adds or changes code to a branch in a repository, tests run and give feedback. This indicates that behavior under test did not change--at least, not in a way that caused test failures. Github commonly hosts software and offers a straightforward approach to creating automation pipelines, which they call "workflows".

 

### Create a repository containing some code:
 https://github.com/ahaskell83/CS6620.git


### Relevant tests for that code:
[Testing for Cat and Clowder Classes](test_cat_code.py)

### Dependency management file(s):

[requirements.txt](requirements.txt)
 
Note: When creating this file must omit local paths so need to use: 

pip list --format=freeze >requirements.txt

### Workflow that runs whenever a user changes either:
[Github Workflow Code](.github/workflows/assign_1_ci.yml)


### To run workflow ad hoc:

Tests can be run manually via Github Actions.
Click the "Run workflow" button shown below and "Run workflow" again in the menu that appears.

![Github Workflow Screenshot](manual_workflow.png)


### Instructions for running the code and scripts:

All tests will run automatically on any push to the main branch of the repo.

Tests can be run out of repo from the files themselves using the command line with the command:

pytest -v

All project code is located in the "cat_code.py" file and consists of two classes: Cat and Clowder.

A Clowder is a community structure of Cats. You can have an empty Clowder as all cats may be adopted (yay!). The more Cats that live in a clowder, the more likely that the cats will breed. A Cat gestation period is 65 days and all intact females at least one year old can and will have kittens. The number of kittens ranges from 1-9 per intact mom. Cats are identified with a name, date of birth, gender, whether or not they have been neutered or spayed, and their arrival date in the clowder (often the day they are born).

All testing code is located in the "test_cat_code.py" file.


## References:

[Github Docs: Workflows](https://docs.github.com/en/actions/writing-workflows)

https://github.com/devopselvis/github-actions-presentation/tree/main
