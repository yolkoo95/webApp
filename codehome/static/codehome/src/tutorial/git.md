# Git - Time Machine

## Table of Contents
- [What is Git][1]
- [Why is Git][2]
	- [Branching and Merging][3]
	- [Small and Fast][4]
	- [Distributed][5]
	- [Staging Area][6]
	- [Free and Open Source][7]
- [Tutorial for Git][8]
	- [Overview][9]
	- [Initialization and Add][10]
	- [Time Travel][11]
		- [Go Back to Last Version][12]
		- [Management of Modification][13]
	- [Remote Repository][14]
		- [Prerequisites: SSH][15]
		- [Github][16]
	- [Branch Management][17]
		- [Create and Merge Branch][18]
		- [Solve Conflicts][19]
		- [Branch Management][20]
		- [Bug Branch][21]
		- [Teamwork with Git][22]
	- [Tag Management][23]
		- [Create Tag][24]
		- [Manipulation of Tag][25]
	- [Git Personal Setting][26]
		- [.gitignore File][27]
		- [Alias Setting][28]


## What is Git

Git can keep track of changes made to code, synchronize code between different people, test changes to code without losing the original, and revert back to old versions of code.

## Why is Git

### Branching and Merging

The Git feature that really makes it stand apart from nearly every other SCM out there is its branching model.

Git allows and encourages you to have multiple local branches that can be entirely independent of each other. The creation, merging, and deletion of those lines of development takes seconds.

![branches](codehome/src/img/tutorial/branches.png)

### Small and Fast

Git is fast. With Git, nearly all operations are performed locally, giving it a huge speed advantage on centralized systems that constantly have to communicate with a server somewhere.

Git was built to work on the Linux kernel, meaning that it has had to effectively handle large repositories from day one. Git is written in C, reducing the overhead of runtimes associated with higher-level languages. Speed and performance has been a primary design goal of the Git from the start.

### Distributed

One of the nicest features of any Distributed SCM, Git included, is that it's distributed. This means that instead of doing a "checkout" of the current tip of the source code, you do a "clone" of the entire repository.

### Staging Area

Unlike the other systems, Git has something called the "staging area" or "index". This is an intermediate area where commits can be formatted and reviewed before completing the commit.

One thing that sets Git apart from other tools is that it's possible to quickly stage some of your files and commit them without committing all of the other modified files in your working directory or having to list them on the command line during the commit.

![index1](codehome/src/img/tutorial/index1.png)

This allows you to stage only portions of a modified file. Gone are the days of making two logically unrelated modifications to a file before you realized that you forgot to commit one of them. Now you can just stage the change you need for the current commit and stage the other change for the next commit. This feature scales up to as many different changes to your file as needed.

Of course, Git also makes it easy to ignore this feature if you don't want that kind of control — just add a '-a' to your commit command in order to add all changes to all files to the staging area.

![index1](codehome/src/img/tutorial/index2.png)

### Free and Open Source

Git is released under the GNU General Public License version 2.0, which is an open source license. The Git project chose to use GPLv2 to guarantee your freedom to share and change free software---to make sure the software is free for all its users.

## Tutorial for Git

### Overview

If you're newer to git, ignore this part and start from [next part](#initialization-and-add), 'cause this is just a summary of common commands, and you will master them after learning knowledge of git.

Git commands:

- `git clone <url>` : take a repository stored on a server (like GitHub) and downloads it
- `git add <filename(s)>` : add files to the staging area to be included in the next commit
- `git commit -m "message"` : take a snapshot of the repository and save it with a message about the changes
- `git commit -am <filename(s)>` "message" : add files and commit changes all in one
- `git status` : print what is currently going on with the repository
- `git push` : push any local changes (commits) to a remote server
git pull : pull any remote changes from a remote server to a local computer
- `git log` : print a history of all the commits that have been made
- `git reflog` : print a list of all the different references to commits
git reset --hard <commit> : reset the repository to a given commit
git reset --hard origin/master : reset the repository to its original state (e.g. the version cloned from GitHub)

When combining different versions of code, e.g. using `git pull`, a merge conflict can occur if the different versions have different data in the same location. Git will try to take care of merging automatically, but if two users edit, for example, the same line, a merge conflict will have to be manually resolved.

- To resolve a merge conflict, simply locally remove all lines and code that are not wanted and push the results.

### Initialization and Add

Before initiate a git workspace, we have to make a directory for it, a blank directory is preferred.

```sh
$ mkdir workspace
$ cd workspace
$ pwd
/Users/unicorn/workspace
```

