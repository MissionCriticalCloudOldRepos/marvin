"""Lists all egress firewall rules for network ID."""
from baseCmd import *
from baseResponse import *


class listEgressFirewallRulesCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """list only resources belonging to the domain specified"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """list resources by display flag; only ROOT admin is eligible to pass this parameter"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """Lists rule with the specified ID."""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """the ID of IP address of the firewall services"""
        self.ipaddressid = None
        self.typeInfo['ipaddressid'] = 'uuid'
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        self.typeInfo['isrecursive'] = 'boolean'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        self.typeInfo['listall'] = 'boolean'
        """the network ID for the egress firewall services"""
        self.networkid = None
        self.typeInfo['networkid'] = 'uuid'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """list objects by project"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        """List resources by tags (key/value pairs)"""
        self.tags = []
        self.typeInfo['tags'] = 'map'
        self.required = []


class listEgressFirewallRulesResponse (baseResponse):
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

