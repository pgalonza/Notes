---
title: "Git"
draft: false
description: "Git notes"
---

{{< toc >}}

## Commands

Removed git tags

```bash
git tag -d $(git tag -l)
git fetch
git push origin --delete $(git tag -l)
git tag -d $(git tag -l)
```

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

Discard changes in file

```bash
git checkout <hash> -- file_name
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

Merge without checkout and push

```bash
git fetch . <src_branch>:<dst_branch>
git push --all
```

Remove file from all commits

```bash
git filter-branch --index-filter 'rm -f <file name> -- --all'
```

Delete remote brannch

```bash
git push --delete origin <remote branch>
```

Add file from other branch

```bash
git checkout <from branch> <file or directory>
```

Pull branch from another remote repository

```bash
git remote add <remote label> <url>
git pull <remote label> <remote branch name>:<new local branch name>
```

Add commit with date

```bash
git commit -am "<>" --date "<mm>/dd/<yyyy>"
```

Sort branch by date

```bash
git config --global branch.sort -committerdate
```

Store credentials

```bash
git config --global credential.helper store
```

## Create new repository

Create the folder and initialization on server

```bash
mkdir example.git
cd example.git
git init --bare --share
useradd -s /usr/bin/git-shell -d /git git
```

Create local repository, add remote,

```bash
git init
git remote add origin ssh://username@example.com/var/git/example.git
touch changelog
git add changelog
git commit -a -m"Initital commit"
git push origin master
```

**[Git ignore templates](https://github.com/github/gitignore)**

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

Apply range of commits

```bash
git cherry-pick <start hash of commit - 1>..<end hash commit>
```

Patch

```bash
git diff (-binary) <> > <name>.patch
git format-patch <>

git apply <name>.patch
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

Resets using index

```bash
git reflog
git reset HEAD@{<index>}
```

## Log

Show log with graph

```bash
git log --decorate --graph --branches --oneline
git log --all --decorate --graph --oneline
```

## BFG Repo-Cleaner

Install

```bash
git clone --mirror git://example.com/some-big-repo.git
```

Clean the repository

```bash
java -jar bfg.jar --strip-blobs-bigger-than 100M some-big-repo.git
```

Replace the passwords

```bash
bfg --replace-text passwords.txt  my-repo.git
```

Remove the files and folders

```bash
bfg --delete-folders .git --delete-files .git  --no-blob-protection  my-repo.git
```

## SVN to GIT

1. Create commits authors file

    ```bash
    svn log --xml | grep author | sort -u | perl -pe 's/.*>(.*?)<.*/$1 = /' > users.txt
    ```

2. Then allow the record to the form

    ```text
    krasnovov = Krasnov Oleg Viktorovich <krasnovov@example.com>
    ```

3. Cone repository

    * ```bash
      git svn clone http://my-project.googlecode.com/svn/ --authors-file=users.txt --no-metadata -s my_project
      ```

    * If repository so large and get timeout, use host with fast file system
    * For contine, execute command

      ```bash
      git svn fetch --authors-file=../users.txt
      ```

    * To clone to a specific revision use -rXXX:HEAD parameter

      ```bash
      git svn clone -rXXX:HEAD http://my-project.googlecode.com/svn/ --authors-file=users.txt --no-metadata -s my_project
      git svn fetch -rXXX:HEAD --authors-file=../users.txt
      ```

4. Create .gitignore file

    ```bash
    git svn show-ignore > .gitignore
    ```

5. Create backup

6. Convert branches and tags

    ```bash
    for t in $(git for-each-ref --format='%(refname:short)' refs/remotes/tags); do git tag ${t/tags\//} $t && git branch -D -r $t; done
    for b in $(git for-each-ref --format='%(refname:short)' refs/remotes); do git branch $b refs/remotes/$b && git branch -D -r $b; done
    ```

7. Remove tag and branch with suffix @xxx

    ```bash
    for p in $(git for-each-ref --format='%(refname:short)' | grep @); do git branch -D $p; done
    for p in $(git for-each-ref --format='%(refname:short)' | grep @); do git tag -d $p; done
    ```

8. Push local repository to remote

    ```bash
    git branch -d trunk
    git remote add origin git@my-git-server:myrepository.git
    git push origin --all
    git push origin --tags
    ```

To synchronize the changes made in svn, restore from backup  step №5 and repeat the steps.

```bash
git svn fetch --authors-file=../users.txt
```

## GPG

### Copy key to another machine

PC1

```bash
gpg —list-keys
gpg —export <Key ID> > public.key
gpg —export-secret-key <Key ID> > private.key
```

PC2

```bash
gpg —import public.key
gpg —import —allow-secret-key-import private.key
gpg --list-secret-keys --keyid-format=long
git config --global user.signingkey <Key ID>
git config --global commit.gpgsign true
```

## Credentials

Store credentials

```bash
git config --global credential.helper store
```

Store credentials in memory

```bash
git config --global credential.helper 'cache --timeout=<time>'
```

Use script

```bash
#!/bin/bash

echo username=<username>
echo password=<password>
```

```bash
git config --global credential.helper '<path to script>'
```

## Worktree

Create worktree

```bash
git worktree add <path> <branch>
git worktree add --track -b <branch> <path> <remote>/<branch>
```

List worktrees

```bash
git worktree list
```

Remove worktree

```bash
git worktree remove <path>
```


## Troubleshooting

### Windows

Filename too long

```bash
git config --global core.longpaths true
```

Illegal instruction

```bash
git config --global core.fscache true
```
