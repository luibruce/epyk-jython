![](https://github.com/luibruce/epyk-jython/blob/master/static/images/logo.PNG?raw=true)

# Epyk from Jython

Epyk is a Python package which can run on any distribution.

Installation:
==================

Install pip.exe on your Jython distribution

The below command will add the pip.exe command to the bin folder in the Jython directory

> java -jar C:\jython2.7.2\jython.jar -m ensurepip

Use pip to install packages

Most of the packages should be available in Jython (as long as there is not C bindings)

In order to run the pip.exe command you can run the below lines:

> SET JAVA_HOME=C:\Program Files\Java\jre1.8.0_251
> C:\jython2.7.2\bin\pip.exe install epyk


Then for the Flask server

> SET JAVA_HOME=C:\Program Files\Java\jre1.8.0_251
> C:\jython2.7.2\bin\pip.exe install flask



Get Started:
============

Add a UI project using Epyk CLI.

From the project directory root

```bash
C:\jython2.7.2\bin\epyk_project.exe add
```

This will create the standard ui folders structure

```bash
C:\jython2.7.2\bin\epyk_project.exe transpike_all
```

Please note that for some reasons in the __import__ the retrieval of the 
page object is not working.

So for Jython environment it is better to use the get_page method.

For example

```python
def get_page(page):
  """

  :param page:

  :rtype: epyk.core.Page.Report
  """
  page.ui.button("Test Button")
```


Documentation:
==================

For more information about [Epyk](https://github.com/epykure/epyk-ui) 
