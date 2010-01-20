Tests for arcs.shibboleth.plone

test setup
----------

check that the plugin was added by the setup profile:

    >>> self.portal.acl_users.shibboleth
    <ShibbolethHelper at /plone/acl_users/shibboleth>

check that the login form is set
    >>> self.portal.acl_users.shibboleth.login_path
    'login_form'

check that the plugin is activated correctly
    >>> from Products.PluggableAuthService.interfaces.plugins import \
    ... ILoginPasswordExtractionPlugin, IChallengePlugin, IAuthenticationPlugin, \
    ... IRolesPlugin, IGroupsPlugin, IUserEnumerationPlugin, IPropertiesPlugin

    >>> for k, v in app.plone.acl_users.plugins.listPlugins(IChallengePlugin):
    ...     if k == 'shibboleth':
    ...         print v
    <ShibbolethHelper at shibboleth>

    >>> for k, v in app.plone.acl_users.plugins.listPlugins(IAuthenticationPlugin):
    ...     if k == 'shibboleth':
    ...         print v
    <ShibbolethHelper at shibboleth>

    >>> for k, v in app.plone.acl_users.plugins.listPlugins(ILoginPasswordExtractionPlugin):
    ...     if k == 'shibboleth':
    ...         print v
    <ShibbolethHelper at shibboleth>

    >>> for k, v in app.plone.acl_users.plugins.listPlugins(IUserEnumerationPlugin):
    ...     if k == 'shibboleth':
    ...         print v
    <ShibbolethHelper at shibboleth>

    >>> for k, v in app.plone.acl_users.plugins.listPlugins(IPropertiesPlugin):
    ...     if k == 'shibboleth':
    ...         print v
    <ShibbolethHelper at shibboleth>

check that the first properties plugin is shibboleth
    >>> app.plone.acl_users.plugins.listPlugins(IPropertiesPlugin)[0][0]
    'shibboleth'


