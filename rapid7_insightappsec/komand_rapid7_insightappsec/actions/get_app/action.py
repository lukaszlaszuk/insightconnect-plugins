import insightconnect_plugin_runtime
from .schema import GetAppInput, GetAppOutput, Input, Output, Component
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Apps
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
from insightconnect_plugin_runtime.exceptions import PluginException
import json


class GetApp(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_app',
                description=Component.DESCRIPTION,
                input=GetAppInput(),
                output=GetAppOutput())

    def run(self, params={}):
        # TODO: Implement run function
        app_id = params.get(Input.APP_ID)
        request = ResourceHelper(self.connection.session, self.logger)

        url = Apps.get_app(self.connection.url,app_id)
        # url = f'{url}{app_id}'

        response = request.resource_request(url, 'get')
        try:
            result = json.loads(response['resource'])
        except (json.decoder.JSONDecodeError, TypeError, KeyError):
            self.logger.error(f'InsightAppSec response: {response}')
            raise PluginException(cause=PluginException.Preset.INVALID_JSON, assistance=PluginException.Preset.INVALID_JSON)

        try:
            output = {'app_name':result['name'], 'app_id':result['id'], 'app_description':result['description'], 'links':result['links']}
        except KeyError:
            self.logger.error(result)
            raise PluginException(cause=PluginException.Preset.INVALID_JSON, assistance=PluginException.Preset.INVALID_JSON)
        return output
