import six

from pubnub.endpoints.endpoint import Endpoint
from pubnub.errors import PNERR_GROUP_MISSING
from pubnub.exceptions import PubNubException
from pubnub.enums import HttpMethod, PNOperationType
from pubnub.models.consumer.channel_group import PNChannelGroupsRemoveGroupResult


class RemoveChannelGroup(Endpoint):
    # /v1/channel-registration/sub-key/<sub_key>/channel-group/<group_name>/remove
    REMOVE_PATH = "/v1/channel-registration/sub-key/%s/channel-group/%s/remove"

    def __init__(self, pubnub):
        Endpoint.__init__(self, pubnub)
        self._channel_group = None

    def channel_group(self, channel_group):
        self._channel_group = channel_group

        return self

    def build_params(self):
        return self.default_params()

    def build_path(self):
            return RemoveChannelGroup.REMOVE_PATH % (
                self.pubnub.config.subscribe_key, self._channel_group)

    def http_method(self):
        return HttpMethod.GET

    def validate_params(self):
        self.validate_subscribe_key()

        if not isinstance(self._channel_group, six.string_types)\
                or len(self._channel_group) == 0:
            raise PubNubException(pn_error=PNERR_GROUP_MISSING)

    def create_response(self, envelope):
        return PNChannelGroupsRemoveGroupResult()

    def operation_type(self):
        return PNOperationType.PNRemoveGroupOperation

    def name(self):
        return "RemoveChannelGroup"
