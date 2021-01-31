# learn-git-with-hack

## Virtual Workshop Recording

[Youtube](https://youtu.be/97rg_UDGkFE) | [Slides](https://docs.google.com/presentation/d/1Sp5AcPmvgugNbaegud_o0Wa9Q4BktUFj2zaG46Pj9W8/edit?usp=sharing)

## Overview

This repo provides a description of several common git commands. It also includes a tutorial that will offer you the opportunity to put your git skills to the test.

Check out the Table of Contents below to simply look for descriptions and explanations of git commands or dive into a quick tutorial to make sure you really know how to use git.

## Table of Contents

- [What is Git?](#what-is-git-?)
- [Setting Git Up](#setting-git-up)
- [Git Principles](#git-principles)
- [Git Commands](#git-commands)
- [Tutorial](#tutorial)
- [Additional Material](#additional-material)

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
> git config --global user.email “youremail@something.com”
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

- [git clone](#git-clone)
- [git init](#git-init)
- [git status](#git-status)
- [git add](#git-add)
- [git commit](#git-commit)
- [git remote add](#git-remote-add)
- [git pull](#git-pull)
- [git push](#git-push)
- [git branch](#git-branch)
- [git checkout](#git-checkout)
- [git merge](#git-merge)
- [git log](#git-log)

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

### Overview

In this tutorial, we are going to:

- Initialize a git repository
- Setup a remote repository on Github
- Create and work on a branch
- Merge that branch to master
- And push to Github

### Steps

- [Setup](#setup)
- [Clone the repo](#step-1-clone-the-repo)
- [Remove the .git directory](#step-2-remove-the-git-directory)
- [Initialize your git repository](#step-3-initialize-your-git-repository)
- [Add and commit the current files in the project](#step-4-add-and-commit-the-current-files-in-the-project)
- [Setting up a remote Github repository](#step-5-setting-up-a-remote-github-repository)
- [Creating and checking out to a branch](#step-6-creating-and-checking-out-to-a-branch)
- [Making commits on that branch](#step-7-making-commits-on-that-branch)
- [Merging that branch and pushing to remote](#step-8-merging-that-branch-and-pushing-to-remote)
- [You did it!!!](#you-did-it)

### Setup

If you have not already, please follow the instructions [here](#setting-git-up)!

### Step 1: Clone the repo

- We are going to clone this repo, so that we can copy all of the code in this Github repository
  - Make sure that change into a directory where you want to keep these files

```
> git clone https://github.com/zpinto/learn-git-with-hack.git
```

<img src='http://g.recordit.co/TKYLmwZlul.gif' title='Clone Repo' width='' alt='Clone Repo' />

### Step 2: Remove the .git directory

- We are going remove the .git directory from inside the repo, so we can go through the motions of initializing this project to be a git repository (pretending that you wrote all this code from scratch)

  - The .git directory holds all the data about all of the commits that I made and the remote location of my Github repository
  - We want this to be your repository, so execute the commands below

- If you have not yet, change into the cloned directory

```
> cd learn-git-with-hack
```

- Remove the .git directory with the following command

```
> rm -rf .git
```

<img src='http://g.recordit.co/qK1ZoKvri6.gif' title='Remove .git' width='' alt='Remove .git' />

### Step 3: Initialize your git repository

- We are now going to initialize a new git repository, as if we were just starting our project
  - Make sure that you are in the project directory

```
> git init
```

- Now we have a clean git repository that is ready to track our changes

<img src='http://g.recordit.co/DMmge4PWgu.gif' title='Initialize git' width='' alt='Initialize git' />

### Step 4: Add and commit the current files in the project

- Because we created a new git repository, none of the files are being tracked yet
  - We can check the status to verify this

```
> git status
```

- Let's add the files, moving them from the [modified state](#modified) to the [staging state](#staging)

```
> git add .
```

- Now that we have added the files, they are in the staging state
- Let's move our files from the staging state to the [committed state](#committed)

```
> git commit -m "initial commit"
```

- Yay! We committed our first changes

<img src='http://g.recordit.co/mPlH2UrMO9.gif' title='Add and commit' width='' alt='Initialize git' />

### Step 5: Setting up a remote Github repository

- We want to make our code available in a remote repository on Github
- Let's create a Github repo for our remote location

<img src='http://g.recordit.co/APqzFouYUX.gif' title='Create Github repo' width='' alt='Create Github repo' />

- Now we need to set the remote location in our git repository and push it to Github

```
> git remote add origin <github_repo_url>
> git push -u origin master
```

- Yay! Our code is on Github

<img src='http://g.recordit.co/H3ZDn1fzRo.gif' title='Push to remote' width='' alt='Push to remote' />

### Step 6: Creating and checking out to a branch

- Now that we have our remote repository set up, we want to add a feature to our project
- The feature we are going to add is the solution to problem 1

- We want to create a new [branch](#branching) so that we can add this feature without interfering with any other changes that our potential team members may be [merging](#merging) to the master branch(typically the production branch)
  - It is bad practice to work on the master branch, so it is important to create a new branch when working on a feature
  - Remember that we want to create a branch based off of master, so we need to be on the master branch when we create the branch

```
> git branch <new_branch_name>
```

- Now let's checkout to that branch and start working

```
> git checkout <created_branch's_name>
```

- Now that we are on the new feature's branch, let's change into the problems directory so we can work on the solution

```
> cd problems
> cd problem 1
```

- Open question1.txt file and read the question
- Code your solution in the file named answer1.py
  - You can do this part yourself!
- Run tester1.py to check your answer

```
python tester1.py
```

<img src='http://g.recordit.co/Cj1dHs5OuA.gif' title='Answer the question' width='' alt='Answer the question' />

### Step 7: Making commits on that branch

- Now that you have made changes to the answer1.py file, we need to add and commit those changes to the branch

```
> git add .
> git commit -m "solve problem1"
```

- Yay! We committed the solution to our feature's branch

<img src='http://g.recordit.co/hMC2s2ShM4.gif' title='Commit feature' width='' alt='Commit feature' />

### Step 8: Merging that branch and pushing to remote

- Now that we have a working feature on our branch, it is time to [merge](#merging) it to the master branch where all of our production code is

- We need to checkout to the master branch and merge our feature's branch
- Note: Always remember to pull before making any changes to master! On of your team members may have made changes since the last time you pulled

```
> git checkout master
> git pull
> git merge <created_branch's_name>
```

- Yay! Now our changes on the feature's branch have been applied to master
- Now let's push it to our remote repository on Github so our potential team members can see the changes as well

```
> git push
```

- Yay! It is on Github!
- To make sure that you have the flow mastered, I would recommend repeating these steps with problem2 as well.

<img src='http://g.recordit.co/s1W77KYW1X.gif' title='Merge and push' width='' alt='Merge and push' />

### You did it!!!

There is much more to learn about git, but you should now have a better understanding of some of the most popular and useful aspects of git.

Now you can use git in your projects to collaborate and keep track of your projects progression.

## Additional Material

- [Git Cheat Sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)

- [Becoming a Git Pro](https://itnext.io/become-a-git-pro-in-just-one-blog-a-thorough-guide-to-git-architecture-and-command-line-interface-93fbe9bdb395)

- [A Simple Git Guide](https://rogerdudler.github.io/git-guide/)