Then, we can initialize `workspace` into a git workspace,

```sh
$ git init
Initialized empty Git repository in /Users/unicorn/workspace/.git/
```

Now let's add a file into git workspace, but first let's create a file and modify it,

```sh
$ touch README.md
$ echo "Hello git" > README.md
```

Then we add `README.md` to staging area,

```sh
$ git add README.md
```

if we make sure that we have finished our work, then we can commit our change to git repository as follows,

```sh
$ git commit -m 'Modified README.md'
```

BTW, `git status` allows us to checkout the status of working space and staging area, 

```sh
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

and `git diff` could be used to compare file that you have changed with the old version. 

```sh
$ git diff README.md
diff --git a/README.md b/README.md
index 46d49bf..9247db6 100644
--- a/README.md
+++ b/README.md
@@ -1,1 +1,1 @@
+Hello git
```

### Time Travel

#### Go Back to Last Version

Let's changed the content of `README.md` and commit changes we have made,

```sh
$ echo 'Git is a distributed version control system.' >> README.md
$ git add .
$ git commit -m 'Added a new line to README.md'
[master 1094adb] Added a new line to README.md
 1 file changed, 1 insertion(+), 0 deletion(-)
```

- Notice that `.` in `git add .` means all the files that have been changed. 

Then we can use `git log` to refer to the commit we have made,

```sh
$ git log
commit 1094adb7b9b3807259d8cb349e7df1d4d6477073 (HEAD -> master)
Author: Unicorn <brysjhhrhl95@163.com>
Date:   Fri May 18 19:06:15 2018 +0800

    Added a new line to README.md

commit e475afc93c209a690c39c13a46716e8fa000c366
Author: Unicorn <brysjhhrhl95@163.com>
Date:   Fri May 18 19:03:36 2018 +0800

    Modified README.md
```

We can see that we have made 2 commits, and `HEAD` now points to the latest version(commit 1094adb). However, the result of `git log` is annoying particularly with so many information. We could add parameter `--pretty=oneline` to the command.

```sh
$ git log --pretty=oneline
1094adb7b9b3807259d8cb349e7df1d4d6477073 (HEAD -> master) Added a new line to README.md
e475afc93c209a690c39c13a46716e8fa000c366 add distributed Modified README.md
```

Ha, this time is better. You might wanna ask 'Why the commit id is such a long string consisting of numbers and characters?', the short answer is avoiding conflicts. Image if everyone uses 1, 2 or 3 as commit id, it will make conflicts. So a random string ensure a kind of uniqueness to the great extent.

Now we are going to go back to the first version of `README.md`, just type in command `git reset --hard commit_id`,

```sh
$ git reset --hard e475a

# or for latest version
$ git reset --hard HEAD^
```

Then let's review the status of our repository,

```sh
$ git log
commit e475afc93c209a690c39c13a46716e8fa000c366 (HEAD -> master)
Author: Unicorn <brysjhhrhl95@163.com>
Date:   Fri May 18 19:03:36 2018 +0800

    Modified README.md
