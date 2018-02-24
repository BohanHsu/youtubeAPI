# Please make sure you run python and pip in 2 version (not 3)

# How to start?

Download code

    git clone https://github.com/BohanHsu/youtubeAPI.git

Install dependencies

    sudo python -m pip install --upgrade google-api-python-client
    sudo python -m pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2

I don't have pip, [install it](https://pip.pypa.io/en/stable/installing/), super easy!


# This is important!

To start use this program, apply your own app and copy **client_secret.json** into root directory. [How to?](https://developers.google.com/youtube/v3/getting-started)

# How to run?
Edit parameter.py file:


### Update your search keyword

    SEARCH_KEY_WORDS="facebook"

### How many videos' information you want to download for that keyword
    MAX_NUMBER=50
    

### Run:
    python youtubeapi.py

**Open the link, login your google account, and paste the link back to python program, press Enter**

### Look for new csv file generated in your root directory.

I don't understand what each column stands for: [read google api definition](https://developers.google.com/youtube/v3/docs/videos)

# Troubleshoot

### If you see this:

    Exception:
    Traceback (most recent call last):
      File "/Library/Python/2.7/site-packages/pip/basecommand.py", line 215, in main
      status = self.run(options, args)
      File "/Library/Python/2.7/site-packages/pip/commands/install.py", line 342, in run
      prefix=options.prefix_path,
      File "/Library/Python/2.7/site-packages/pip/req/req_set.py", line 778, in install
      requirement.uninstall(auto_confirm=True)
      File "/Library/Python/2.7/site-packages/pip/req/req_install.py", line 754, in uninstall
      paths_to_remove.remove(auto_confirm)
      File "/Library/Python/2.7/site-packages/pip/req/req_uninstall.py", line 115, in remove
      renames(path, new_path)
      File "/Library/Python/2.7/site-packages/pip/utils/__init__.py", line 267, in renames
      shutil.move(old, new)
      File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/shutil.py", line 302, in move
      copy2(src, real_dst)
      File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/shutil.py", line 131, in copy2
      copystat(src, dst)
      File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/shutil.py", line 103, in copystat
      os.chflags(dst, st.st_flags)
      OSError: [Errno 1] Operation not permitted: '/tmp/pip-7_woYF-uninstall/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/six-1.4.1-py2.7.egg-info'

### Run use the following command to install dependencies

    sudo python -m pip install --upgrade google-api-python-client --ignore-installed six
    sudo pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 --ignore-installed six
