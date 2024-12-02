# Commit 9

'''

    In git, "HEAD" is the commit that you are currently in.
    'master' is the newest commit of the main/master branch.
    Till now, I have only 1 branch. SO its name is 'master'    
    In some OS, it may be named 'main' instead of 'master'.

    HEAD -> master means you are currently viewing 'master' commit.

    Commit hash = unique symbol given to any commits
    Ex: f8a1ea71e36250eff0a0550699a177101cceafbd
    It is used to uniquely identify any commit.

    In your terminal,
    when you run git log --all --graph
    HEAD is written on right of the commit hash you are currently viewing.

    Ex: 
        commit f8a1ea71e36250eff0a0550699a177101cceafbd (HEAD -> master)

    >> viewing previous versions <<


    git checkout <commit hash/branch name>
        Ex: git checkout 5aeba3063e4a3fdad859d56fcd04dd229cbd268e

            this will open that version/commit of our code whose commit hash is 5aeba3063e4a3fdad859d56fcd04dd229cbd268e

    git checkout master
        will open the latest version of our code on master branch

    

'''