```

Commit with # of `1094a` disappeared. If we want to go back to `commit[id:1094a]`, same as what we have done,`git reset --hard 1094a`. 

However, the problem is that people may forget the id of those commits ahead of current commit. Don't worry, using `git reflog`, we can track the travel path.

```sh
$ git reflog
e475afc HEAD@{1}: reset: moving to HEAD^
1094adb (HEAD -> master) HEAD@{2}: commit: Added a new line to README.md
e475afc HEAD@{2}: commit (initial): Modified README.md
```

#### Management of Modification

##### Undo Modification

After finished project, if we want to undo our modification to some files, what should we do? It is easy with command of Git, `git checkout -- file` , but we need to consider two scenarios.

###### Files in Working Space

If the file where we want to undo the changes we did is in working space, i.e. the file has not been added to staging area. Then, the result of `git checkout -- file` will undo all the change you made in the file.

If the file is in staging area, and we make changes again after adding it into staging area. Then, the command `git checkout -- file` will undo the changes we made **after** adding the file into staging area.

###### Files in Staging Area

Then it's natural to ask 'How to undo the changes of the files in staging area'. The answer is `git reset HEAD <file>`. `git reset` is able to not only go back to any version in the repository, but undo the changes of file in staging area, and put the file back into working space.

##### Removal of Files

If we use `rm <file>`, we only remove the file in working space.

If we make sure that the file, README.md for example, is no more useful and wanna remove it from repository, using command `git rm <file>` to remove the `<file>` from repository.

### Remote Repository

#### Prerequisites: SSH

For local repo connects remote repo by ssh encrypted transmission, we'd better create ssh key locally. 

Checkout if `.ssh` directory exists in home directory. If not, run command as follows, (if yes, ignore this)

```sh
$ ssh-keygen -t rsa -C "youremail@example.com"
```

Then we created `.ssh` directory in home directory, which includes `id_rsa` and `id_rsa.pub`. `id_rsa` is private key, which is top secret for you, and `id-rsa.pub` is public key, which we will use later.

#### Github

GitHub is a website that stores Git repositories on the internet to facilitate the collaboration that Git allows for. A repository is simply a place to keep track of code and all the changes to code.

Create a Github account and login in, then add your public key in SSH Key setting, which is in Setting of Github account.

##### Add a New Remote Repo

Login your account and click 'Create a new repo' button in the upper right corner, and type in related information (e.g. repo name).

After creating it, connect local repo to it with command,

```sh
$ git remote add origin git@github.com:yolkoo95/markdown.git
```

- `origin` is the name of remote repo of Github by default.

Then we can push files of local repo to remote repo,

```sh
# -u is must when first push
$ git push -u origin master
Counting objects: 20, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (15/15), done.
Writing objects: 100% (20/20), 1.64 KiB | 560.00 KiB/s, done.
Total 20 (delta 5), reused 0 (delta 0)
remote: Resolving deltas: 100% (5/5), done.
To github.com:yolkoo95/markdown.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

After pushing, we could see the same contents in remote repo.

- Warning: if new repo you made have README.md or other files (a conflict will produce), please clone them from remote repo into local repo, and then push local contents to remote repo.
- When push or clone for the first time, a warning would generate, enter `yes` is okay.

```sh
The authenticity of host 'github.com (xx.xx.xx.xx)' can't be established.
RSA key fingerprint is xx.xx.xx.xx.xx.
Are you sure you want to continue connecting (yes/no)?
```

##### Clone from Remote Repo

Clone repo from Github is easy with git, using `git clone` as follows,

```sh
$ git clone 'git@github.com:yolkoo95/webApp.git'
```

### Branch Management

Git allows and encourages you to have multiple local branches that can be entirely independent of each other. The creation, merging, and deletion of those lines of development takes seconds.

#### Create and Merge Branch

In the section of [Time Travel](#time-travel), we know that Git treats different versions of project as a time baseline, where we can jump among them. So far, there is only one baseline - i.e. `master` branch. and `HEAD` refers to current branch.

At the beginning, `master` branch is a baseline, Git points to latest commit with `master pointer`, and points to `master` with `HEAD`, whereby it can locate current branch and commit timestamp.

![branch1](codehome/src/img/tutorial/branch1.png)

Every time the project is committed, `master` will move one step forward along `master` branch. So it becomes longer as the project is committed.

When we create a new branch, `dev` for example, Git creates a new pointer called 'dev', pointing to the same timestamp as `master`, and makes `Head` point to `dev`, meaning that we are on `dev` branch.

![branch2](codehome/src/img/tutorial/branch2.png)

- this explains why Git is so fast (pointer explains everything)

Yet, since now, everything we are going to do will be on `dev` branch. For example, if we commit a new change, `dev pointer` will move one step forward but `master pointer` stays in place.

![branch3](codehome/src/img/tutorial/branch3.png)

Suppose that we have finished changes on `dev` branch, how to merge `master` with `dev`? The simplest way is to let `master` point to where `dev` points.

![branch4](codehome/src/img/tutorial/branch4.png)

After merging, `dev` branch will be deleted and there only `master` branch exists.

![branch5](codehome/src/img/tutorial/branch5.png)

That's AWESOME!

Let's practice with Git.

Create `dev` branch,

```sh
$ git checkout -b dev
Switched to a new branch 'dev'
```

`git checkout` with `-b` parameter means create and switch to a new branch, which is equal to following commands,

```sh
$ git branch dev
$ git checkout dev
Switched to branch 'dev'
```

Then, checkout current branch,

```sh
$ git branch
* dev
  master
```

- `*` indicates current branch.

Image that we have made some changes and have committed changes. Now let's merge `master` branch with `dev` branch,

```sh
# switch to master branch
$ git checkout master
Switched to branch 'master'

# merge dev branch
$ git merge dev
Updating d46f35e..b17d20e
Fast-forward
 README.md | 1 +
 1 file changed, 1 insertion(+)
```

- `Fast-forward` is a kind of merging method, which we will remove merged branch and get rid of the log of that branch.

After merging, delete `dev` branch,

```sh
$ git branch -d dev
Deleted branch dev (was b17d20e).
```

#### Solve Conflicts

Image a scenario that someone commit different changes on `master` branch and `dev` branch respectively. If then we try to merge two branches, a conflict will emerge.

![conflict](codehome/src/img/tutorial/conflict.png)

```sh
$ git merge dev
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

Then we must solve conflict manually. Find the files that cause conflicts, and modify them.

```sh
# find the files that cause conflicts: README.md
$ git status
On branch master
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)

	both modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

