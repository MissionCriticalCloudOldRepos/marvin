"""Updates a Pod."""
from baseCmd import *
from baseResponse import *
class updatePodCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """the ID of the Pod"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """Allocation state of this cluster for allocation of new resources"""
        self.allocationstate = None
        self.typeInfo['allocationstate'] = 'string'
        """the ending IP address for the Pod"""
        self.endip = None
        self.typeInfo['endip'] = 'string'
        """the gateway for the Pod"""
        self.gateway = None
        self.typeInfo['gateway'] = 'string'
        """the name of the Pod"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the netmask of the Pod"""
        self.netmask = None
        self.typeInfo['netmask'] = 'string'
        """the starting IP address for the Pod"""
        self.startip = None
        self.typeInfo['startip'] = 'string'
        self.required = ["id",]

class updatePodResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the ID of the Pod"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the allocation state of the Pod"""
        self.allocationstate = None
        self.typeInfo['allocationstate'] = 'string'
        """the ending IP for the Pod"""
        self.endip = None
        self.typeInfo['endip'] = 'string'
        """the gateway of the Pod"""
        self.gateway = None
        self.typeInfo['gateway'] = 'string'
        """the name of the Pod"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the netmask of the Pod"""
        self.netmask = None
        self.typeInfo['netmask'] = 'string'
        """the starting IP for the Pod"""
        self.startip = None
        self.typeInfo['startip'] = 'string'
        """the Zone ID of the Pod"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'
        """the Zone name of the Pod"""
        self.zonename = None
        self.typeInfo['zonename'] = 'string'
        """the capacity of the Pod"""
        self.capacity = []

class capacity:
    def __init__(self):
        """"the total capacity available"""
        self.capacitytotal = None
        """"the capacity currently in use"""
        self.capacityused = None
        """"the Cluster ID"""
        self.clusterid = None
        """"the Cluster name"""
        self.clustername = None
        """"the percentage of capacity currently in use"""
        self.percentused = None
        """"the Pod ID"""
        self.podid = None
        """"the Pod name"""
        self.podname = None
        """"the capacity type"""
        self.type = None
        """"the Zone ID"""
        self.zoneid = None
        """"the Zone name"""
        self.zonename = None

