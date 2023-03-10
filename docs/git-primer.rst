**********
Git Primer
**********

Installation
============
#. Install Git
#. Use a command line terminal
#. Make an SSH key
#. Add your SSH key to GitHub account

Windows
-------
#. Download and install from here: https://git-scm.com/download/win
#. Use the included Git Bash application as a command line interface to Git.
#. Make an ssh key as outlined here:

    * `GitHub's SSH Key Guide for Windows <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=windows>`_
    * Alternative tutorial: https://www.atlassian.com/git/tutorials/git-ssh

#. `Add SSH Key to GitHub Account Guide <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?tool=webui&platform=linux>`_

MacOS
-----
#. Use one of the methods outlined here to install Git: https://phoenixnap.com/kb/install-git-on-mac
#. Use the Terminal app to interface with Git.
#. Make an ssh key as outlined here:

    * `GitHub's SSH Key Guide for Mac <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=mac>`_
    * Alternative tutorial: https://www.atlassian.com/git/tutorials/git-ssh
#. `Add SSH Key to GitHub Account Guide <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?tool=webui&platform=linux>`_

Linux
-----
#. Install the ``git`` package with your distribution's package manager; for example on Ubuntu::

    sudo apt install git

#. Use any terminal app to interface with Git.
#. Make an ssh key as outlined here:

    * `GitHub's SSH Key Guide for Linux <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux>`_
    * Alternative tutorial: https://www.atlassian.com/git/tutorials/git-ssh
#. `Add SSH Key to GitHub Account Guide <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?tool=webui&platform=linux>`_

GitHub Desktop
--------------
On Windows and Mac, GitHub offers a graphical application called GitHub Desktop
as an alternative to the command line interface for Git.

See here: https://desktop.github.com/

Using Git
=========
Here we'll cover some of the basic commands from the command line.
See :any:`more-git` for more extensive tutorials.

git clone
-------------
Grab a copy of a repository from the URL provided.

.. code-block:: bash

    $ git clone git@github.com:Smithsonian/cfa-git-users.git
    Cloning into 'cfa-git-users'...
    remote: Enumerating objects: 90, done.
    remote: Counting objects: 100% (90/90), done.
    remote: Compressing objects: 100% (50/50), done.
    remote: Total 90 (delta 29), reused 78 (delta 22), pack-reused 0
    Receiving objects: 100% (90/90), 616.79 KiB | 8.12 MiB/s, done.
    Resolving deltas: 100% (29/29), done.
    $ ls .
    cfa-git-users

git status
----------
View the statius of the repository.

.. code-block:: bash
    $ git status
    On branch main
    Your branch is up to date with 'origin/main'.

    Changes not staged for commit:
    (use "git add/rm <file>..." to update what will be committed)
    (use "git restore <file>..." to discard changes in working directory)
    modified:   git-primer.rst
    deleted:    github.rst
    modified:   index.rst
    modified:   si-org.rst

    Untracked files:
    (use "git add <file>..." to include in what will be committed)
    git-github.rst

    no changes added to commit (use "git add" and/or "git commit -a")


``git commit``
--------------



``git pull``
------------

``git push``
------------

``git log``
-----------

``git status``
--------------

``git help``
------------
clone, commit, pull, push, log, status

.. _more-git:

More Git Resources
==================
* Git's homepage: https://git-scm.com/
* Software Carpentry class: https://swcarpentry.github.io/git-novice/

