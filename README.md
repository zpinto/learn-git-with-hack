# learn-git-with-hack

## What is Git?

- Created by Linus Torvalds for the development of the Linux Kernel
- Git is a distributed version-control system for tracking changes in source code during software development.
- Allows many programmers to work on the same project at the same time without accidentally overriding someone else's changes

## Workshop Setup

### Git installation: https://git-scm.com/downloads

- Windows Users :(
- Mac/Linux
  - Yay! Git is already installed
  - If it is not, please navigate to the link above and follow the instructions for downloading git
- Create a GitHub account: https://github.com/join

### Set your git config

```
> git config --global user.name “Your name”
> git config --global user.email “youremail@somehting.com”
```

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
