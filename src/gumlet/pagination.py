# File generated from our OpenAPI spec by Scalar. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional, cast
from typing_extensions import override


from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage
from ._models import construct_type

__all__ = ["SyncPageNumberPage", "AsyncPageNumberPage"]

_T = TypeVar("_T")


def _page_number(value: object) -> Optional[int]:
    """Return an integer page value while rejecting booleans and non-finite numbers."""
    import math

    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value) if math.isfinite(value) else None
    if isinstance(value, str) and value.strip():
        try:
            return int(value)
        except ValueError:
            return None
    return None


def _page_param_number(value: object, default: int) -> Optional[int]:
    return default if value is None else _page_number(value)


class SyncPageNumberPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    all_profiles: List[_T]
    total_profile_count: int
    page_size: int

    @override
    def _get_page_items(self) -> List[_T]:
        all_profiles = self.all_profiles
        if not all_profiles:
            return []
        # The item model is attached by the response post-parser after the page is parsed.
        return [cast(_T, construct_type(value=item, type_=self._model)) for item in all_profiles]

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = _page_param_number(self._options.params.get("page_number"), 1)
        if current_page is None:
            return None

        total_pages = None
        if total_pages is not None and current_page >= total_pages:
            return None

        next_page = current_page + 1
        return PageInfo(params={"page_number": next_page})


class AsyncPageNumberPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    all_profiles: List[_T]
    total_profile_count: int
    page_size: int

    @override
    def _get_page_items(self) -> List[_T]:
        all_profiles = self.all_profiles
        if not all_profiles:
            return []
        # The item model is attached by the response post-parser after the page is parsed.
        return [cast(_T, construct_type(value=item, type_=self._model)) for item in all_profiles]

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = _page_param_number(self._options.params.get("page_number"), 1)
        if current_page is None:
            return None

        total_pages = None
        if total_pages is not None and current_page >= total_pages:
            return None

        next_page = current_page + 1
        return PageInfo(params={"page_number": next_page})
