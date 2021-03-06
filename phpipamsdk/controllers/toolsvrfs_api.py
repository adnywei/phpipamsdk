""" Tools VRFs Api Calls """

from phpipamsdk.phpipam import PhpIpamApi
from phpipamsdk.phpipam import build_payload


class ToolsVRFsApi(object):
    """ Tools VRFs Api Class """

    _objmap = {
        'id': 'id',
        'name': 'name',
        'rd': 'rd',
        'description': 'description',
        'sections': 'sections'
    }

    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()

    def list_tools_vrfs(self):
        """ get vrf list """
        uri = 'tools/vrfs/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_tools_vrf(self, vrf_id=''):
        """ get vrf list """
        uri = 'tools/vrfs/' + str(vrf_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def list_tools_vrf_subnets(self, vrf_id=''):
        """ get vrf subnet list """
        uri = 'tools/vrfs/' + str(vrf_id) + '/subnets/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def add_tools_vrf(self, name='', **kwargs):
        """ add new tools vrf """
        payload = {
            'name': name
        }
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/vrfs/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result

    def update_tools_vrf(self, vrf_id='', **kwargs):
        """ update tools vrf """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/vrfs/' + str(vrf_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result

    def del_vrf(self, vrf_id=''):
        """ delete tools vrf """
        uri = 'tools/vrfs/' + str(vrf_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
