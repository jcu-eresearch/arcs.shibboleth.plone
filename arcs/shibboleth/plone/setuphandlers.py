#############################################################################
#
# Copyright (c) 2010 Victorian Partnership for Advanced Computing Ltd and
# Contributors.
# All Rights Reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

from zope.component import getUtility
from zope.component import getMultiAdapter
from StringIO import StringIO
from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.portlets.interfaces import IPortletManager
from plone.app.openid.portlets.login import Assignment as LoginAssignment
from Products.CMFCore.utils import getToolByName
from Products.PluggableAuthService.interfaces.plugins \
                import IExtractionPlugin

from jcu.shibboleth.pas.interface import IShibbolethHelper
from jcu.shibboleth.pas.plugin import ShibbolethHelper


def hasShibbolethPlugin(portal):
    acl=getToolByName(portal, "acl_users")
    plugins=acl.plugins.listPlugins(IExtractionPlugin)

    for plugin in plugins:
        if IShibbolethHelper.providedBy(plugin[1]):
            return True

    return False


def createShibbolethPlugin(portal, out):
    print >>out, "Adding a Shibboleth plugin"
    acl=getToolByName(portal, "acl_users")
    # TODO the normal add method seems to have problems because of the add page being a browser view.
    #acl.manage_addProduct["jcu.shibboleth.pas"].manage_addShibbolethHelperForm(
    #        id="shibboleth", title="Shibboleth authentication plugin")
    p=ShibbolethHelper(id='shibboleth', title="Shibboleth authentication plugin")
    acl._setObject(p.getId(), p)
    p.login_path = 'login_form'


def activatePlugin(portal, out, plugin):
    acl=getToolByName(portal, "acl_users")
    plugin=getattr(acl, plugin)
    interfaces=plugin.listInterfaces()

    activate=[]

    for info in acl.plugins.listPluginTypeInfo():
        interface=info["interface"]
        interface_name=info["id"]
        if plugin.testImplements(interface):
            if not interface_name in ['IRolesPlugin', 'IGroupsPlugin']:
                activate.append(interface_name)
                print >>out, "Activating interface %s for plugin %s" % \
                        (interface_name, info["title"])

    plugin.manage_activateInterfaces(activate)


def importVarious(context):
    # Only run step if a flag file is present (e.g. not an extension profile)
    if context.readDataFile('shibboleth-pas.txt') is None:
        return

    site = context.getSite()
    out = StringIO()
    if not hasShibbolethPlugin(site):
        createShibbolethPlugin(site, out)
        #activatePlugin(site, out, "shibboleth")


