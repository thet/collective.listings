from setuptools import setup

import pathlib


version = "1.0.1.dev0"
long_description = "\n".join(
    [pathlib.Path(filename).read_text() for filename in ("README.md", "CHANGES.md")]
)

setup(
    name="collective.listings",
    version=version,
    description="Alternative content listings for Plone.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Get more strings from
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: 6.2",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="plone classicui content listing",
    author="Johannes Raggam",
    author_email="thetetet@gmail.com",
    url="https://github.com/thet/collective.listings/",
    license="gpl",
    python_requires=">=3.10",
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "Products.CMFPlone>=6.1",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "plone.browserlayer",
            "plone.testing>=5.0.0",
            "plone.restapi[test]",
            "plone.app.robotframework",
            "robotsuite",
        ],
    },
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
