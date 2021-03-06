"""Updates ACL item with specified ID"""
from baseCmd import *
from baseResponse import *


class updateNetworkACLItemCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the ID of the network ACL item"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """scl entry action, allow or deny"""
        self.action = None
        self.typeInfo['action'] = 'string'
        """the cidr list to allow traffic from/to"""
        self.cidrlist = []
        self.typeInfo['cidrlist'] = 'list'
        """an optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only"""
        self.customid = None
        self.typeInfo['customid'] = 'string'
        """the ending port of ACL"""
        self.endport = None
        self.typeInfo['endport'] = 'integer'
        """an optional field, whether to the display the rule to the end user or not"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """error code for this ICMP message"""
        self.icmpcode = None
        self.typeInfo['icmpcode'] = 'integer'
        """type of the ICMP message being sent"""
        self.icmptype = None
        self.typeInfo['icmptype'] = 'integer'
        """The network of the vm the ACL will be created for"""
        self.number = None
        self.typeInfo['number'] = 'integer'
        """the protocol for the ACL rule. Valid values are TCP/UDP/ICMP/ALL or valid protocol number"""
        self.protocol = None
        self.typeInfo['protocol'] = 'string'
        """the starting port of ACL"""
        self.startport = None
        self.typeInfo['startport'] = 'integer'
        """the traffic type for the ACL,can be Ingress or Egress, defaulted to Ingress if not specified"""
        self.traffictype = None
        self.typeInfo['traffictype'] = 'string'
        self.required = ["id", ]


class updateNetworkACLItemResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the ACL Item"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the ID of the ACL this item belongs to"""
        self.aclid = None
        self.typeInfo['aclid'] = 'string'
        """Action of ACL Item. Allow/Deny"""
        self.action = None
        self.typeInfo['action'] = 'string'
        """the cidr list to forward traffic from"""
        self.cidrlist = None
        self.typeInfo['cidrlist'] = 'string'
        """the ending port of ACL's port range"""
        self.endport = None
        self.typeInfo['endport'] = 'string'
        """is rule for display to the regular user"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """error code for this icmp message"""
        self.icmpcode = None
        self.typeInfo['icmpcode'] = 'integer'
        """type of the icmp message being sent"""
        self.icmptype = None
        self.typeInfo['icmptype'] = 'integer'
        """Number of the ACL Item"""
        self.number = None
        self.typeInfo['number'] = 'integer'
        """the protocol of the ACL"""
        self.protocol = None
        self.typeInfo['protocol'] = 'string'
        """the starting port of ACL's port range"""
        self.startport = None
        self.typeInfo['startport'] = 'string'
        """the state of the rule"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """the traffic type for the ACL"""
        self.traffictype = None
        self.typeInfo['traffictype'] = 'string'
        """the list of resource tags associated with the network ACLs"""
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