# solve conflicts
$ vi README.md

Git is a distributed control system.
<<<<<< HEAD
Hello world
======
Hello git
>>>>>> dev 
```

Git marks contents that cause conflict with `<<<<<<` and `>>>>>>`. Delete what we don't want and save the file. After fixed bugs, commit the changes.

```sh
git commit -m "conflict fixed"
```

Then we are able to merge successfully.

#### Branch Management

Often when we working in a team, we are working on our own branch. After finishing the project, we will merge our branch to `master` branch. If use `fast forward` mode, our branch will be removed, which is not what we expect. So `--no-ff` is a more common way to merge branch.

with `--no-ff` parameter, our repository will works like this,

![no-ff](codehome/src/img/tutorial/no-ff.png)

#### Bug Branch

During programing, bug is everywhere and so we need to fix bugs from time to time. In general, we will create a new bug branch, fix bugs, and finally merge it into main master. 

Image a scenario that when developing a project on `dev` branch, we are assigned a emergent bug-fixed task. However, the current project is on half way. What should we do?

```sh
$ git status
On branch dev
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   hello.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md
```

Git have a fancy feature called `stash`, which will save current workspace waiting to be used later. 

```sh
$ git stash
Saved working directory and index state WIP on dev: f52c633 add merge
```

Now, we are able to create a new branch and fix bugs safely.

Suppose, the bug to be fixed is on `master` branch, then we will create `bug` branch from `master` branch.

```sh
$ git checkout master
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 6 commits.
  (use "git push" to publish your local commits)

$ git checkout -b issue-101
Switched to a new branch 'issue-101'
```

After fixing bugs, switch to `master` branch, merge `bug` branch, and delete it.

```sh
$ git switch master
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 6 commits.
  (use "git push" to publish your local commits)

$ git merge --no-ff -m "merged bug fix 101" issue-101
Merge made by the 'recursive' strategy.
 README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Now, we can continue our work on `dev` branch.

```sh
$ git switch dev
Switched to branch 'dev'

$ git status
On branch dev
nothing to commit, working tree clean
```

Workspace is clean, get our work back. Using `git stash list` to list all stash,

```sh
$ git stash list
stash@{0}: WIP on dev: f52c633 add merge
```

There are two ways to recover our works,

- `git stash apply`: the cache in stash will not be deleted.
- `git stash pop`: the cache will be deleted.

Using `git stash pop` for example,

```sh
$ git stash pop
On branch dev
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   hello.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

Dropped refs/stash@{0} (5d677e2ee266f39ea296182fb2354265b91b3b2a)
```

Fantastic!

One more question, if the same bug exist on `dev` branch, what should we do?

The answer is that we can apply commit[issue-101] we have made in `bug` branch to `dev` branch with `cherry-pick`.

```sh
$ git branch
* dev
  master

$ git cherry-pick 4c805e2
[master 1d4b803] fix bug 101
 1 file changed, 1 insertion(+), 1 deletion(-)
```

`git cherry-pick` allows us to apply the same modification, fix bugs for example, to different branches.

- Notice: current commit id is `1d4b8`, the commit id of bug fix for `master` branch is `4c805`. Although the modifications are same, they are two different commits indeed.

#### Teamwork with Git

When cloning from remote repo, we actually make a link between local repo and remote repo, and the default name of remote (Github) repo is `origin`.

We can look over the info of remote repo with `git remote`,

```sh
$ git remote
origin
```

or `git remote -v` for more detailed information,

```sh
$ git remote -v
origin  git@github.com:yolkoo95/webapp.git (fetch)
origin  git@github.com:yolkoo95/webapp.git (push)
```

##### Push Branch

If we want to push local branch to remote repo, use `git push origin <branch-name>`

```sh
$ git push origin dev
```

##### Fetch Branch

When working in a team, programmers will push commits to `master` or `dev` branch. 

