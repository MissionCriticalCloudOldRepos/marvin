"""Lists accounts and provides detailed account information for listed accounts"""
from baseCmd import *
from baseResponse import *


class listAccountsCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """list accounts by account type. Valid account types are 1 (admin), 2 (domain-admin), and 0 (user)."""
        self.accounttype = None
        self.typeInfo['accounttype'] = 'long'
        """list only resources belonging to the domain specified"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """list account by account ID"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """list accounts by cleanuprequired attribute (values are true or false)"""
        self.iscleanuprequired = None
        self.typeInfo['iscleanuprequired'] = 'boolean'
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        self.typeInfo['isrecursive'] = 'boolean'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        self.typeInfo['listall'] = 'boolean'
        """list account by account name"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """list accounts by state. Valid states are enabled, disabled, and locked."""
        self.state = None
        self.typeInfo['state'] = 'string'
        self.required = []


class listAccountsResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the id of the account"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """details for the account"""
        self.accountdetails = None
        self.typeInfo['accountdetails'] = 'map'
        """account type (admin, domain-admin, user)"""
        self.accounttype = None
        self.typeInfo['accounttype'] = 'short'
        """the total number of cpu cores available to be created for this account"""
        self.cpuavailable = None
        self.typeInfo['cpuavailable'] = 'string'
        """the total number of cpu cores the account can own"""
        self.cpulimit = None
        self.typeInfo['cpulimit'] = 'string'
        """the total number of cpu cores owned by account"""
        self.cputotal = None
        self.typeInfo['cputotal'] = 'long'
        """the default zone of the account"""
        self.defaultzoneid = None
        self.typeInfo['defaultzoneid'] = 'string'
        """name of the Domain the account belongs too"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """id of the Domain the account belongs too"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """the total number of public ip addresses available for this account to acquire"""
        self.ipavailable = None
        self.typeInfo['ipavailable'] = 'string'
        """the total number of public ip addresses this account can acquire"""
        self.iplimit = None
        self.typeInfo['iplimit'] = 'string'
        """the total number of public ip addresses allocated for this account"""
        self.iptotal = None
        self.typeInfo['iptotal'] = 'long'
        """true if the account requires cleanup"""
        self.iscleanuprequired = None
        self.typeInfo['iscleanuprequired'] = 'boolean'
        """true if account is default, false otherwise"""
        self.isdefault = None
        self.typeInfo['isdefault'] = 'boolean'
        """the total memory (in MB) available to be created for this account"""
        self.memoryavailable = None
        self.typeInfo['memoryavailable'] = 'string'
        """the total memory (in MB) the account can own"""
        self.memorylimit = None
        self.typeInfo['memorylimit'] = 'string'
        """the total memory (in MB) owned by account"""
        self.memorytotal = None
        self.typeInfo['memorytotal'] = 'long'
        """the name of the account"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the total number of networks available to be created for this account"""
        self.networkavailable = None
        self.typeInfo['networkavailable'] = 'string'
        """the network domain"""
        self.networkdomain = None
        self.typeInfo['networkdomain'] = 'string'
        """the total number of networks the account can own"""
        self.networklimit = None
        self.typeInfo['networklimit'] = 'string'
        """the total number of networks owned by account"""
        self.networktotal = None
        self.typeInfo['networktotal'] = 'long'
        """the total primary storage space (in GiB) available to be used for this account"""
        self.primarystorageavailable = None
        self.typeInfo['primarystorageavailable'] = 'string'
        """the total primary storage space (in GiB) the account can own"""
        self.primarystoragelimit = None
        self.typeInfo['primarystoragelimit'] = 'string'
        """the total primary storage space (in GiB) owned by account"""
        self.primarystoragetotal = None
        self.typeInfo['primarystoragetotal'] = 'long'
        """the total number of projects available for administration by this account"""
        self.projectavailable = None
        self.typeInfo['projectavailable'] = 'string'
        """the total number of projects the account can own"""
        self.projectlimit = None
        self.typeInfo['projectlimit'] = 'string'
        """the total number of projects being administrated by this account"""
        self.projecttotal = None
        self.typeInfo['projecttotal'] = 'long'
        """the total number of network traffic bytes received"""
        self.receivedbytes = None
        self.typeInfo['receivedbytes'] = 'long'
        """the total secondary storage space (in GiB) available to be used for this account"""
        self.secondarystorageavailable = None
        self.typeInfo['secondarystorageavailable'] = 'string'
        """the total secondary storage space (in GiB) the account can own"""
        self.secondarystoragelimit = None
        self.typeInfo['secondarystoragelimit'] = 'string'
        """the total secondary storage space (in GiB) owned by account"""
        self.secondarystoragetotal = None
        self.typeInfo['secondarystoragetotal'] = 'long'
        """the total number of network traffic bytes sent"""
        self.sentbytes = None
        self.typeInfo['sentbytes'] = 'long'
        """the total number of snapshots available for this account"""
        self.snapshotavailable = None
        self.typeInfo['snapshotavailable'] = 'string'
        """the total number of snapshots which can be stored by this account"""
        self.snapshotlimit = None
        self.typeInfo['snapshotlimit'] = 'string'
        """the total number of snapshots stored by this account"""
        self.snapshottotal = None
        self.typeInfo['snapshottotal'] = 'long'
        """the state of the account"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """the total number of templates available to be created by this account"""
        self.templateavailable = None
        self.typeInfo['templateavailable'] = 'string'
        """the total number of templates which can be created by this account"""
        self.templatelimit = None
        self.typeInfo['templatelimit'] = 'string'
        """the total number of templates which have been created by this account"""
        self.templatetotal = None
        self.typeInfo['templatetotal'] = 'long'
        """the total number of virtual machines available for this account to acquire"""
        self.vmavailable = None
        self.typeInfo['vmavailable'] = 'string'
        """the total number of virtual machines that can be deployed by this account"""
        self.vmlimit = None
        self.typeInfo['vmlimit'] = 'string'
        """the total number of virtual machines running for this account"""
        self.vmrunning = None
        self.typeInfo['vmrunning'] = 'integer'
        """the total number of virtual machines stopped for this account"""
        self.vmstopped = None
        self.typeInfo['vmstopped'] = 'integer'
        """the total number of virtual machines deployed by this account"""
        self.vmtotal = None
        self.typeInfo['vmtotal'] = 'long'
        """the total volume available for this account"""
        self.volumeavailable = None
        self.typeInfo['volumeavailable'] = 'string'
        """the total volume which can be used by this account"""
        self.volumelimit = None
        self.typeInfo['volumelimit'] = 'string'
        """the total volume being used by this account"""
        self.volumetotal = None
        self.typeInfo['volumetotal'] = 'long'
        """the total number of vpcs available to be created for this account"""
        self.vpcavailable = None
        self.typeInfo['vpcavailable'] = 'string'
        """the total number of vpcs the account can own"""
        self.vpclimit = None
        self.typeInfo['vpclimit'] = 'string'
        """the total number of vpcs owned by account"""
        self.vpctotal = None
        self.typeInfo['vpctotal'] = 'long'
        """the list of users associated with account"""
        self.user = []

class user:
    def __init__(self):
        """"the user ID"""
        self.id = None
        """"the account name of the user"""
        self.account = None
        """"the account ID of the user"""
        self.accountid = None
        """"the account type of the user"""
        self.accounttype = None
        """"the api key of the user"""
        self.apikey = None
        """"the date and time the user account was created"""
        self.created = None
        """"the domain name of the user"""
        self.domain = None
        """"the domain ID of the user"""
        self.domainid = None
        """"the user email address"""
        self.email = None
        """"the user firstname"""
        self.firstname = None
        """"the boolean value representing if the updating target is in caller's child domain"""
        self.iscallerchilddomain = None
        """"true if user is default, false otherwise"""
        self.isdefault = None
        """"the user lastname"""
        self.lastname = None
        """"the secret key of the user"""
        self.secretkey = None
        """"the user state"""
        self.state = None
        """"the timezone user was created in"""
        self.timezone = None
        """"the user name"""
        self.username = None

