"""Lists secondary staging stores."""
from baseCmd import *
from baseResponse import *


class listSecondaryStagingStoresCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """the ID of the staging store"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """the name of the staging store"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """the staging store protocol"""
        self.protocol = None
        self.typeInfo['protocol'] = 'string'
        """the staging store provider"""
        self.provider = None
        self.typeInfo['provider'] = 'string'
        """the Zone ID for the staging store"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'uuid'
        self.required = []


class listSecondaryStagingStoresResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the image store"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the details of the image store"""
        self.details = None
        self.typeInfo['details'] = 'set'
        """the name of the image store"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the protocol of the image store"""
        self.protocol = None
        self.typeInfo['protocol'] = 'string'
        """the provider name of the image store"""
        self.providername = None
        self.typeInfo['providername'] = 'string'
        """the scope of the image store"""
        self.scope = None
        self.typeInfo['scope'] = 'scopetype'
        """the url of the image store"""
        self.url = None
        self.typeInfo['url'] = 'string'
        """the Zone ID of the image store"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'
        """the Zone name of the image store"""
        self.zonename = None
        self.typeInfo['zonename'] = 'string'

