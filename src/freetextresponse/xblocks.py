"""
This is the core logic for the XBlock
"""
from xblock.core import XBlock

from .mixins.scenario import XBlockWorkbenchMixin
from .mixins.user import MissingDataFetcherMixin
from .models import FreeTextResponseModelMixin
from .views import FreeTextResponseViewMixin


@XBlock.needs('i18n')
class FreeTextResponse(
        FreeTextResponseModelMixin,
        FreeTextResponseViewMixin,
        MissingDataFetcherMixin,
        XBlockWorkbenchMixin,
        XBlock,
):
    """
    XBlock to capture a free-text response.
    """
