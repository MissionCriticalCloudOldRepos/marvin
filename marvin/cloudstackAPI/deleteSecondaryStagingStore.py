"""Deletes a secondary staging store ."""
from baseCmd import *
from baseResponse import *


class deleteSecondaryStagingStoreCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """the staging store ID"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id", ]


class deleteSecondaryStagingStoreResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

