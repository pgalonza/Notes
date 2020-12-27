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
