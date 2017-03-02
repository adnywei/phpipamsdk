""" Sections Api Calls """

from ..phpipam import PhpIpamApi

class SectionsApi(object):
    """ Sections Api Class """
    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()
            