from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='arcs.shibboleth.plone',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Russell Sim',
      author_email='russell.sim@arcs.org.au',
      url='http://svn.plone.org/svn/plone/plone.app.example',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['arcs', 'arcs.shibboleth'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'jcu.shibboleth.pas',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
