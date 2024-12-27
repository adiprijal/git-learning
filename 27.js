// git pull rebase

// when you are working on a team project, you will need to pull the changes from the remote repository to your local repository.
// But when you pull the changes, you are fetching the changes and merging them into your local repository.
// This can create a lot of merge commits in your history, which can make it difficult to read.
// To avoid this, you can use the git pull rebase command.

alert("when you pull from a remote repository, you are fetching the changes and merging them into your local repository. ");

alert("git pull rebase is a command that allows you to reapply commits on top of another base tip. It is useful for keeping a clean history and avoiding merge commits. ");

alert("so always try using git pull rebase instead of git pull when you are working on a team project. ");

// syntax
// git pull --rebase

// this will fetch the changes from the remote repository and reapply your commits on top of the base tip. This will keep your history clean and avoid merge commits.

// if you get a conflict while rebasing, you have two options:
// 1. resolve the conflict manually and continue the rebase
// 2. abort the rebase and do git pull

// to resolve the conflict manually, you can use the following commands:
// 1. git status
// 2. git diff
// 3. git add <file>
// 4. git rebase --continue

// to abort the rebase and do git pull, you can use the following command:
// git rebase --abort
// git pull