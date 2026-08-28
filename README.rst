.. image:: https://img.shields.io/badge/status-deprecated-red
   :alt: Status

###############################
This repository is deprecated
###############################

**This repository is no longer maintained.**

The Free Text Response XBlock has been moved to `xblocks-extra <https://github.com/openedx/xblocks-extra>`_.

Please use the new repository for all future work.

Free Text Response XBlock
================================

XBlock to capture a free-text response.

|badge-ci|
|badge-coveralls|

This package provides an XBlock for use with the EdX Platform and makes
it possible for instructors to create questions that expect a
free-text response.


Installation
------------


System Administrator
~~~~~~~~~~~~~~~~~~~~

To install the XBlock on your platform,
add the following to your `requirements.txt` file:

    xblock-free-text-response

You'll also need to add this to your `INSTALLED_APPS`:

    freetextresponse


Course Staff
~~~~~~~~~~~~

To install the XBlock in your course,
access your `Advanced Module List`:

    Settings -> Advanced Settings -> Advanced Module List

and add the following:

    freetextresponse



.. |badge-coveralls| image:: https://coveralls.io/repos/github/Stanford-Online/xblock-free-text-response/badge.svg?branch=master
   :target: https://coveralls.io/github/Stanford-Online/xblock-free-text-response?branch=master
.. |badge-ci| image:: https://github.com/openedx/xblock-free-text-response/workflows/Python%20CI/badge.svg?branch=master
   :target: https://github.com/openedx/xblock-free-text-response/actions?query=workflow%3A%22Python+CI%22
