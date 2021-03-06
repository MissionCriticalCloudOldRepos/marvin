"""Updates a port forwarding rule. Only the private port and the virtual machine can be updated."""
from baseCmd import *
from baseResponse import *


class updatePortForwardingRuleCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the ID of the port forwarding rule"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """an optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only"""
        self.customid = None
        self.typeInfo['customid'] = 'string'
        """an optional field, whether to the display the rule to the end user or not"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """the private port of the port forwarding rule"""
        self.privateport = None
        self.typeInfo['privateport'] = 'integer'
        """the ID of the virtual machine for the port forwarding rule"""
        self.virtualmachineid = None
        self.typeInfo['virtualmachineid'] = 'uuid'
        """VM guest nic Secondary ip address for the port forwarding rule"""
        self.vmguestip = None
        self.typeInfo['vmguestip'] = 'string'
        self.required = ["id", ]


class updatePortForwardingRuleResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the port forwarding rule"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the cidr list to forward traffic from"""
        self.cidrlist = None
        self.typeInfo['cidrlist'] = 'string'
        """is firewall for display to the regular user"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """the public ip address for the port forwarding rule"""
        self.ipaddress = None
        self.typeInfo['ipaddress'] = 'string'
        """the public ip address id for the port forwarding rule"""
        self.ipaddressid = None
        self.typeInfo['ipaddressid'] = 'string'
        """the id of the guest network the port forwarding rule belongs to"""
        self.networkid = None
        self.typeInfo['networkid'] = 'string'
        """the ending port of port forwarding rule's private port range"""
        self.privateendport = None
        self.typeInfo['privateendport'] = 'string'
        """the starting port of port forwarding rule's private port range"""
        self.privateport = None
        self.typeInfo['privateport'] = 'string'
        """the protocol of the port forwarding rule"""
        self.protocol = None
        self.typeInfo['protocol'] = 'string'
        """the ending port of port forwarding rule's private port range"""
        self.publicendport = None
        self.typeInfo['publicendport'] = 'string'
        """the starting port of port forwarding rule's public port range"""
        self.publicport = None
        self.typeInfo['publicport'] = 'string'
        """the state of the rule"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """the VM display name for the port forwarding rule"""
        self.virtualmachinedisplayname = None
        self.typeInfo['virtualmachinedisplayname'] = 'string'
        """the VM ID for the port forwarding rule"""
        self.virtualmachineid = None
        self.typeInfo['virtualmachineid'] = 'string'
        """the VM name for the port forwarding rule"""
        self.virtualmachinename = None
        self.typeInfo['virtualmachinename'] = 'string'
        """the vm ip address for the port forwarding rule"""
        self.vmguestip = None
        self.typeInfo['vmguestip'] = 'string'
        """the list of resource tags associated with the rule"""
        self.tags = []

class tags:
    def __init__(self):
        """"the account associated with the tag"""
        self.account = None
        """"customer associated with the tag"""
        self.customer = None
        """"the domain associated with the tag"""
        self.domain = None
        """"the ID of the domain associated with the tag"""
        self.domainid = None
        """"tag key name"""
        self.key = None
        """"the project name where tag belongs to"""
        self.project = None
        """"the project id the tag belongs to"""
        self.projectid = None
        """"id of the resource"""
        self.resourceid = None
        """"resource type"""
        self.resourcetype = None
        """"tag value"""
        self.value = None

