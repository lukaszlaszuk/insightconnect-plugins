import insightconnect_plugin_runtime
from .schema import DAddInput, DAddOutput, Input, Output, Component
# Custom imports below


class DAdd(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='dAdd',
                description=Component.DESCRIPTION,
                input=DAddInput(),
                output=DAddOutput())

    def run(self, params={}):
        payload = params.get(Input.PAYLOAD)
        destinations = []

        for i in payload:
            destination = i.get('destination')
            i["destination"] = destination

            # Comment is optional so if NOT none,
            # then add comment under key 'comment'
            comment = i.get('comment')
            if comment:
                i['comment'] = comment
            destinations.append(i)

        try:
            dictIds = self.connection.client.create_destinations(destinations)
        except Exception:
            self.logger.error("AddDestination: run: Problem with request")
            raise Exception("AddDestination: run: Problem with request")


        # return {Output.SUCCESS: self.connection.client.create_destinations(destinations)}
        # return {"success": "Destination successfully added!"}
