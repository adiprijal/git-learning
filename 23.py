# Commit 23

'''

    As discussed in 22.py, 
    when a new user 
        ~   clones our repo
        ~   makes new commits
        ~   pushes it to GitHub ..

        when you open terminal in that new clone repo and run git log --all

        you'll see sth like this...

             commit 34e87c2caa78d06b27aec7991242f1c40ac3e8bb (HEAD -> master, origin/master, origin/HEAD)
             Author: Adip Rijal <rizalaryan2@gmail.com>
             Date:   Wed Dec 4 15:19:57 2024 +0545
                commit 22

        But if we run git log in our original local repo.. you'll see

            commit e31207f582676969e5ab9330e78e34bd662cf605 (HEAD -> master, origin/master)
             Author: Adip Rijal <rizalaryan2@gmail.com>
             Date:   Wed Dec 4 15:16:33 2024 +0545
                commit 21

                
            What is happening here?
                To understand better , lets say Manoj is another user who cloned Adip's repo.
                Now Manoj made some changes, commited it and pushed to GitHub.
                His git log shows that latest commit is 'commit 22' and both remote and local repo are updated to 'commit 22'

                But, in Adip's case, his git log also shows that his local and remote repo are up to date but are at 'commit 21'

                So why so?  
                        Here, remote tracking branches { ex: origin/master } doesn't update automatically.
                        As remote repo in Adip's pc was last updated to 'commit 21' and his local repo is also at 'commit 21' , the terminal shows that it's updated.

                        But it's not. as Manoj already made a new push 'commit 22'

    How to solve?
        ~   Fetch the updated version of remote repo in Adip's pc.
        ~   Pull updated remote repo to local repo.

'''