By default, when cloning a project from remote repo, we are able to get `master` branch. However, it must be troublesome if we have to develop on `dev` branch of the project. So we have to clone remote `dev` branch as follows,

```sh
$ git checkout -b dev origin/dev
```

Now, we can work on `dev` branch, and push local `dev` to remote `dev` branch.

To sum up, the working mode of multi-person collaboration is usually like this:

1. Try to push commit by `git push origin <branch-name>`.
2. If failed, it is entirely possible that remote branch is ahead of local branch by **n** commits. We should try to merge remote branch to local one with `git pull`.
3. If there is a conflict when we try to merge remote branch with local one, then [fix conflict](#solve-conflicts) and commit changes.
4. After fixing conflict, try to push commit as step 1.

- if `git pull` generates a warning that `no tracking information`, which means that the link between remote repo and local repo does not exist. Link them with `git branch --set-upstream-to <branch-name> origin/<branch-name>`

### Tag Management

The aim of tag is to help developer index different version of project easily, instead of annoying commit number.

#### Create Tag

It's easy to create a tag, first switch to a branch that needs to be tagged.

```sh
$ git branch
* dev
  master

$ git checkout master
Switched to branch 'master'
```

then use `git tag <name>` to tag,

```sh
$ git tag v1.0
```

use `git tag` to list all tags,

```sh
$ git tag
v1.0
```

By default, tag will applied on latest commit. If we want to tag on other commit, use `git tag <name> <commit-id>`

Also, if we want to add some description on tag, use command `git tag -a <name> -m 'Hello Git' <commit-id>`, and use `git show <tag-name>` to query related information.

```sh
$ git show v1.0
tag v1.0
Tagger: Unicorn <brysjhhrhl95@163.com>
Date:   Fri May 18 12:48:43 2018 +0800

version 1.0 released

commit 1094adb7b9b3807259d8cb349e7df1d4d6477073 (tag: v1.0)
Author: Unicorn <brysjhhrhl95@163.com>
Date:   Fri May 17 11:44:23 2018 +0800

    Added a newline
...
```

#### Manipulation of Tag

- `git push origin <tag-name>`: push a commit by tag.
- `git push origin --tags`: push all tags that have not been pushed earlier.
- `git tag -d <tag-name>`: delete a local tag.
- `git push origin :refs/tags/<tag-name>`: delete a remote tag.

### Git Personal Setting

#### .gitignore File

If we don't want to commit some of files, such as configuration files, we could create a `.gitignore` file and write all files that we don't want to commit into `.gitignore` file.

[Github](https://github.com/github/gitignore) provide different kinds of `.gitignore` files for developer.

For example, there will be some by-product files when run a python file, like `.pyc`, `.pyo`, `dist` etc.

```sh
# Python:
*.py[cod]
*.so
*.egg
*.egg-info
dist
build
```

Finish our own `.gitignore` file and commit it.

#### Alias Setting

We can set alias of Git command in a way same as setting linux environment variables.

There are two ways:

1. With command line, `git config --global alias.<name> <command-name>`, for example `git config --global alias.co checkout`. BTW, amazingly some people will set alias of `log` to `git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"`

2. Setting alias by modifying config file. In user's home directory, there is a hidden file `.gitconfig`. Customize your own `[alias]` section.

```sh
$ cat .gitconfig
[alias]
    co = checkout
    ci = commit
    br = branch
    st = status
[user]
    name = Your Name
    email = your@email.com
```

Hope Git will make your life efficient []~(￣▽￣)~*

A good git reference: [GIT CHEAT SHEET](codehome/src/pdf/git-cheatsheet.pdf)

<EndMarkdown>
[1]: #what-is-git
[2]: #why-is-git
[3]: #branching-and-merging
[4]: #small-and-fast
[5]: #distributed
[6]: #staging-area
[7]: #free-and-open-source
[8]: #tutorial-for-git
[9]: #overview
[10]: #initialization-and-add
[11]: #time-travel
[12]: #go-back-to-last-version
[13]: #management-of-modification
[14]: #remote-repository
[15]: #prerequisites:-ssh
[16]: #github
[17]: #branch-management
[18]: #create-and-merge-branch
[19]: #solve-conflicts
[20]: #branch-management
[21]: #bug-branch
[22]: #teamwork-with-git
[23]: #tag-management
[24]: #create-tag
[25]: #manipulation-of-tag
[26]: #git-personal-setting
[27]: #.gitignore-file
[28]: #alias-setting