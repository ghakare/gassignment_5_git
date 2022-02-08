import git
repo = git.Repo.clone_from(self._small_repo_url(), os.path.join(rw_dir, 'repo'), branch='master')

heads = repo.heads
master = heads.master       # lists can be accessed by name for convenience
master.commit               # the commit pointed to by head called master
master.rename('new_name')   # rename heads
master.rename('master')
