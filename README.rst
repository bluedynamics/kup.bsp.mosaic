.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============
kup.bsp.mosaic
==============

This is an example addon for Mosaic customization on Plone 5.1.x

Hint: look at the commit history and its diffs.

Features
--------

- Installs Mosaic.
- Sets Mosaic's ``layout_view`` as default for Document.
- Create a custom site layout for Document.
- Switch off Basic layout.
- add a simple tile showing a random number.
- add a tile with schema adding some kind of note.
- enable and use site layouts.


Installation
------------

Install kup.bsp.mosaic by adding it to your buildout::

    [buildout]

    ...

    eggs =
        kup.bsp.mosaic


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/kup.bsp.mosaic/issues
- Source Code: https://github.com/collective/kup.bsp.mosaic


Support
-------

If you are having issues, please let me know: jens@bluedynamics.com


License
-------

The project is licensed under the GPLv2.
