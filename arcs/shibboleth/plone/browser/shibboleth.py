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

from zope.interface import implements
from plone.memoize.instance import memoize

from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView


class ShibbolethInfoView(BrowserView):
    def getHostName(self):
        """ Extract host name in virtual host safe manner

        @return: Host DNS name, as requested by client. Lowercased, no port part.
                 Return None if host name is not present in HTTP request headers
                 (e.g. unit testing).
        """

        if "HTTP_X_FORWARDED_HOST" in self.request.environ:
            # Virtual host
            host = self.request.environ["HTTP_X_FORWARDED_HOST"]
        elif "HTTP_HOST" in self.request.environ:
            # Direct client request
            host = self.request.environ["HTTP_HOST"]
        else:
            return None

        # separate to domain name and port sections
        host=host.split(":")[0].lower()

        return "https://" + host



