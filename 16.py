# Commit 16

'''

    >> Linking GitHub to local repository <<

    ~ Open terminal in your local repo.     [ repo - repository ]

    git remote add <remote_name> <url> 

    Ex:     git remote add origin https://github.com/adiprijal/git-learning.git

    # we've not learned about SSH key yet. So, use https url for now.

    'remote_name' can be anything.
    But, generally it's named 'origin'.

    

    git remote              List all remote repositories that are linked
        git remote -v       
            List all remote repositories (but with more detail)     [ v - verbose = more detail]


    >> Unlink remote repo <<

        git remote remove <remote_name>

'''