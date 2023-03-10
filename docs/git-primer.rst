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
Grab a copy of a repository from the URL provided. ::

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
View the statius of the repository. ::

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

git add
-------
Stage a file to be comitted. ::

    $ git add git-github.rst
    $ git status
    On branch main
    Your branch is up to date with 'origin/main'.

    Changes to be committed:
    (use "git restore --staged <file>..." to unstage)
    new file:   git-github.rst

    Changes not staged for commit:
    (use "git add/rm <file>..." to update what will be committed)
    (use "git restore <file>..." to discard changes in working directory)
    modified:   git-primer.rst
    deleted:    github.rst
    modified:   index.rst
    modified:   si-org.rst

git commit
----------
Commit a snapshot of the files. ::

    $ git commit -m "update docs"
    [main 5fd9f1e] update docs
    4 files changed, 116 insertions(+), 8 deletions(-)
    rename docs/{github.rst => git-github.rst} (100%)

git pull
--------
Update your local directory with the contents from the remote repository. :::

    $ git pull
    Already up to date.

git push
--------
Send your local changes to the remote repository. ::

    $ git push
    Enumerating objects: 11, done.
    Counting objects: 100% (11/11), done.
    Delta compression using up to 16 threads
    Compressing objects: 100% (6/6), done.
    Writing objects: 100% (6/6), 2.08 KiB | 1.04 MiB/s, done.
    Total 6 (delta 4), reused 0 (delta 0), pack-reused 0
    remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
    To github.com:Smithsonian/cfa-git-users.git
    b57a6fc..5fd9f1e  main -> main


git log
-------
Show a log of the previous commits. ::

    $ git log --oneline
    5fd9f1e (HEAD -> main, origin/main, origin/HEAD) update docs
    b57a6fc add note on front page
    f79ecfe more updates
    7097b47 add a couple images
    ead1c28 don't use cache
    43096ed update requirements
    6083458 update docs
    baaeda2 use furo theme, update si-org page
    6a8adb7 add .gitkeep files
    bea5821 Update README.md
    3ec6262 flatter dir structure
    61f11c8 some structure and github deploy action
    6fc244b skeleton of documentation
    d9d9889 Initial commit

git help
--------
Show help for a command. ::

    $ git help

.. _more-git:

More Git Resources
==================
* Git's homepage: https://git-scm.com/
* Software Carpentry class: https://swcarpentry.github.io/git-novice/

