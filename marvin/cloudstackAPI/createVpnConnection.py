"""Create site to site vpn connection"""
from baseCmd import *
from baseResponse import *


class createVpnConnectionCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """id of the customer gateway"""
        """Required"""
        self.s2scustomergatewayid = None
        self.typeInfo['s2scustomergatewayid'] = 'uuid'
        """id of the vpn gateway"""
        """Required"""
        self.s2svpngatewayid = None
        self.typeInfo['s2svpngatewayid'] = 'uuid'
        """an optional field, whether to the display the vpn to the end user or not"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """connection is passive or not"""
        self.passive = None
        self.typeInfo['passive'] = 'boolean'
        self.required = ["s2scustomergatewayid", "s2svpngatewayid", ]


class createVpnConnectionResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the connection ID"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the owner"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """guest cidr list of the customer gateway"""
        self.cidrlist = None
        self.typeInfo['cidrlist'] = 'string'
        """the date and time the host was created"""
        self.created = None
        self.typeInfo['created'] = 'date'
        """the domain name of the owner"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain id of the owner"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """if DPD is enabled for customer gateway"""
        self.dpd = None
        self.typeInfo['dpd'] = 'boolean'
        """Lifetime of ESP SA of customer gateway"""
        self.esplifetime = None
        self.typeInfo['esplifetime'] = 'long'
        """ESP policy of the customer gateway"""
        self.esppolicy = None
        self.typeInfo['esppolicy'] = 'string'
        """if Force NAT Encapsulation is enabled for customer gateway"""
        self.forceencap = None
        self.typeInfo['forceencap'] = 'boolean'
        """is connection for display to the regular user"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """public ip address id of the customer gateway"""
        self.gateway = None
        self.typeInfo['gateway'] = 'string'
        """Lifetime of IKE SA of customer gateway"""
        self.ikelifetime = None
        self.typeInfo['ikelifetime'] = 'long'
        """IKE policy of the customer gateway"""
        self.ikepolicy = None
        self.typeInfo['ikepolicy'] = 'string'
        """IPsec Preshared-Key of the customer gateway"""
        self.ipsecpsk = None
        self.typeInfo['ipsecpsk'] = 'string'
        """State of vpn connection"""
        self.passive = None
        self.typeInfo['passive'] = 'boolean'
        """the project name"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """the public IP address"""
        self.publicip = None
        self.typeInfo['publicip'] = 'string'
        """the date and time the host was removed"""
        self.removed = None
        self.typeInfo['removed'] = 'date'
        """the customer gateway ID"""
        self.s2scustomergatewayid = None
        self.typeInfo['s2scustomergatewayid'] = 'string'
        """the vpn gateway ID"""
        self.s2svpngatewayid = None
        self.typeInfo['s2svpngatewayid'] = 'string'
        """State of vpn connection"""
        self.state = None
        self.typeInfo['state'] = 'string'

