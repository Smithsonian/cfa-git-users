**************
Git and GitHub
**************

What is Git?
============
Git is the version control tool that underlies GitHub's repositories. It does not
need a website to run; it runs on your computer, keeping track of changes to files
and allowing you to save snapshots called "commits."

From https://en.wikipedia.org/wiki/Git:

    Git is a distributed version control system that tracks changes in any set
    of computer files, usually used for coordinating work among programmers
    collaboratively developing source code during software development. Its goals
    include speed, data integrity, and support for distributed, non-linear workflows.

What is GitHub?
===============
From https://kinsta.com/knowledgebase/what-is-github/:

    GitHub is a for-profit company that offers a cloud-based Git repository hosting
    service. Essentially, it makes it a lot easier for individuals and teams to use
    Git for version control and collaboration.

    GitHub's interface is user-friendly enough so even novice coders can take advantage
    of Git. Without GitHub, using Git generally requires a bit more technical savvy
    and use of the command line. GitHub is so user-friendly, though, that some people
    even use GitHub to manage other types of projects - like writing books.

    Additionally, anyone can sign up and host a public code repository for free,
    which makes GitHub especially popular with open-source projects.

    As a company, GitHub makes money by selling hosted private code repositories,
    as well as other business-focused plans that make it easier for organizations
    to manage team members and security. We utilize Github extensively at Kinsta to
    manage and develop internal projects.

Features of GitHub
==================
A few notable features of GitHub:

    * `Repositories <https://docs.github.com/en/repositories>`_: the core GitHub feature to host Git repositories
    * `Pull Requests <https://docs.github.com/en/pull-requests>`_: suggest changes to a project's code 
    * `Issues <https://docs.github.com/en/issues>`_: bug and task tracking for repositories
    * `Projects <https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects>`_: project management tools
    * `Actions <https://docs.github.com/en/actions>`_: automation and continuous integration
    * `Wikis <https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis>`_
    * `Pages <https://pages.github.com/>`_: websites hosted by GitHub

See https://github.com/features for all the features.

Using GitHub in Your Project
============================
There are many ways to make use of GitHub in your project, but here's one possible scenario.

Imagine that you have a piece of software which you're developing on your laptop, and you
want to keep track of changes, collaborate with other software developers, and ultimately
publish your code for the public to use.

Tracking Changes
----------------
Initialize a Git repository in your source code's directory with ``git init``. Then save a
snapshot of the current state with ``git commit``. Now, when you edit files, those changes
will be tracked; you can see the differences with ``git diff``. When you're satisfied with
the new version of your code, you can save another snapshot with ``git commit`` again.

Sharing Code
------------
Now you want to share your code from your laptop with someone else. You can set up a
repository on GitHub, then add it to your local source code's Git repository as a *remote*.
Then, you can ``git push`` your code to GitHub, where it will be available to share.

Collaborating
-------------
Collaborators can copy your code from GitHub to their own laptops with ``git clone``.
They can do this by first copying it to their own GitHub space, called *forking* it.
Then, after they make some changes and push those changes to their GitHub space, they
can make a *pull request* and suggest that you merge those changes into your repository.

Automatic Testing
-----------------
You can set up a *GitHub Action* to automatically run a suite of test scripts everytime
you push your code to GitHub, and it will report back if the tests pass or fail.

Publishing Code
---------------
You can package your code into a *release* and make it available to the public. Then, users
can open *issues* against your code if they find a bug or want to request a new feature.

More
----
This simplified scenario covers a basic use case, but it doesn't really explain how to do
all the things mentioned here; for that, check out the additional resources on the
:doc:`git-primer` and :doc:`github-primer` pages.