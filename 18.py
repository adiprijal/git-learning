# Commit 18

'''

    >> Pushing local repo to remote repo <<

    git push <remote_name> <branch> 
        ~   Upload a branch of your git version history to your remote repository

    
    As we know, there may be multiple branches of our commits in git. We can push only one branch at a time.

    Ex:  
        git push origin master      

        ~ upload the 'master' branch to remote repo named 'origin' 

        
    If you now run, git log --all --graph, you will see sth like this on the latest commit of the pushed branch..

     commit eb87547fb96a6db9e54fb2d68f6adb93d99485eb (HEAD -> master, origin/master)

     Here, origin/master shows which branch is the master branch in remote repo


     Know that, git push only pushes commits, not changes, not staged changes... only commits.

     So before pushing make sure you have commited your changes.

'''