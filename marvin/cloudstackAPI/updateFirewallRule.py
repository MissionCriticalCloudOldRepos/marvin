"""Updates firewall rule"""
from baseCmd import *
from baseResponse import *


class updateFirewallRuleCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the ID of the firewall rule"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """an optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only"""
        self.customid = None
        self.typeInfo['customid'] = 'string'
        """an optional field, whether to the display the rule to the end user or not"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        self.required = ["id", ]


class updateFirewallRuleResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the firewall rule"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the cidr list to forward traffic from"""
        self.cidrlist = None
        self.typeInfo['cidrlist'] = 'string'
        """the ending port of firewall rule's port range"""
        self.endport = None
        self.typeInfo['endport'] = 'integer'
        """is rule for display to the regular user"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """error code for this icmp message"""
        self.icmpcode = None
        self.typeInfo['icmpcode'] = 'integer'
        """type of the icmp message being sent"""
        self.icmptype = None
        self.typeInfo['icmptype'] = 'integer'
        """the public ip address for the firewall rule"""
        self.ipaddress = None
        self.typeInfo['ipaddress'] = 'string'
        """the public ip address id for the firewall rule"""
        self.ipaddressid = None
        self.typeInfo['ipaddressid'] = 'string'
        """the network id of the firewall rule"""
        self.networkid = None
        self.typeInfo['networkid'] = 'string'
        """the protocol of the firewall rule"""
        self.protocol = None
        self.typeInfo['protocol'] = 'string'
        """the starting port of firewall rule's port range"""
        self.startport = None
        self.typeInfo['startport'] = 'integer'
        """the state of the rule"""
        self.state = None
        self.typeInfo['state'] = 'string'
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

