# FTPy
Python-based FTP client for Portland State's agile course.

## Installation
The following instructions are primarily intended for Mac/Linux, but they should also work for Cygwin.

1. Install [Python 2.7](https://www.python.org/downloads/) if it's not already on your system.

2. Install [pip](https://pip.pypa.io/en/latest/installing.html), the Python package manager.

3. Install [virtualenv](https://virtualenv.pypa.io/en/latest/).

	```[sudo] pip install virtualenv```

4. Install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/index.html). Follow installation instructions [here](http://virtualenvwrapper.readthedocs.org/en/latest/install.html).

5. Clone this repo.

	```git clone git@github.com:agile-pdx/FTPy.git```

6. Create your virtual environment. This will isolate the project from any other python projects you may have running on your system.

	```mkvirtualenv -a FTPy/ FTPy```

7. Enter your new virtual environment. From any directory:

	```workon FTPy```

8. Install dependencies:

	```pip install -r requirements.txt```

9. When you are finished and wish to exit the virtualenv, exit by the command:

    ```deactivate```


## External Links

* [Scrum Board](https://trello.com/cs410agile)
* [Slack](https://agile-pdx.slack.com/messages)
