Tests for arcs.shibboleth.plone

test setup
----------

check that the plugin was added by the setup profile:

    >>> self.portal.acl_users.shibboleth
    <ShibbolethHelper at /plone/acl_users/shibboleth>

check that the login form is set
    >>> self.portal.acl_users.shibboleth.login_path
    'login_form'

and so on. Continue your tests here

    >>> 'ALL OK'
    'ALL OK'

