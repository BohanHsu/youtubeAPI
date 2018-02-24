# How to start?


Download code

    git clone

Install dependencies

    sudo pip install --upgrade google-api-python-client
    sudo pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2

I don't have pip, [install it](https://pip.pypa.io/en/stable/installing/), super easy!


# This is important!

To start use this program, apply your own app and copy **client_secret.json** into root directory. [How to?](https://developers.google.com/youtube/v3/getting-started)

# How to run?
Edit parameter.py file:


### Update your search keyword

    SEARCH_KEY_WORDS="facebook"

### How many videos' information you want to download for that keyword
    MAX_NUMBER=20
    
I don't understand what each column stands for: [read google api definition](https://developers.google.com/youtube/v3/docs/videos)

### Run:
    python youtubeapi.com

**Open the link, login your google account, and paste the link back to python program, press Enter**

### Look for new csv file generated in your root directory.
