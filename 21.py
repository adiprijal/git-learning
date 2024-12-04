# commit 21

'''

    >> Push Error <<

        ~   When you make a new commit in your local repo and then try to push it to remote repo, it goes smoothly.

        ~   But if we make a commit amend and then try to push it , an error will occur.

        Why error?

            When we amend commit, it'll create a branch because there'll be two different version of a same commit in our local and remote repo.
            And when we try to push local repo to remote , git will not allow that because it'll lead to disappearing of that version of commit which is already in remote. As deleting a branch of code may be risky, git return an error.

            Ex:
                    To https://github.com/adiprijal/git-learning.git
                    ! [rejected]        master -> master (non-fast-forward)
                    error: failed to push some refs to 'https://github.com/adiprijal/git-learning.git'
                    hint: Updates were rejected because the tip of your current branch is behind
                    hint: its remote counterpart. If you want to integrate the remote changes,
                    hint: use 'git pull' before pushing again.
                    hint: See the 'Note about fast-forwards' in 'git push --help' for details.

        Then what?

            We should try to not make any necessary branch disappear.

            But for now, to bypass this error, we can force push...

                i.e.  git push origin master -f                                         [ f = forced ]
                        OR, git push -f
                            { it works if you have set upstream }

            
        This command will force push our local repo to remote.

'''