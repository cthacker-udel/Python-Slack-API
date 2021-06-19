## Python Slack API
> Author : Cameron Thacker (University of Delaware)

### Description :

This project implements the Slack API using Python, the way the project is structured includes multiple separate Python files, which each implement separate attributes of each individual API. These separate files all tie into one file, the [SlackClient](https://github.com/cthacker-udel/Python-Slack-API/blob/master/SlackClient.py) file. This file then utilizes all methods declared in the file [SlackRestAPI](https://github.com/cthacker-udel/Python-Slack-API/blob/master/SlackRestAPI.py). The [SlackRestAPI](https://github.com/cthacker-udel/Python-Slack-API/blob/master/SlackRestAPI.py) file utilizes multiple classes to implement each individual API, and provide a more organized layout, each class containing all the methods and the only requirement, is to pass in the edited [SlackClient](https://github.com/cthacker-udel/Python-Slack-API/blob/master/SlackClient.py) when creating an instance of the class. Then utilize all the methods available, editing necessary instance attributes, which represent query parameters(with GET requests) and body parameters(with POST requests).  
