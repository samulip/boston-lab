# boston-lab
An excercise for a workflow in Jupyter. Name refers to the Boston Housing dataset from Sklearn used in the code snippets organized in this excercise.

# References

This excercise is based on two blog post from November 2018:

Florian Wilhelm
[https://florianwilhelm.info/2018/11/working_efficiently_with_jupyter_lab/]

Christopher Prohm
[https://cprohm.de/article/notebooks-and-modules.html]

# Notes

Pipenv really takes it time to execute. Decision to avoid conda for now.

Nteract not yet tested or explored.

Nbdime needed edits in .git/config for git to function outside pipenv.

Local package refers to project. Change if copying.

Use autoreload to get local module updates into notebook.

No actual tests for the model right now.

Current version of ipytest exposes ipytest.running_as_test.

Invoke task "test" linked to Pipfile and precommit but does not invoke separate linter for now.

Does not use PyScaffold for now.


