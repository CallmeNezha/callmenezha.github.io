Title: XStatic, a Python packaging standard for bundling external static files as Python packages
Date: 2023-07-25 00:46
Category: Python
Tags: Python, Packaging, Deprecated

XStatic is a Python packaging standard for bundling external static files as Python packages. It allows easy usage of these files across operating systems and package management systems. With a focus on minimalism, XStatic packages provide only the necessary files, making it convenient to handle static assets maintained by others. It simplifies virtual environment creation and supports different platforms, promoting efficient distribution and integration of static files in Python projects.

There are several packeges conform to xstatic standard in maintained by xstatic-py, refer to https://github.com/xstatic-py.

* xstatic-jquery
* xstatic-bootstrap
* xstatic-jquery_ui

You can package you assets as well.

## Real life usage: tornado-xstatic
XStatic is a means of packaging static files, especially JS libraries, for Python applications. Tornado is a Python web framework.
`tornado-xstatic` is a thin boilerplate intergrate both side.


## Update 2023-07-25
After I used webpack, now I think this library can be archived into the history now... Webpack can pack all js files 
used in the browser which means you aren't bother to maintain all the versions of js library and package them into 
XStatic nowaadys.


