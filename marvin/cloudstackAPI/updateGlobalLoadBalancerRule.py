"""update global load balancer rules."""
from baseCmd import *
from baseResponse import *


class updateGlobalLoadBalancerRuleCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the ID of the global load balancer rule"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """the description of the load balancer rule"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """load balancer algorithm (roundrobin, leastconn, proximity) that is used to distributed traffic across the zones participating in global server load balancing, if not specified defaults to 'round robin'"""
        self.gslblbmethod = None
        self.typeInfo['gslblbmethod'] = 'string'
        """session sticky method (sourceip) if not specified defaults to sourceip"""
        self.gslbstickysessionmethodname = None
        self.typeInfo['gslbstickysessionmethodname'] = 'string'
        self.required = ["id", ]


class updateGlobalLoadBalancerRuleResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """global load balancer rule ID"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account of the load balancer rule"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the description of the global load balancer rule"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """the domain of the load balancer rule"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID of the load balancer rule"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """DNS domain name given for the global load balancer"""
        self.gslbdomainname = None
        self.typeInfo['gslbdomainname'] = 'string'
        """Load balancing method used for the global load balancer"""
        self.gslblbmethod = None
        self.typeInfo['gslblbmethod'] = 'string'
        """GSLB service type"""
        self.gslbservicetype = None
        self.typeInfo['gslbservicetype'] = 'string'
        """session persistence method used for the global load balancer"""
        self.gslbstickysessionmethodname = None
        self.typeInfo['gslbstickysessionmethodname'] = 'string'
        """name of the global load balancer rule"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the project name of the load balancer"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id of the load balancer"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """Region Id in which global load balancer is created"""
        self.regionid = None
        self.typeInfo['regionid'] = 'integer'
        """List of load balancer rules that are part of GSLB rule"""
        self.loadbalancerrule = []

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

class loadbalancerrule:
    def __init__(self):
        """"the load balancer rule ID"""
        self.id = None
        """"the account of the load balancer rule"""
        self.account = None
        """"the load balancer algorithm (source, roundrobin, leastconn)"""
        self.algorithm = None
        """"the cidr list to forward traffic from"""
        self.cidrlist = None
        """"the HAProxy client_timeout setting for this load balancing rule."""
        self.clienttimeout = None
        """"the description of the load balancer"""
        self.description = None
        """"the domain of the load balancer rule"""
        self.domain = None
        """"the domain ID of the load balancer rule"""
        self.domainid = None
        """"is rule for display to the regular user"""
        self.fordisplay = None
        """"the name of the load balancer"""
        self.name = None
        """"the id of the guest network the lb rule belongs to"""
        self.networkid = None
        """"the private port"""
        self.privateport = None
        """"the project name of the load balancer"""
        self.project = None
        """"the project id of the load balancer"""
        self.projectid = None
        """"the protocol of the loadbalanacer rule"""
        self.protocol = None
        """"the public ip address"""
        self.publicip = None
        """"the public ip address id"""
        self.publicipid = None
        """"the public port"""
        self.publicport = None
        """"the HAProxy server_timeout setting for this load balancing rule."""
        self.servertimeout = None
        """"the state of the rule"""
        self.state = None
        """"the id of the zone the rule belongs to"""
        self.zoneid = None
        """"the list of resource tags associated with load balancer"""
        self.tags = []
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

