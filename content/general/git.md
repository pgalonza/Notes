---
title: "Git"
draft: false
---

Removed git tags

```bash
git tag -d $(git tag -l)
git fetch
git push origin --delete $(git tag -l)
git tag -d $(git tag -l)
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
