# Commit 22

'''

    >> Clone GitHub repo to computer <<                 [ downloading form github ]

    ~ Open terminal         [ here i'm opening desktop directory ]
    
        Simply put, open terminal where you want to download GitHub repository/folder.


    run,
        git clone <url> <repo_name>

            Ex: git clone https://github.com/adiprijal/git-learning git-tut

            Here, repo_name is not compulsory.
            If you don't give any repo name , it'll use the name same as of in GitHub
                Ex: git clone https://github.com/adiprijal/git-learning

                Here, the new created folder will be named 'git-learning'


                
*******************************************************************************************************************


    You can also use this command to clone a local git repo to another local git repo.
    i.e.
            git clone <old_repo_address> <new_repo_name>

            Ex: 
                git clone .\git-learning\ git-tut

        This'll create a new folder 'git-tut' which is clone of 'git-learning' folder and all same commit history.  



    why clone?
        Cloning our repo is similar to multiple users working on same project.
        With cloning multiple user can work on the project in different computer and make commits and later sync those changes.

        We'll learn to sync those changes in next 23.py      

'''