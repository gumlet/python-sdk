# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional, Union
from typing_extensions import overload
from .._types import SequenceNotStr

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform, required_args
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.folder_create_response import FolderCreateResponse
from ..types import folder_create_params, folder_list_params, folder_update_params, folder_delete_assets_params
from ..types.folder_list_response import FolderListResponse
from ..types.folder_retrieve_response import FolderRetrieveResponse
from ..types.folder_update_response import FolderUpdateResponse
from ..types.folder_delete_response import FolderDeleteResponse
from ..types.folder_delete_assets_response import FolderDeleteAssetsResponse

__all__ = ["FoldersResource", "AsyncFoldersResource"]


class FoldersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FoldersResourceWithRawResponse:
        return FoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FoldersResourceWithStreamingResponse:
        return FoldersResourceWithStreamingResponse(self)

    def create(
        self,
        workspace_id: str,
        *,
        name: str,
        parent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderCreateResponse:
        """
        Create a folder inside a video workspace. Optionally provide `parent_id` to create a nested folder.

        Args:
            workspace_id: Video workspace id.
            name: Folder name.
            parent_id: Parent folder id. Send `null` or omit it to create a root-level folder.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderCreateResponse: 200

        Example:
            ```python
            folder = client.folders.create(
                workspace_id="workspaceId",
                name="Course Assets",
                parent_id="",
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            path_template("/video/workspaces/{workspace_id}/folders", **{"workspace_id": workspace_id}),
            body=maybe_transform(
                {
                    "name": name,
                    "parent_id": parent_id,
                },
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderCreateResponse,
        )

    def list(
        self,
        workspace_id: str,
        *,
        parent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderListResponse:
        """
        List folders for a video workspace. Use `parent_id` to list only folders inside a specific parent folder.

        Args:
            workspace_id: Video workspace id.
            parent_id: Parent folder id. Send `null` to list root folders.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderListResponse: 200

        Example:
            ```python
            folder = client.folders.list(
                workspace_id="workspaceId",
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get(
            path_template("/video/workspaces/{workspace_id}/folders", **{"workspace_id": workspace_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"parent_id": parent_id}, folder_list_params.FolderListParams),
            ),
            cast_to=FolderListResponse,
        )

    def retrieve(
        self,
        folder_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderRetrieveResponse:
        """
        Get a single folder by id.

        Args:
            folder_id: Folder id.
            workspace_id: Video workspace id.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderRetrieveResponse: 200

        Example:
            ```python
            folder = client.folders.retrieve(
                workspace_id="workspaceId",
                folder_id="folderId",
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if folder_id is None or (isinstance(folder_id, str) and not folder_id):
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._get(
            path_template(
                "/video/workspaces/{workspace_id}/folders/{folder_id}",
                **{"workspace_id": workspace_id, "folder_id": folder_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderRetrieveResponse,
        )

    @overload
    def update(
        self,
        folder_id: str,
        *,
        workspace_id: str,
        name: str,
        parent_id: Optional[str] | Omit = omit,
        asset_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderUpdateResponse: ...

    @overload
    def update(
        self,
        folder_id: str,
        *,
        workspace_id: str,
        name: str | Omit = omit,
        parent_id: str | Omit = omit,
        asset_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderUpdateResponse: ...

    @required_args(["name"], ["asset_ids"])
    def update(
        self,
        folder_id: str,
        *,
        workspace_id: str,
        name: str | Omit = omit,
        parent_id: Union[Optional[str], str] | Omit = omit,
        asset_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderUpdateResponse:
        """
        Rename a folder, move it to another parent folder, or move assets into the folder by sending `asset_ids`.

        Args:
            folder_id: Folder id.
            workspace_id: Video workspace id.
            name: New folder name.
            parent_id: New parent folder id. Send `null` to move the folder to the root level.
            asset_ids: Asset ids to move into this folder.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderUpdateResponse: 200

        Example:
            ```python
            folder = client.folders.update(
                workspace_id="workspaceId",
                folder_id="folderId",
                name="Course Assets Updated",
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if folder_id is None or (isinstance(folder_id, str) and not folder_id):
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._post(
            path_template(
                "/video/workspaces/{workspace_id}/folders/{folder_id}",
                **{"workspace_id": workspace_id, "folder_id": folder_id},
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "parent_id": parent_id,
                    "asset_ids": asset_ids,
                },
                folder_update_params.FolderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderUpdateResponse,
        )

    def delete(
        self,
        folder_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderDeleteResponse:
        """
        Delete a folder. Descendant folders and assets inside them are deleted by the backend workflow.

        Args:
            folder_id: Folder id.
            workspace_id: Video workspace id.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderDeleteResponse: 200

        Example:
            ```python
            folder = client.folders.delete(
                workspace_id="workspaceId",
                folder_id="folderId",
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if folder_id is None or (isinstance(folder_id, str) and not folder_id):
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._delete(
            path_template(
                "/video/workspaces/{workspace_id}/folders/{folder_id}",
                **{"workspace_id": workspace_id, "folder_id": folder_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderDeleteResponse,
        )

    def delete_assets(
        self,
        workspace_id: str,
        *,
        asset_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderDeleteAssetsResponse:
        """
        Remove one or more assets from their current folder assignment inside the workspace.

        Args:
            workspace_id: Video workspace id.
            asset_ids: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderDeleteAssetsResponse: 200

        Example:
            ```python
            folder = client.folders.delete_assets(
                workspace_id="workspaceId",
                asset_ids=["67e4f2b4403562dbea654301", "67e4f2bb403562dbea654302"],
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            path_template(
                "/video/workspaces/{workspace_id}/remove-assets-from-folder", **{"workspace_id": workspace_id}
            ),
            body=maybe_transform(
                {"asset_ids": asset_ids},
                folder_delete_assets_params.FolderDeleteAssetsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderDeleteAssetsResponse,
        )


class AsyncFoldersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFoldersResourceWithRawResponse:
        return AsyncFoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFoldersResourceWithStreamingResponse:
        return AsyncFoldersResourceWithStreamingResponse(self)

    async def create(
        self,
        workspace_id: str,
        *,
        name: str,
        parent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderCreateResponse:
        """
        Create a folder inside a video workspace. Optionally provide `parent_id` to create a nested folder.

        Args:
            workspace_id: Video workspace id.
            name: Folder name.
            parent_id: Parent folder id. Send `null` or omit it to create a root-level folder.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderCreateResponse: 200

        Example:
            ```python
            folder = await client.folders.create(
                workspace_id="workspaceId",
                name="Course Assets",
                parent_id="",
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            path_template("/video/workspaces/{workspace_id}/folders", **{"workspace_id": workspace_id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parent_id": parent_id,
                },
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderCreateResponse,
        )

    async def list(
        self,
        workspace_id: str,
        *,
        parent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderListResponse:
        """
        List folders for a video workspace. Use `parent_id` to list only folders inside a specific parent folder.

        Args:
            workspace_id: Video workspace id.
            parent_id: Parent folder id. Send `null` to list root folders.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderListResponse: 200

        Example:
            ```python
            folder = await client.folders.list(
                workspace_id="workspaceId",
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._get(
            path_template("/video/workspaces/{workspace_id}/folders", **{"workspace_id": workspace_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"parent_id": parent_id}, folder_list_params.FolderListParams),
            ),
            cast_to=FolderListResponse,
        )

    async def retrieve(
        self,
        folder_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderRetrieveResponse:
        """
        Get a single folder by id.

        Args:
            folder_id: Folder id.
            workspace_id: Video workspace id.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderRetrieveResponse: 200

        Example:
            ```python
            folder = await client.folders.retrieve(
                workspace_id="workspaceId",
                folder_id="folderId",
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if folder_id is None or (isinstance(folder_id, str) and not folder_id):
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._get(
            path_template(
                "/video/workspaces/{workspace_id}/folders/{folder_id}",
                **{"workspace_id": workspace_id, "folder_id": folder_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderRetrieveResponse,
        )

    @overload
    async def update(
        self,
        folder_id: str,
        *,
        workspace_id: str,
        name: str,
        parent_id: Optional[str] | Omit = omit,
        asset_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderUpdateResponse: ...

    @overload
    async def update(
        self,
        folder_id: str,
        *,
        workspace_id: str,
        name: str | Omit = omit,
        parent_id: str | Omit = omit,
        asset_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderUpdateResponse: ...

    @required_args(["name"], ["asset_ids"])
    async def update(
        self,
        folder_id: str,
        *,
        workspace_id: str,
        name: str | Omit = omit,
        parent_id: Union[Optional[str], str] | Omit = omit,
        asset_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderUpdateResponse:
        """
        Rename a folder, move it to another parent folder, or move assets into the folder by sending `asset_ids`.

        Args:
            folder_id: Folder id.
            workspace_id: Video workspace id.
            name: New folder name.
            parent_id: New parent folder id. Send `null` to move the folder to the root level.
            asset_ids: Asset ids to move into this folder.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderUpdateResponse: 200

        Example:
            ```python
            folder = await client.folders.update(
                workspace_id="workspaceId",
                folder_id="folderId",
                name="Course Assets Updated",
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if folder_id is None or (isinstance(folder_id, str) and not folder_id):
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._post(
            path_template(
                "/video/workspaces/{workspace_id}/folders/{folder_id}",
                **{"workspace_id": workspace_id, "folder_id": folder_id},
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parent_id": parent_id,
                    "asset_ids": asset_ids,
                },
                folder_update_params.FolderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderUpdateResponse,
        )

    async def delete(
        self,
        folder_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderDeleteResponse:
        """
        Delete a folder. Descendant folders and assets inside them are deleted by the backend workflow.

        Args:
            folder_id: Folder id.
            workspace_id: Video workspace id.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderDeleteResponse: 200

        Example:
            ```python
            folder = await client.folders.delete(
                workspace_id="workspaceId",
                folder_id="folderId",
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if folder_id is None or (isinstance(folder_id, str) and not folder_id):
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._delete(
            path_template(
                "/video/workspaces/{workspace_id}/folders/{folder_id}",
                **{"workspace_id": workspace_id, "folder_id": folder_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderDeleteResponse,
        )

    async def delete_assets(
        self,
        workspace_id: str,
        *,
        asset_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderDeleteAssetsResponse:
        """
        Remove one or more assets from their current folder assignment inside the workspace.

        Args:
            workspace_id: Video workspace id.
            asset_ids: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderDeleteAssetsResponse: 200

        Example:
            ```python
            folder = await client.folders.delete_assets(
                workspace_id="workspaceId",
                asset_ids=["67e4f2b4403562dbea654301", "67e4f2bb403562dbea654302"],
            )
            ```
        """
        if workspace_id is None or (isinstance(workspace_id, str) and not workspace_id):
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            path_template(
                "/video/workspaces/{workspace_id}/remove-assets-from-folder", **{"workspace_id": workspace_id}
            ),
            body=await async_maybe_transform(
                {"asset_ids": asset_ids},
                folder_delete_assets_params.FolderDeleteAssetsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderDeleteAssetsResponse,
        )


class FoldersResourceWithRawResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.create = to_raw_response_wrapper(
            folders.create,
        )
        self.list = to_raw_response_wrapper(
            folders.list,
        )
        self.retrieve = to_raw_response_wrapper(
            folders.retrieve,
        )
        self.update = to_raw_response_wrapper(
            folders.update,
        )
        self.delete = to_raw_response_wrapper(
            folders.delete,
        )
        self.delete_assets = to_raw_response_wrapper(
            folders.delete_assets,
        )


class AsyncFoldersResourceWithRawResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.create = async_to_raw_response_wrapper(
            folders.create,
        )
        self.list = async_to_raw_response_wrapper(
            folders.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            folders.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            folders.update,
        )
        self.delete = async_to_raw_response_wrapper(
            folders.delete,
        )
        self.delete_assets = async_to_raw_response_wrapper(
            folders.delete_assets,
        )


class FoldersResourceWithStreamingResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.create = to_streamed_response_wrapper(
            folders.create,
        )
        self.list = to_streamed_response_wrapper(
            folders.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            folders.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            folders.update,
        )
        self.delete = to_streamed_response_wrapper(
            folders.delete,
        )
        self.delete_assets = to_streamed_response_wrapper(
            folders.delete_assets,
        )


class AsyncFoldersResourceWithStreamingResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.create = async_to_streamed_response_wrapper(
            folders.create,
        )
        self.list = async_to_streamed_response_wrapper(
            folders.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            folders.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            folders.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            folders.delete,
        )
        self.delete_assets = async_to_streamed_response_wrapper(
            folders.delete_assets,
        )
