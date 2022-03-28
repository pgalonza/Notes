# Git

Edit _.gitconfig_

```bash
git config --global --edit
git config --global user.name
git config --global user.email
```

Interactively choose hunks of patch between the index and the work tree and add them to the index.

```bash
git add --patch
```

Author name and email

```bash
git config --global user.name "author_name"
git config --global user.email email_address
```

All repository settings

```bash
git config --list
```

Remove paths only from the index

```bash
git rm --cashed
```

Discard changes

```bash
git checkout -- file_name
```

Replace the tip of the current branch by creating a new commit

```bash
git commit --amend
```

Revert some existing commits

```bash
git revert commit_hash
```

Create a new branch

```bash
git checkout --branch <branch_name>
git branch <branch_name>
git branch <branch_name> <upstream_name>/<remote_branch>
```

Add remote repository

```bash
git remote add <upstream_name> <url>
```

Push in upstream and create Merge Request

```bash
git push -u <upstream_name> -o merge_request.create
```

## Clone

Clone large svn repository

```bash
git svn clone -r1:HEAD http://my-project.googlecode.com/svn/ --authors-file=users.txt --no-metadata -s my_project
git svn fetch -r1:HEAD --authors-file=users.txt
```

Clone and auto checkout

```bash
git clone --branch
```

Сlone a specific branch

```bash
git clone --branch --single-branch
```

## Stash

Stash the changes

```bash
git stash
git stash apply
git stash --save "massage_text"
```

## Reset

Unstage

```bash
git reset HEAD file_name
```

Resets the index and working tree

```bash
git reset --hard commit_hash
```

Does not touch the index file or the working tree at all

```bash
git reset --soft commit_hash
```

Resets the index but not the working tree. Default

```bash
git reset --mixed commit_hash
```
