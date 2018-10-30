
from django.utils.translation import ugettext_lazy as _

from temba.contacts.models import APPLE_BUSINESS_CHAT_SCHEME

from ...models import ChannelType
from .views import ClaimView


class AppleChatType(ChannelType):
    """
    An Apple Business Chat channel (https://developer.apple.com/documentation/businesschat)
    """

    code = "ABC"
    category = ChannelType.Category.API

    courier_url = r"^abc/(?P<uuid>[a-z0-9\-]+)/receive$"



    name = "Apple Business Chat"
    icon = "icon-fcm"

    claim_blurb = _(
        """Connect your approved <a href="https://developer.apple.com/documentation/businesschat/" target="_blank"> Apple Business Chat</a> app"""
    )
    claim_view = ClaimView

    schemes = [APPLE_BUSINESS_CHAT_SCHEME]
    attachment_support = True
    free_sending = True
    # TODO: determine the actual max text size
    max_length = 10000
    # quick_reply_text_size = 36

    configuration_blurb = _(
        """
        To use your Apple Business Chat channel you'll have to configure the Apple Business Chat server to direct messages to the url below.
        """
    )

    configuration_urls = (
        dict(
            label=_("Receive URL"),
            url="https://{{ channel.callback_domain }}{% url 'courier.abc' channel.uuid %}",
            description=_(
                "To handle incoming messages, refer to the Business Chat server in the Apple documentation."
            ),
        ),
    )
