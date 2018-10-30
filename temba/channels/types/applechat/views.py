

from smartmin.views import SmartFormView

from django import forms
from django.utils.translation import ugettext_lazy as _

from ...models import Channel
from ...views import ClaimViewMixin


class ClaimView(ClaimViewMixin, SmartFormView):
    class Form(ClaimViewMixin.Form):
        title = forms.CharField(required=True, label=_("Apple Business Chat Environment Title"), help_text=_("The name of your environment"))

        business_id = forms.CharField(
            required=True, label=_("Apple Business ID"), help_text=_("The business id provided by Apple.")
        )
        csp_id = forms.CharField(
            required=True, label=_("Apple CSP ID"), help_text=_("The CSP id provided by Apple.")
        )
        secret_key = forms.CharField(
            required=True,
            label=_("Apple Secret Key"),
            help_text=_("The secret key provided by apple"),
        )

    form_class = Form

    def form_valid(self, form):
        org = self.request.user.get_org()

        title = form.cleaned_data.get("title")
        business_id = form.cleaned_data.get("business_id")
        secret_key = form.cleaned_data.get("secret_key")
        csp_id = form.cleaned_data.get("csp_id")
        config = {
            Channel.CONFIG_API_KEY: secret_key,
            Channel.CONFIG_APPLE_BUSINESS_ID: business_id,
            Channel.CONFIG_APPLE_BUSINESS_CHAT_CSP_ID: csp_id,
        }

        self.object = Channel.create(
            org, self.request.user, None, self.channel_type, name=title, address=business_id, config=config
        )

        return super().form_valid(form)
