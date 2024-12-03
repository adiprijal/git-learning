# Commit 10

'''

    >> Restoring to previous commit <<

    Why?

    When we are doing any project we may find out that our code was better and accurate in any previous commit.
    In that case, we'll want to restore that code.


    git checkout <hash>       will only view previous commit

    To restore previous version, we use

    git checkout <hash|branch> <file|folder>
        git checkout <hash|branch> file
        git checkout <hash|branch> folder
        git checkout <hash|branch> .

        What happens?
        After this, your code from that commit hash will be restored in the latest commit.
        
        Know that it will not create a new commit. Rather it'll update the HEAD commit with the code of that commit which you wanted to restore. 

        Also it only keeps the changes in staging area i.e. changes are only added , not commited.

        So, now you can either 
        1)  amend current HEAD commit
        2)  create new commit for restored code


'''