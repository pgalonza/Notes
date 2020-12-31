# Git

Used words
* feature — используется при добавлении новой функциональности уровня приложения
* fix — если исправили какую-то серьезную багу
* docs — всё, что касается документации
* style — исправляем опечатки, исправляем форматирование
* refactor — рефакторинг кода приложения
* test — всё, что связано с тестированием
* chore — обычное обслуживание кода
* This commit will ... (this commit will fix bugs)

## Create new repository
Create the folder and initialization on server
```
mkdir example.git
cd example.git
git init --bare --share
useradd -s /usr/bin/git-shell -d /git git
```

Create local repository, add remote,
```
git init
git remote add origin ssh://username@example.com/var/git/example.git
touch changelog
git add changelog
git commit -a -m"Initital commit"
git push origin master
```

###### [Git ignore templates](https://github.com/github/gitignore)

## BFG Repo-Cleaner
Install
```
git clone --mirror git://example.com/some-big-repo.git
```

Clean the repository
```
java -jar bfg.jar --strip-blobs-bigger-than 100M some-big-repo.git
```

Replace the passwords
```
bfg --replace-text passwords.txt  my-repo.git
```
Remove the files and folders
```
bfg --delete-folders .git --delete-files .git  --no-blob-protection  my-repo.git
```

## SVN to GIT

1. Create commits authors file
  ```
  svn log --xml | grep author | sort -u | perl -pe 's/.*>(.*?)<.*/$1 = /' > users.txt
  ```
2. Then allow the record to the form
  ```
  krasnovov = Krasnov Oleg Viktorovich <krasnovov@example.com>
  ```
3. Cone repository
  * ```
    git svn clone http://my-project.googlecode.com/svn/ --authors-file=users.txt --no-metadata -s my_project
    ```
  * If repository so large and get timeout, use host with fast file system
  * For contine, execute command
    ```
    git svn fetch --authors-file=../users.txt
    ```
  * To clone to a specific revision use -rXXX:HEAD parameter
  ```
  git svn clone -rXXX:HEAD http://my-project.googlecode.com/svn/ --authors-file=users.txt --no-metadata -s my_project
  git svn fetch -rXXX:HEAD --authors-file=../users.txt
  ```
4. Create .gitignore file
  ```
  git svn show-ignore > .gitignore
  ```
5. Create backup

6. Convert branches and tags
  ```
  for t in $(git for-each-ref --format='%(refname:short)' refs/remotes/tags); do git tag ${t/tags\//} $t && git branch -D -r $t; done
  for b in $(git for-each-ref --format='%(refname:short)' refs/remotes); do git branch $b refs/remotes/$b && git branch -D -r $b; done
  ```

7. Remove tag and branch with suffix @xxx
  ```
  for p in $(git for-each-ref --format='%(refname:short)' | grep @); do git branch -D $p; done
  for p in $(git for-each-ref --format='%(refname:short)' | grep @); do git tag -d $p; done
  ```

6. Push local repository to remote
  ```
  git branch -d trunk
  git remote add origin git@my-git-server:myrepository.git
  git push origin --all
  git push origin --tags
  ```

To synchronize the changes made in svn, restore from backup  step №5 and repeat the steps.
```
git svn fetch --authors-file=../users.txt
```

## Troubleshooting

### Windows

Filename too long
```
git config --global core.longpaths true
```

Illegal instruction
```
git config --global core.fscache true
```
