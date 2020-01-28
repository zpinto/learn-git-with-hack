# learn-git-with-hack

## Overview

This repo provides a description of several common git commands. It also includes a tutorial that will offer you the opportunity to put your git skills to the test.

Check out the Table of Contents below to simply look for descriptions and explanations of git commands or dive into a quick tutorial to make sure you really know how to use git.

## Table of Contents

- [What is Git?](#what-is-git-?)
- [Setting Git Up](#setting-git-up)
- [Git Principles](#git-principles)
- [Git Commands](#git-commands)
- [Tutorial](#tutorial)

## What is Git?

- Created by Linus Torvalds for the development of the Linux Kernel
- Git is a distributed version-control system for tracking changes in source code during software development.
- Allows many programmers to work on the same project at the same time without accidentally overriding the changes of someone else

## Setting Git Up

### Git installation: https://git-scm.com/downloads

- Windows Users :(
- Mac/Linux
  - Yay! Git is already installed
  - If it is not, please navigate to the link above and follow the instructions for downloading git
- Create a GitHub account: https://github.com/join

### Set your git config

- Go to your terminal(git bash for windows) and set up your git config
  - This is important, because all the commits you make will be tied to these configurations.
  - This is how Github can keep track of your contributions to a project.

```
> git config --global user.name “Your name”
> git config --global user.email “youremail@somehting.com”
```

## Git Principles

- [Repository](#repository)
- [Remote](#remote)
- [Branching](#branching)
- [Merging](#merging)
- [Merge Conflicts](#merge-conflicts)
- [The 3 Git States](#the-3-git-states)

### Repository

A repository is the directory in which git is tracking the changes for the project. The repository holds a .git directory that holds all of the data that git uses to keep track of changes and other information about the particular project. A repository can be local and(or) remote.

### Remote

Remote is the location of a repository that is not on the machine of the programmer. An example of a remote location is github.com. Having a remote location for a project allows multiple programmers to push new code to the same project and pull the changes made by their fellow programmers.

### Branching

A branch diverges from another branch(typically master) and allows programmers to add features without making changes to the master or branch that was branched from. The new branch works off of the last commit of the branch branched from. The programmer can then work on features and add commits to their branch. Using branches allows all programmers on the project to work on a separate features on separate branches all without making changes directly to the master or production branch.

### Merging

Once a programmer finishes building a feature on a branch, they need to add this new code to the production branch. To do this, they can merge the branch of their new feature to the production branch. This will apply all of the changes from the branch onto the master branch or any other selected branch.

### Merge Conflicts

When merging, there is a chance that another programmer has made changes to some lines of code following the branch operation of someone else that made changes to the same lines on their branch. Because the brancher's branch does not know about these changes, there is a conflict on these lines when the brancher tries to merge. This will need to be resolved by the programmer merging by selecting the lines that they actually want to keep and continuing the merge.

### The 3 Git States:

#### Modified

This is the state that contains all of the files that have been modified since the last commit. This may include new files that are not yet being tracked by git or files that are being tracked and have some kind of changes. To commit these changes, they first need to be added to the staging area using the git add command.

#### Staging

This is the state that determines all of the changes that will be included in the next commit. This is essentially like packing a box of desired contents before you ship it. When you are ready to ship the box, you use the command git commit.

#### Committed

Committed files are a grouping of changes applied and associated with a message that explains the intent of the changes. You can think of a commit as a building block. Each commit gets stacked on top of all of the previous commits to build the current version of the project. These commits can be used to revert to old versions and look back to changes made in the past.

## Git Commands

### git clone

- Clone will go to the URL provided and copy the git repository located at this link
- The link typically refers to a Github repository

```
> git clone <repo_url>
```

### git init

- Init will initialize a new git repository by creating a .git directory that will be used for holding all the git related information about the project you are working on
- This command is typically used at the start of the project

```
> git init
```

### git status

- Status gives you information about what files are tracked and un-tracked
- Also lists which of the [3 states](#the-3-git-stages) your changed files are in

```
> git status
```

### git add

- Add will move files from the [modified state](#modified) to the [staging state](#staging)

- You can add all files in the current directory and subdirectories to the staging state by executing the following command

```
> git add .
```

- You can add just one file to the staging state by executing the following command

```
> git add <path_to_file>
```

### git commit

- Commit will move files from the [staging state](#staging) to the [committed state](#committed)
- Remember to associate a message with your commit so that you and your fellow programmers know the purpose of the commit's changes

```
> git commit -m "<message_explaining_changes>"
```

### git remote add

- Remote is the location of your non-local repository
- Click [here](#remote) to read about what remote is in the [git principles](#git-principles) section
- Remote add is the command that allows you to tell git where you want your repository to live not on your computer
- You would do this so that you could work on the same project with multiple people

- To add a remote location, execute the following command
  - When adding a remote location, we create a name for it (kinda like a variable name for the url)
  - The convention is to call our main remote location "origin"

```
> git remote add origin <url_of_remote_repo>
```

### git pull

- Pull will get all of the changes made to the current branch of the remote repository and add them to your local repository
- These changes may have been made by your fellow team members

```
> git pull
```

### git push

- Push will push all of the local changes that you have committed to a [branch](#branching) to the remote branch of the repository
- You would do this so that you could share the changes you made with your team members

```
> git push
```

- Note: When pushing to your remote branch for the first time, you will have to execute
  - The -u stands for upstream
  - "origin" is the upstream location that is associated with the remote location of the repository

```
> git push -u origin <branch_name>
```

### git branch

- Branch will create a new branch with the given name
- Click [here](#branching) to read about what branching is in the [git principles](#git-principles) section

```
> git branch <new_branch_name>
```

### git checkout

- Checkout will switch you to the given branch
- You will now be able to make changes and commits to the switched to branch

```
> git checkout <branch_name>
```

### git merge

- Merge will allow you to apply the commits on the selected branch to the current branch
- Click [here](#merging) to read about what merging is in the [git principles](#git-principles) section

```
> git merge <branch_to_merge>
```

### git log

- Log will show a lits of all of the commits made to the current branch in chronological order
  - You can continue pressing the enter key to continue down the list
  - You can press the q key to exit

```
git log
```

## Tutorial

### Clone this repo

```

> git clone https://github.com/zpinto/learn-git-with-hack.git

```

### Make your own repo

- Rename the directory and remove the .git directory inside your new project

```

> mv learn-git-with-hack <learn-git-yourname>
> cd <learn-git-yourname>
> rm -rf .git

```

- Initialize your new git repository

```

> git init

```

## Important Commands

### Status

- Gives you information about what files are staged and which ones are not

```

> git status

```

### Staging

- You must stage your files in order to commit and save changes

```

> git add <file_name>

```

### Committing

- Adds the latest changes that are staged to the source code
- Allows you to save a snapshot of the changes that you made

```

> git commit -m “my commit message”

```

### Setting Remote Origin

- Make a GitHub repo with you GitHub account
- Set your local repositories remote origin

#### Sets your repos remote origin

```

> git remote add origin <url-of-your-repo>

```

#### Pushes your commits from local master to remote master

```

> git push -u origin master

```

### Pushing

- Pushes code to the remote repository

```

git push

```

### Pulling

- Pulls any new changes from your repository

```

git pull

```

### Branching

#### Creating a branch

- Creates a new branch based off of the latest commit of the branch that you are branching from

```

git branch <my_branch_name>

```

#### Checking out that branch

- Switches you to the branch that you select

```

git checkout <my_branch_name>

```

### Merging

- Merges the selected branch onto the one that you are currently on

```

git merge <my_branch_name>

```

### Logs

- Log of all of the commits, merges, etc.

```

git log

```

## Additional Material

- [Git Cheat Sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)

- [Becoming a Git Pro](https://itnext.io/become-a-git-pro-in-just-one-blog-a-thorough-guide-to-git-architecture-and-command-line-interface-93fbe9bdb395)

- [A Simple Git Guide](https://rogerdudler.github.io/git-guide/)

```

```
