# docker_instagram_bot	 
This is a repository which stores the setup for a docker container which hosts my instagram bot. The instagram bot is written in Python, utilizing the Selenium library. Currently it is exposed as an API using Flask.

The docker container itself is setup with an Nginx server which hosts the flask API, as well as a Selenium Grid with a firefox node running with it. The flask application talks directly to the selenium grid in order to perform its webscraping.

The underlying instagram bot code in this docker container is based off of the original repository here - [instagram-post-scheduler-bot](https://github.com/ColeInc/instagram-post-scheduler-bot)

##Resources:
I've made a directory named resources_example inside app/flask which is an example of what you can edit yourself to your liking. mysql_credentials being the credentials for a MySQL server which would run hand in hand with this API for long term storage. comments_list and hashtags_list being a custom list you'd like the bot to use in its processes.
All you need to do is rename the resources_example directory to resources in order for the python scripts to pick it up.
