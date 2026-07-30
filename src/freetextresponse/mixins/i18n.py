"""
Mixin i18n logic
"""


class I18nXBlockMixin(object):
    """
    Make an XBlock translation-aware
    """

    def _i18n_service(self):
        """
        Provide the XBlock runtime's i18n service
        """
        service = self.runtime.service(self, 'i18n')
        return service

    def gettext(self, text):
        """
        Call gettext from the XBlock i18n service
        """
        text = self._i18n_service().gettext(text)
        return text

    def ngettext(self, *args, **kwargs):
        """
        Call ngettext from the XBlock i18n service
        """
        text = self._i18n_service().ngettext(*args, **kwargs)
        return text
