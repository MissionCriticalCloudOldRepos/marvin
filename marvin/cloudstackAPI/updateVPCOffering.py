"""Updates VPC offering"""
from baseCmd import *
from baseResponse import *


class updateVPCOfferingCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the id of the VPC offering"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """the display text of the VPC offering"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """the name of the VPC offering"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """update state for the VPC offering; supported states - Enabled/Disabled"""
        self.state = None
        self.typeInfo['state'] = 'string'
        self.required = ["id", ]


class updateVPCOfferingResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the id of the vpc offering"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the date this vpc offering was created"""
        self.created = None
        self.typeInfo['created'] = 'date'
        """an alternate display text of the vpc offering."""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """indicates if the vpc offering supports distributed router for one-hop forwarding"""
        self.distributedvpcrouter = None
        self.typeInfo['distributedvpcrouter'] = 'boolean'
        """true if vpc offering is default, false otherwise"""
        self.isdefault = None
        self.typeInfo['isdefault'] = 'boolean'
        """the name of the vpc offering"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """The secondary system compute offering id used for the virtual router"""
        self.secondaryserviceofferingid = None
        self.typeInfo['secondaryserviceofferingid'] = 'string'
        """The secondary system compute offering name used for the virtual router"""
        self.secondaryserviceofferingname = None
        self.typeInfo['secondaryserviceofferingname'] = 'string'
        """The primary system compute offering id used for the virtual router"""
        self.serviceofferingid = None
        self.typeInfo['serviceofferingid'] = 'string'
        """The primary system compute offering name used for the virtual router"""
        self.serviceofferingname = None
        self.typeInfo['serviceofferingname'] = 'string'
        """state of the vpc offering. Can be Disabled/Enabled"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """indicated if the offering can support region level vpc"""
        self.supportsregionLevelvpc = None
        self.typeInfo['supportsregionLevelvpc'] = 'boolean'
        """the list of supported services"""
        self.service = []

class capability:
    def __init__(self):
        """"can this service capability value can be choosable while creatine network offerings"""
        self.canchooseservicecapability = None
        """"the capability name"""
        self.name = None
        """"the capability value"""
        self.value = None

class provider:
    def __init__(self):
        """"uuid of the network provider"""
        self.id = None
        """"true if individual services can be enabled/disabled"""
        self.canenableindividualservice = None
        """"the destination physical network"""
        self.destinationphysicalnetworkid = None
        """"the provider name"""
        self.name = None
        """"the physical network this belongs to"""
        self.physicalnetworkid = None
        """"services for this provider"""
        self.servicelist = None
        """"state of the network provider"""
        self.state = None

class service:
    def __init__(self):
        """"the service name"""
        self.name = None
        """"the list of capabilities"""
        self.capability = []
        """"can this service capability value can be choosable while creatine network offerings"""
        self.canchooseservicecapability = None
        """"the capability name"""
        self.name = None
        """"the capability value"""
        self.value = None
        """"the service provider name"""
        self.provider = []
        """"uuid of the network provider"""
        self.id = None
        """"true if individual services can be enabled/disabled"""
        self.canenableindividualservice = None
        """"the destination physical network"""
        self.destinationphysicalnetworkid = None
        """"the provider name"""
        self.name = None
        """"the physical network this belongs to"""
        self.physicalnetworkid = None
        """"services for this provider"""
        self.servicelist = None
        """"state of the network provider"""
        self.state = None

