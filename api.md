# Gumlet Python API

Complete reference of every operation, grouped by resource. See [the README](./README.md) for usage and configuration.

## Contents

- [`VideoAssets`](#videoassets)
  - [Create Asset](#create-asset)
  - [Create Asset Direct Upload](#create-asset-direct-upload)
  - [Asset Details](#asset-details)
  - [Delete Asset](#delete-asset)
  - [Update Asset](#update-asset)
  - [Update thumbnail from video](#update-thumbnail-from-video)
  - [Update thumbnail via upload](#update-thumbnail-via-upload)
  - [Create/Update Video Asset Chapters](#createupdate-video-asset-chapters)
  - [List Assets](#list-assets)
  - [List Assets](#list-assets-1)
  - [Bulk Delete](#bulk-delete)
  - [Bulk Tag](#bulk-tag)
  - [Asset Analytics](#asset-analytics)
- [`SubtitleUpload`](#subtitleupload)
  - [Upload Subtitles](#upload-subtitles)
  - [Complete Subtitle Upload](#complete-subtitle-upload)
- [`AudioUpload`](#audioupload)
  - [Add Audio](#add-audio)
  - [Complete Audio Upload](#complete-audio-upload)
- [`VideoUsageAnalytics`](#videousageanalytics)
  - [Video Usage Analytics](#video-usage-analytics)
  - [Top Streamed Assets](#top-streamed-assets)
- [`MultipartUpload`](#multipartupload)
  - [Get Part Upload URL](#get-part-upload-url)
  - [Complete Multipart Upload](#complete-multipart-upload)
- [`VideoProfiles`](#videoprofiles)
  - [Create Profile](#create-profile)
  - [List Profiles](#list-profiles)
  - [Update Profile](#update-profile)
  - [Get Profile](#get-profile)
  - [Delete Profile](#delete-profile)
- [`VideoPlaylists`](#videoplaylists)
  - [Create Playlist](#create-playlist)
  - [Get all playlists](#get-all-playlists)
  - [Add asset to playlist](#add-asset-to-playlist)
  - [Remove asset from playlist](#remove-asset-from-playlist)
  - [Update Playlist](#update-playlist)
  - [`delete`](#delete)
  - [Get playlist assets](#get-playlist-assets)
  - [Arrange Videos In Playlist](#arrange-videos-in-playlist)
- [`Webhooks`](#webhooks)
  - [Create Webhook](#create-webhook)
  - [List Webhooks](#list-webhooks)
  - [Update Webhook](#update-webhook)
  - [Delete Webhook](#delete-webhook)
  - [Get History](#get-history)
- [`ImageSources`](#imagesources)
  - [Create Source](#create-source)
  - [List Sources](#list-sources)
  - [Get Image Source](#get-image-source)
  - [Update Source](#update-source)
  - [Delete Source](#delete-source)
  - [Purge Cache](#purge-cache)
  - [Purge Image Cache](#purge-image-cache)
- [`ImageUsageAnalytics`](#imageusageanalytics)
  - [Image Usage Analytics](#image-usage-analytics)
- [`LiveStreamAssets`](#livestreamassets)
  - [Create Live Asset](#create-live-asset)
  - [Update Live Asset](#update-live-asset)
  - [Get Live Asset Status](#get-live-asset-status)
  - [Delete Live Asset](#delete-live-asset)
  - [Complete Live Stream](#complete-live-stream)
  - [Filter Live Assets](#filter-live-assets)
  - [`start`](#start)
  - [Upload Live Thumbnails](#upload-live-thumbnails)
  - [Get Live Asset Status History](#get-live-asset-status-history)
- [`RecycleBin`](#recyclebin)
  - [Recover Deleted Asset](#recover-deleted-asset)
  - [List Recycle Bin](#list-recycle-bin)
- [`VideoWorkspaces`](#videoworkspaces)
  - [List Workspaces](#list-workspaces)
  - [Create Workspace](#create-workspace)
  - [Update Workspace](#update-workspace)
  - [Get Workspace](#get-workspace)
  - [Delete Workspace](#delete-workspace)
- [`Folders`](#folders)
  - [Create Folder](#create-folder)
  - [List Folders](#list-folders)
  - [Get Folder](#get-folder)
  - [Update Folder](#update-folder)
  - [Delete Folder](#delete-folder)
  - [Remove Assets From Folder](#remove-assets-from-folder)
- [`ChannelViewers`](#channelviewers)
  - [Invite Channel Viewers](#invite-channel-viewers)
  - [Remove Channel Viewers](#remove-channel-viewers)
  - [Invite Channel Viewers via CSV](#invite-channel-viewers-via-csv)
  - [List Subscribers](#list-subscribers)
- [`VideoAnalytics`](#videoanalytics)
  - [Viewer Analytics](#viewer-analytics)
  - [Breakdown Data](#breakdown-data)
  - [Aggregated Data](#aggregated-data)
- [`OrganizationData`](#organizationdata)
  - [Get Organization Details](#get-organization-details)
- [`UserData`](#userdata)
  - [Get User](#get-user)
- [`AuditLogs`](#auditlogs)
  - [Fetch Audit Logs](#fetch-audit-logs)
- [`Billing`](#billing)
  - [List Invoices](#list-invoices)
  - [Get Billing Details](#get-billing-details)
  - [Update Billing Details](#update-billing-details)
  - [Upcoming Invoice](#upcoming-invoice)
- [`LiveStreamWorkspaces`](#livestreamworkspaces)
  - [List Workspaces](#list-workspaces-1)
  - [Create Workspace](#create-workspace-1)
  - [Update Workspace](#update-workspace-1)
  - [Delete Workspace](#delete-workspace-1)
- [`LiveStreamAnalytics`](#livestreamanalytics)
  - [Usage Analytics](#usage-analytics)

## Setup

```python
import os

from gumlet import Gumlet

client = Gumlet(
    api_key=os.environ.get("API_KEY"),
)
```

## `VideoAssets`

Upload, manage, and retrieve video assets, including thumbnails, subtitles, audio tracks, and chapters.

### Create Asset

An asset refers to a media content/video that is processed, stored, and delivered through Gumlet. This endpoint creates an asset allowing users to ingest media content into the Gumlet system for processing and delivery.

| Direction | Type |
| --- | --- |
| Request | [`VideoAssetCreateParams`](./src/gumlet/types/video_asset_create_params.py) |
| Response | [`VideoAssetCreateResponse`](./src/gumlet/types/video_asset_create_response.py) |

```python
video_asset = client.video_assets.create(
    input="http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8",
    collection_id="646df1c9173a4a2fcac180b4",
    profile_id="646df1c9173a4a2fcac180b7",
    format="ABR",
    tag=["ball"],
    description="some description",
    metadata={"headermeta": "metavalue"},
    call_to_actions=[
        {
            "start_time": 1,
            "end_time": 90,
            "text": "some test",
            "url": "https://some-url.com",
            "position_from_top": 11,
            "position_from_right": 23,
            "border_radius": "11",
            "font_color": "#000001",
            "background_color": "#ffffff",
        }
    ],
    playlist_id="6597acd5ed6f26a9c5ca9633",
    folder="697375fbfa2d1037283140e4",
)
```

### Create Asset Direct Upload

This endpoint creates a video asset allowing to upload of the video from the local file system and ingest media content into the Gumlet system for processing and delivery.Body Parameters are the same as the Create Asset Body Parameters except for the `input` parameter which this endpoint does not take.A successful response will be returned with `upload_url` field. You can make `PUT` request to that URL to upload video. To upload video using `upload_url` refer to [this](https://docs.gumlet.com/docs/direct-upload#2-use-the-url-to-upload-a-file).

| Direction | Type |
| --- | --- |
| Request | [`VideoAssetUploadParams`](./src/gumlet/types/video_asset_upload_params.py) |
| Response | [`VideoAssetUploadResponse`](./src/gumlet/types/video_asset_upload_response.py) |

```python
video_asset = client.video_assets.upload(
    collection_id="646df1c9173a4a2fcac180b4",
    profile_id="646df1c9173a4a2fcac180b7",
    format="ABR",
    tag=["ball"],
    description="some description",
    metadata={"headermeta": "metavalue"},
    call_to_actions=[
        {
            "start_time": 1,
            "end_time": 90,
            "text": "some test",
            "url": "https://some-url.com",
            "position_from_top": 11,
            "position_from_right": 23,
            "border_radius": "11",
            "font_color": "#000001",
            "background_color": "#ffffff",
        }
    ],
    playlist_id="6597acd5ed6f26a9c5ca9633",
    folder="697375fbfa2d1037283140e4",
)
```

### Asset Details

This endpoint retrieves the details of an asset that has previously been created.

| Direction | Type |
| --- | --- |
| Response | [`VideoAssetRetrieveDetailsResponse`](./src/gumlet/types/video_asset_retrieve_details_response.py) |

```python
video_asset = client.video_assets.retrieve_details(
    asset_id="assetId",
)
```

### Delete Asset

This endpoint removes an asset given its unique asset id. The asset will be removed from storage as well, associated URLs will be inaccessible.

```python
client.video_assets.delete(
    asset_id="assetId",
)
```

### Update Asset

This endpoint allows users to update video asset that has previously been created.

| Direction | Type |
| --- | --- |
| Request | [`VideoAssetUpdateParams`](./src/gumlet/types/video_asset_update_params.py) |
| Response | [`VideoAssetUpdateResponse`](./src/gumlet/types/video_asset_update_response.py) |

```python
video_asset = client.video_assets.update(
    asset_id="<YOUR_ASSET_ID>",
    title="Updated Title",
)
```

### Update thumbnail from video

Select frame from video to use as thumbnail.

| Direction | Type |
| --- | --- |
| Request | [`VideoAssetThumbnailSelectParams`](./src/gumlet/types/video_asset_thumbnail_select_params.py) |
| Response | [`VideoAssetThumbnailSelectResponse`](./src/gumlet/types/video_asset_thumbnail_select_response.py) |

```python
video_asset = client.video_assets.thumbnail_select(
    asset_id="assetId",
    frame_at_second=2,
)
```

### Update thumbnail via upload

Use any image file to use as thumbnail. Once you use the API, you will get `upload_url` in the response, and that can be used to upload the image file.

Here is the sample curl request.

```bash
curl --location --request PUT '<upload_url>' \
--data '<YOUR_FILE_PATH>'
```

| Direction | Type |
| --- | --- |
| Response | [`VideoAssetThumbnailUploadResponse`](./src/gumlet/types/video_asset_thumbnail_upload_response.py) |

```python
video_asset = client.video_assets.thumbnail_upload(
    asset_id="assetId",
)
```

### Create/Update Video Asset Chapters

This endpoint will create/update video asset chapters.

| Direction | Type |
| --- | --- |
| Request | [`VideoAssetCreateUpdateChapterParams`](./src/gumlet/types/video_asset_create_update_chapter_params.py) |
| Response | [`VideoAssetCreateUpdateChapterResponse`](./src/gumlet/types/video_asset_create_update_chapter_response.py) |

```python
video_asset = client.video_assets.create_update_chapter(
    asset_id="assetId",
    chapters=[{"label": "Chapter 1", "startTime": 0}, {"label": "Chapter 2", "startTime": 10}],
)
```

### List Assets

List folders and assets for a workspace in a single response. Use `parent_id` to browse a specific folder, or filters like `title`, `status`, and `playlist_id` to search assets.

| Direction | Type |
| --- | --- |
| Request | [`VideoAssetListParams`](./src/gumlet/types/video_asset_list_params.py) |
| Response | [`VideoAssetListResponse`](./src/gumlet/types/video_asset_list_response.py) |

```python
video_asset = client.video_assets.list(
    workspace_id="workspaceId",
    type="all",
    offset=0,
    size=20,
    signed_token="false",
)
```

### List Assets

[Deprecated] This endpoint list assets in video workspace. You can also pass `status` and `tag` to filter assets.

| Direction | Type |
| --- | --- |
| Request | [`VideoAssetListDeprecatedParams`](./src/gumlet/types/video_asset_list_deprecated_params.py) |
| Response | [`VideoAssetListDeprecatedResponse`](./src/gumlet/types/video_asset_list_deprecated_response.py) |

```python
video_asset = client.video_assets.list_deprecated(
    workspace_id="workspaceId",
    sort_by="created_at",
    order_by="desc",
)
```

### Bulk Delete

Delete multiple VOD assets at once.

| Direction | Type |
| --- | --- |
| Request | [`VideoAssetDeleteManyParams`](./src/gumlet/types/video_asset_delete_many_params.py) |
| Response | [`VideoAssetDeleteManyResponse`](./src/gumlet/types/video_asset_delete_many_response.py) |

```python
video_asset = client.video_assets.delete_many(
    asset_list=["64249a8858fd3a208b987702", "64784bae843b155b829bbf84"],
    source_id="60bd2ba353ff754d28179ee6",
)
```

### Bulk Tag

Add / remove tags from multiple assets at once.

| Direction | Type |
| --- | --- |
| Request | [`VideoAssetTagManyParams`](./src/gumlet/types/video_asset_tag_many_params.py) |
| Response | [`VideoAssetTagManyResponse`](./src/gumlet/types/video_asset_tag_many_response.py) |

```python
video_asset = client.video_assets.tag_many(
    asset_list=["6221db301c8b821b0519fba0", "61e8f2726ec832ab2ac4fa6e"],
    source_id="60bd2ba353ff754d28179ee6",
    add_tags=["tag-1"],
    remove_tags=["playlist-1"],
)
```

### Asset Analytics

Get video analytics for a single asset.

| Direction | Type |
| --- | --- |
| Request | [`VideoAssetAnalyticsParams`](./src/gumlet/types/video_asset_analytics_params.py) |
| Response | [`VideoAssetAnalyticsResponse`](./src/gumlet/types/video_asset_analytics_response.py) |

```python
video_asset = client.video_assets.analytics(
    asset_id="assetId",
    group_by="daily",
    date_range={"start_at": "", "end_at": ""},
    metrics=["impressions"],
)
```

## `SubtitleUpload`

Add subtitles to an existing asset.

### Upload Subtitles

Upload `.srt` or `.vtt`  file to the video asset. The response of this API call gives `upload_url` for each language specified. You need to send a `PUT` request of the subtitle files to those URLs. Once that's done, you need to call the subtitle upload complete API. Only after that, Gumlet will add subtitles to asset.

| Direction | Type |
| --- | --- |
| Request | [`SubtitleUploadUploadParams`](./src/gumlet/types/subtitle_upload_upload_params.py) |
| Response | [`SubtitleUploadUploadResponse`](./src/gumlet/types/subtitle_upload_upload_response.py) |

```python
subtitle_upload = client.subtitle_upload.upload(
    asset_id="assetId",
    language_codes=["en"],
)
```

### Complete Subtitle Upload

This API must be called after adding subtitles; the add subtitle call gives you URLs to upload, and you complete a `PUT` request to those URLs. 
Once that is done, calling this initiates the process to actually add the subtitle to the video.

| Direction | Type |
| --- | --- |
| Request | [`SubtitleUploadCompleteParams`](./src/gumlet/types/subtitle_upload_complete_params.py) |
| Response | [`SubtitleUploadCompleteResponse`](./src/gumlet/types/subtitle_upload_complete_response.py) |

```python
subtitle_upload = client.subtitle_upload.complete(
    asset_id="assetId",
    upload_responses=[{"language_code": "en", "uploaded": True}],
)
```

## `AudioUpload`

Add additional audio tracks to an existing asset.

### Add Audio

Add any audio file to the video asset. 
The response of this API call gives `upload_url` for each language specified. You need to send a `PUT` request of the audio files to those URLs. Once that's done, you need to call the audio upload complete API. Only after that will Gumlet add audio to the asset.

| Direction | Type |
| --- | --- |
| Request | [`AudioUploadUploadParams`](./src/gumlet/types/audio_upload_upload_params.py) |
| Response | [`AudioUploadUploadResponse`](./src/gumlet/types/audio_upload_upload_response.py) |

```python
audio_upload = client.audio_upload.upload(
    asset_id="assetId",
    language_codes=["en"],
)
```

### Complete Audio Upload

This API must be called after adding audio(s); The add audio call gives you URLs to upload, and you complete a `PUT` request to those URLs. 
Once that is done, calling this initiates the process to actually add the subtitle to the video.

| Direction | Type |
| --- | --- |
| Request | [`AudioUploadCompleteParams`](./src/gumlet/types/audio_upload_complete_params.py) |
| Response | [`AudioUploadCompleteResponse`](./src/gumlet/types/audio_upload_complete_response.py) |

```python
audio_upload = client.audio_upload.complete(
    asset_id="assetId",
    upload_responses=[{"language_codes": ["en"], "uploaded": True}],
)
```

## `VideoUsageAnalytics`

Query video analytics and streaming duration usage data.

### Video Usage Analytics

This endpoint gives usage analytics data of your videos. Ex - top assets, bandwidth consumption

| Direction | Type |
| --- | --- |
| Request | [`VideoUsageAnalyticRetrieveParams`](./src/gumlet/types/video_usage_analytic_retrieve_params.py) |
| Response | [`VideoUsageAnalyticRetrieveResponse`](./src/gumlet/types/video_usage_analytic_retrieve_response.py) |

```python
video_usage_analytic = client.video_usage_analytics.retrieve(
    metrics=["bandwidth_consumption", "asset_duration", "storage_unit", "top_assets", "drm_requests"],
    date_range={"start_at": "2026-08-01", "end_at": "2026-08-20"},
    top_assets_count="5",
    top_assets_page="0",
    group_by="hourly",
)
```

### Top Streamed Assets

This endpoint lists top streamed assets in a video collection

| Direction | Type |
| --- | --- |
| Request | [`VideoUsageAnalyticTopAssetsParams`](./src/gumlet/types/video_usage_analytic_top_assets_params.py) |
| Response | [`VideoUsageAnalyticTopAssetsResponse`](./src/gumlet/types/video_usage_analytic_top_assets_response.py) |

```python
video_usage_analytic = client.video_usage_analytics.top_assets(
    start_at="2026-06-21",
    end_at="2026-06-30",
    page="1",
    page_size="1000",
)
```

## `MultipartUpload`

Upload large video files in parts and complete the multipart upload.

### Get Part Upload URL

Use this endpoint to retrieve a pre-signed upload URL for the given part number.

| Direction | Type |
| --- | --- |
| Response | [`MultipartUploadRetrievePartURLResponse`](./src/gumlet/types/multipart_upload_retrieve_part_url_response.py) |

```python
multipart_upload = client.multipart_upload.retrieve_part_url(
    asset_id="assetId",
    part_number="partNumber",
)
```

### Complete Multipart Upload

Once you upload all parts to S3 bucket via pre-signed URL, use this endpoint to complete the multipart upload.

| Direction | Type |
| --- | --- |
| Request | [`MultipartUploadCompleteParams`](./src/gumlet/types/multipart_upload_complete_params.py) |
| Response | [`MultipartUploadCompleteResponse`](./src/gumlet/types/multipart_upload_complete_response.py) |

```python
multipart_upload = client.multipart_upload.complete(
    asset_id="assetId",
)
```

## `VideoProfiles`

Create and manage encoding/output profiles for video assets.

### Create Profile

Gumlet provides the functionality of creating multiple video assets using the same set of parameters. A Video profile is a set of parameters that can be referenced/used while creating a video as a single parameter.

| Direction | Type |
| --- | --- |
| Request | [`VideoProfileCreateParams`](./src/gumlet/types/video_profile_create_params.py) |
| Response | [`VideoProfileCreateResponse`](./src/gumlet/types/video_profile_create_response.py) |

```python
video_profile = client.video_profiles.create(
    name="Gumlet-Profile-1",
    format="ABR",
)
```

### List Profiles

This endpoint retrieves the details of all profiles that have previously been created.

| Direction | Type |
| --- | --- |
| Request | [`VideoProfileListParams`](./src/gumlet/types/video_profile_list_params.py) |
| Response | [`VideoProfileListResponse`](./src/gumlet/types/video_profile_list_response.py) |

```python
video_profile = client.video_profiles.list()
```

### Update Profile

Update an existing profile. Settings provided in body parameters will only be updated in the existing profile.

| Direction | Type |
| --- | --- |
| Request | [`VideoProfileUpdateParams`](./src/gumlet/types/video_profile_update_params.py) |
| Response | [`VideoProfileUpdateResponse`](./src/gumlet/types/video_profile_update_response.py) |

```python
video_profile = client.video_profiles.update(
    path_profile_id="profileId",
    body_profile_id="",
    format="ABR",
)
```

### Get Profile

This endpoint retrieves the details of a video profile that has previously been created.

| Direction | Type |
| --- | --- |
| Response | [`VideoProfileRetrieveResponse`](./src/gumlet/types/video_profile_retrieve_response.py) |

```python
video_profile = client.video_profiles.retrieve(
    profile_id="profileId",
)
```

### Delete Profile

This endpoint removes a profile given its unique `profile_id`. The profile will be removed but video assets created using the profile will remain as it is.

| Direction | Type |
| --- | --- |
| Response | [`VideoProfileDeleteResponse`](./src/gumlet/types/video_profile_delete_response.py) |

```python
video_profile = client.video_profiles.delete(
    profile_id="profileId",
)
```

## `VideoPlaylists`

Create and manage playlists, and control which assets belong to them.

### Create Playlist

Create new playlist inside video wprkspace

| Direction | Type |
| --- | --- |
| Request | [`VideoPlaylistCreateParams`](./src/gumlet/types/video_playlist_create_params.py) |
| Response | [`VideoPlaylistCreateResponse`](./src/gumlet/types/video_playlist_create_response.py) |

```python
video_playlist = client.video_playlists.create(
    collection_id="{{video-source-id}}",
    title="Playlist-Title",
    description="This is description for playlist.",
)
```

### Get all playlists

Get all playlists for given workspace

| Direction | Type |
| --- | --- |
| Request | [`VideoPlaylistListAllParams`](./src/gumlet/types/video_playlist_list_all_params.py) |
| Response | [`VideoPlaylistListAllResponse`](./src/gumlet/types/video_playlist_list_all_response.py) |

```python
video_playlist = client.video_playlists.list_all()
```

### Add asset to playlist

This operation adds a single asset or a list of assets to a playlist.

| Direction | Type |
| --- | --- |
| Request | [`VideoPlaylistCreateAssetParams`](./src/gumlet/types/video_playlist_create_asset_params.py) |
| Response | [`VideoPlaylistCreateAssetResponse`](./src/gumlet/types/video_playlist_create_asset_response.py) |

```python
video_playlist = client.video_playlists.create_asset(
    playlist_id="playlistId",
    asset_list=[
        {"asset_id": "6508790283e4d60611846790"},
        {"position": 1, "asset_id": "650878f883e4d6061184677d"},
        {"asset_id": "650878de83e4d6061184676a"},
        {"position": 2, "asset_id": "650878d883e4d60611846757"},
        {"position": 3, "asset_id": "65578dd87eebc22dcdd549a2"},
    ],
)
```

### Remove asset from playlist

Removed an asset or list of assets from a given playlist.

| Direction | Type |
| --- | --- |
| Request | [`VideoPlaylistDeleteAssetParams`](./src/gumlet/types/video_playlist_delete_asset_params.py) |
| Response | [`VideoPlaylistDeleteAssetResponse`](./src/gumlet/types/video_playlist_delete_asset_response.py) |

```python
video_playlist = client.video_playlists.delete_asset(
    playlist_id="playlistId",
    delete_list=["6508790783e4d606118467a3"],
)
```

### Update Playlist

This endpoint allows you to update playlist name, channel visibility, or playlist order on a channel page.

| Direction | Type |
| --- | --- |
| Request | [`VideoPlaylistUpdateParams`](./src/gumlet/types/video_playlist_update_params.py) |
| Response | [`VideoPlaylistUpdateResponse`](./src/gumlet/types/video_playlist_update_response.py) |

```python
video_playlist = client.video_playlists.update(
    playlist_id="playlistId",
    title="Playlist-Title-Updated",
    description="This is updated description",
    position=6,
    player_config={
        "preload": True,
        "autoplay": False,
        "disable_seek": True,
        "disable_player_controls": False,
        "powered_by_gumlet_overlay": False,
        "allow_drm_protected_videos": False,
        "loop": False,
        "player_color": "#6658ea",
        "include_seo": True,
        "subtitle_enabled": True,
        "pixel_tags": {},
        "logo_width": 51,
        "logo_height": 100,
        "dynamic_watermark": False,
        "watermark_font_size": 1,
        "watermark_font_color": "#ff0000",
        "watermark_bg_color": "transparent",
        "watermark_interval": 1000,
    },
    channel_visibility=False,
)
```

### `delete`

Deletes this playlist.

```python
client.video_playlists.delete(
    playlist_id="playlistId",
)
```

### Get playlist assets

Get a list of all assets inside playlist. You can choose in which order are assets returned.

| Direction | Type |
| --- | --- |
| Request | [`VideoPlaylistListAssetsParams`](./src/gumlet/types/video_playlist_list_assets_params.py) |
| Response | [`VideoPlaylistListAssetsResponse`](./src/gumlet/types/video_playlist_list_assets_response.py) |

```python
video_playlist = client.video_playlists.list_assets(
    playlist_id="playlistId",
    sort_order=1,
    page_number=1,
    page_size="10",
)
```

### Arrange Videos In Playlist

Reorder videos inside a playlist either by moving a single asset to a position or by sorting the playlist by title or created date.

| Direction | Type |
| --- | --- |
| Request | [`VideoPlaylistReorderAssetParams`](./src/gumlet/types/video_playlist_reorder_asset_params.py) |
| Response | [`VideoPlaylistReorderAssetResponse`](./src/gumlet/types/video_playlist_reorder_asset_response.py) |

```python
video_playlist = client.video_playlists.reorder_asset(
    playlist_id="playlistId",
    asset_id="6e82bf783e88be000ab45ed2",
    page_number=1,
    page_size=10,
    asset_position=0,
)
```

## `Webhooks`

Configure webhooks for account and asset events.

### Create Webhook

Creates a new webhook listener.

| Direction | Type |
| --- | --- |
| Request | [`WebhookCreateParams`](./src/gumlet/types/webhook_create_params.py) |
| Response | [`WebhookCreateResponse`](./src/gumlet/types/webhook_create_response.py) |

```python
webhook = client.webhooks.create(
    url="",
    secret_token="",
    triggers=[""],
    sources=[""],
)
```

### List Webhooks

List all webhooks.

| Direction | Type |
| --- | --- |
| Response | [`WebhookListResponse`](./src/gumlet/types/webhook_list_response.py) |

```python
webhook = client.webhooks.list()
```

### Update Webhook

Update a webhook listener.

| Direction | Type |
| --- | --- |
| Request | [`WebhookUpdateParams`](./src/gumlet/types/webhook_update_params.py) |
| Response | [`WebhookUpdateResponse`](./src/gumlet/types/webhook_update_response.py) |

```python
webhook = client.webhooks.update(
    webhook_id="webhookId",
)
```

### Delete Webhook

Delete webhook listener endpoint.

| Direction | Type |
| --- | --- |
| Response | [`WebhookDeleteResponse`](./src/gumlet/types/webhook_delete_response.py) |

```python
webhook = client.webhooks.delete(
    webhook_id="webhookId",
)
```

### Get History

Get logs history for a given webhook.

| Direction | Type |
| --- | --- |
| Response | [`WebhookHistoryResponse`](./src/gumlet/types/webhook_history_response.py) |

```python
webhook = client.webhooks.history(
    webhook_id="webhookId",
)
```

## `ImageSources`

Manage image sources, view image analytics, and purge the image cache.

### Create Source

This endpoint allows users to create image source.

| Direction | Type |
| --- | --- |
| Request | [`ImageSourceCreateParams`](./src/gumlet/types/image_source_create_params.py) |
| Response | [`ImageSourceCreateResponse`](./src/gumlet/types/image_source_create_response.py) |

```python
image_source = client.image_sources.create(
    namespace="google-demo",
    type="webfolder",
    webfolder={"base_url": "https://www.google.com"},
)
```

### List Sources

This endpoint list image sources which are assigned to the user or token.

| Direction | Type |
| --- | --- |
| Request | [`ImageSourceListParams`](./src/gumlet/types/image_source_list_params.py) |
| Response | [`ImageSourceListResponse`](./src/gumlet/types/image_source_list_response.py) |

```python
image_source = client.image_sources.list(
    offset=0,
    size=20,
)
```

### Get Image Source

Get all details about image source.

| Direction | Type |
| --- | --- |
| Response | [`ImageSourceRetrieveResponse`](./src/gumlet/types/image_source_retrieve_response.py) |

```python
image_source = client.image_sources.retrieve(
    image_source_id="imageSourceId",
)
```

### Update Source

This endpoint allows users to update image source that has previously been created.

| Direction | Type |
| --- | --- |
| Request | [`ImageSourceUpdateParams`](./src/gumlet/types/image_source_update_params.py) |
| Response | [`ImageSourceUpdateResponse`](./src/gumlet/types/image_source_update_response.py) |

```python
image_source = client.image_sources.update(
    image_source_id="imageSourceId",
    type="aws",
    aws={
        "bucket_name": "my-bucket-test",
        "bucket_region": "ap-southeast-1",
        "access_key": "BQUA6QFXVWHAAB6IO2X1",
        "secret": "aws_secret",
    },
)
```

### Delete Source

This endpoint removes a image source. All image delivery using this subdomain will be stopped.

| Direction | Type |
| --- | --- |
| Response | [`ImageSourceDeleteResponse`](./src/gumlet/types/image_source_delete_response.py) |

```python
image_source = client.image_sources.delete(
    image_source_id="imageSourceId",
)
```

### Purge Cache

You can purge cache for any image by using our cache purge API.

| Direction | Type |
| --- | --- |
| Request | [`ImageSourcePurgeCacheParams`](./src/gumlet/types/image_source_purge_cache_params.py) |
| Response | [`ImageSourcePurgeCacheResponse`](./src/gumlet/types/image_source_purge_cache_response.py) |

```python
image_source = client.image_sources.purge_cache(
    subdomain="subdomain",
    paths=["image.jpeg", "image2.png"],
)
```

### Purge Image Cache

You can purge the cache for any image path by using this cache purge API.

| Direction | Type |
| --- | --- |
| Request | [`ImageSourcePurgeParams`](./src/gumlet/types/image_source_purge_params.py) |
| Response | [`ImageSourcePurgeResponse`](./src/gumlet/types/image_source_purge_response.py) |

```python
image_source = client.image_sources.purge(
    source_id="sourceId",
    paths=["image.jpeg", "image2.png"],
)
```

## `ImageUsageAnalytics`

Query aggregated and chart-ready image usage analytics data.

### Image Usage Analytics

This endpoint helps you get image analytics data like bandwidth consumption, request count, CDN hit ratio, etc.

| Direction | Type |
| --- | --- |
| Request | [`ImageUsageAnalyticRetrieveParams`](./src/gumlet/types/image_usage_analytic_retrieve_params.py) |
| Response | [`ImageUsageAnalyticRetrieveResponse`](./src/gumlet/types/image_usage_analytic_retrieve_response.py) |

```python
image_usage_analytic = client.image_usage_analytics.retrieve(
    metrics=["bandwidth_consumption"],
    date_range={},
    group_by="daily",
)
```

## `LiveStreamAssets`

Create, control, and monitor live stream assets.

### Create Live Asset

A live asset refers to a media content/video that is live-streamed through Gumlet. This endpoint creates a live streaming asset allowing users to live stream a video that will be pushed to Gumlet.

| Direction | Type |
| --- | --- |
| Request | [`LiveStreamAssetCreateParams`](./src/gumlet/types/live_stream_asset_create_params.py) |
| Response | [`LiveStreamAssetCreateResponse`](./src/gumlet/types/live_stream_asset_create_response.py) |

```python
live_stream_asset = client.live_stream_assets.create(
    live_source_id="",
    resolution="",
)
```

### Update Live Asset

A live asset refers to a media content/video that is live-streamed through Gumlet. This endpoint allows user to update a live streaming asset.

| Direction | Type |
| --- | --- |
| Request | [`LiveStreamAssetUpdateParams`](./src/gumlet/types/live_stream_asset_update_params.py) |
| Response | [`LiveStreamAssetUpdateResponse`](./src/gumlet/types/live_stream_asset_update_response.py) |

```python
live_stream_asset = client.live_stream_assets.update(
    live_asset_id="",
)
```

### Get Live Asset Status

This endpoint retrieves the details of a live video asset that has previously been created.

| Direction | Type |
| --- | --- |
| Response | [`LiveStreamAssetRetrieveStatusResponse`](./src/gumlet/types/live_stream_asset_retrieve_status_response.py) |

```python
live_stream_asset = client.live_stream_assets.retrieve_status(
    live_asset_id="liveAssetId",
)
```

### Delete Live Asset

This endpoint removes a live asset given its unique live asset id. The live asset will be removed from storage as well, associated URLs will be inaccessible.

| Direction | Type |
| --- | --- |
| Response | [`LiveStreamAssetDeleteResponse`](./src/gumlet/types/live_stream_asset_delete_response.py) |

```python
live_stream_asset = client.live_stream_assets.delete(
    live_asset_id="liveAssetId",
)
```

### Complete Live Stream

This endpoint allows marking live assets complete. Once the live asset is marked complete, it can no longer be used to ingest the live stream on Gumlet.

| Direction | Type |
| --- | --- |
| Response | [`LiveStreamAssetCompleteResponse`](./src/gumlet/types/live_stream_asset_complete_response.py) |

```python
live_stream_asset = client.live_stream_assets.complete(
    live_asset_id="liveAssetId",
)
```

### Filter Live Assets

This endpoint lists live assets on the basis of `status` for the given `live_source_id`.

| Direction | Type |
| --- | --- |
| Request | [`LiveStreamAssetFilterParams`](./src/gumlet/types/live_stream_asset_filter_params.py) |
| Response | [`LiveStreamAssetFilterResponse`](./src/gumlet/types/live_stream_asset_filter_response.py) |

```python
live_stream_asset = client.live_stream_assets.filter(
    live_source_id="liveSourceId",
)
```

### `start`

Start a live stream.

```python
client.live_stream_assets.start(
    live_asset_id="liveAssetId",
)
```

### Upload Live Thumbnails

Generate presigned upload URLs for live stream thumbnails. Supported thumbnail states are `preparing`, `disconnected`, and `end`.

| Direction | Type |
| --- | --- |
| Request | [`LiveStreamAssetUploadParams`](./src/gumlet/types/live_stream_asset_upload_params.py) |
| Response | [`LiveStreamAssetUploadResponse`](./src/gumlet/types/live_stream_asset_upload_response.py) |

```python
live_stream_asset = client.live_stream_assets.upload(
    live_asset_id="68c406b147f9ad0c0d584ce2",
    statuses="preparing",
)
```

### Get Live Asset Status History

This endpoint retrieves the history of a live video asset that has previously been created.

| Direction | Type |
| --- | --- |
| Response | [`LiveStreamAssetStatusHistoryResponse`](./src/gumlet/types/live_stream_asset_status_history_response.py) |

```python
live_stream_asset = client.live_stream_assets.status_history(
    live_asset_id="liveAssetId",
)
```

## `RecycleBin`

Endpoints to list deleted assets and restore them.

### Recover Deleted Asset

Recovers a deleted asset from the recycle bin.

| Direction | Type |
| --- | --- |
| Request | [`RecycleBinRecoverParams`](./src/gumlet/types/recycle_bin_recover_params.py) |

```python
client.recycle_bin.recover(
    asset_id="",
)
```

### List Recycle Bin

List all assets in a recycle bin for a given workspace. The deleted assets are available for 30 days. After that, assets are permanently deleted.

| Direction | Type |
| --- | --- |
| Request | [`RecycleBinListParams`](./src/gumlet/types/recycle_bin_list_params.py) |
| Response | [`RecycleBinListResponse`](./src/gumlet/types/recycle_bin_list_response.py) |

```python
recycle_bin = client.recycle_bin.list(
    size=20,
    workspace_id="workspace_id",
)
```

## `VideoWorkspaces`

Create and manage video workspaces.

### List Workspaces

This endpoint list video workspace which are assigned to the user or token.

| Direction | Type |
| --- | --- |
| Request | [`VideoWorkspaceListParams`](./src/gumlet/types/video_workspace_list_params.py) |
| Response | [`VideoWorkspaceListResponse`](./src/gumlet/types/video_workspace_list_response.py) |

```python
video_workspace = client.video_workspaces.list(
    offset="0",
    size="10",
)
```

### Create Workspace

Video workspaces are top-level entities in Gumlet. You can use them to organize videos for different teams/departments or use cases.

| Direction | Type |
| --- | --- |
| Request | [`VideoWorkspaceCreateParams`](./src/gumlet/types/video_workspace_create_params.py) |
| Response | [`VideoWorkspaceCreateResponse`](./src/gumlet/types/video_workspace_create_response.py) |

```python
video_workspace = client.video_workspaces.create(
    name="zoom-workspace",
    type="direct-upload",
    zoom={"secret": "yourSecret"},
)
```

### Update Workspace

This endpoint allows users to update video workspace that has previously been created.

| Direction | Type |
| --- | --- |
| Request | [`VideoWorkspaceUpdateParams`](./src/gumlet/types/video_workspace_update_params.py) |
| Response | [`VideoWorkspaceUpdateResponse`](./src/gumlet/types/video_workspace_update_response.py) |

```python
video_workspace = client.video_workspaces.update(
    workspace_id="workspaceId",
    name="awsrename",
    default_profile_id="646df1c9173a4a2fcac180b7",
    type="aws",
    aws={
        "bucket_name": "my-bucket-test",
        "bucket_region": "ap-southeast-1",
        "access_key": "BQUA6QFXVWHAAB6IO2X1",
        "secret": "aws_secret",
    },
)
```

### Get Workspace

This endpoint get all the data of video workspace that has previously been created.

| Direction | Type |
| --- | --- |
| Response | [`VideoWorkspaceRetrieveResponse`](./src/gumlet/types/video_workspace_retrieve_response.py) |

```python
video_workspace = client.video_workspaces.retrieve(
    workspace_id="workspaceId",
)
```

### Delete Workspace

This endpoint removes a video workspace given its unique asset id. All the asset in workspace will be removed from storage as well, associated URLs will be inaccessible.

| Direction | Type |
| --- | --- |
| Response | [`VideoWorkspaceDeleteResponse`](./src/gumlet/types/video_workspace_delete_response.py) |

```python
video_workspace = client.video_workspaces.delete(
    workspace_id="workspaceId",
)
```

## `Folders`

Organize video assets into folders within a workspace.

### Create Folder

Create a folder inside a video workspace. Optionally provide `parent_id` to create a nested folder.

| Direction | Type |
| --- | --- |
| Request | [`FolderCreateParams`](./src/gumlet/types/folder_create_params.py) |
| Response | [`FolderCreateResponse`](./src/gumlet/types/folder_create_response.py) |

```python
folder = client.folders.create(
    workspace_id="workspaceId",
    name="Course Assets",
    parent_id="",
)
```

### List Folders

List folders for a video workspace. Use `parent_id` to list only folders inside a specific parent folder.

| Direction | Type |
| --- | --- |
| Request | [`FolderListParams`](./src/gumlet/types/folder_list_params.py) |
| Response | [`FolderListResponse`](./src/gumlet/types/folder_list_response.py) |

```python
folder = client.folders.list(
    workspace_id="workspaceId",
)
```

### Get Folder

Get a single folder by id.

| Direction | Type |
| --- | --- |
| Response | [`FolderRetrieveResponse`](./src/gumlet/types/folder_retrieve_response.py) |

```python
folder = client.folders.retrieve(
    workspace_id="workspaceId",
    folder_id="folderId",
)
```

### Update Folder

Rename a folder, move it to another parent folder, or move assets into the folder by sending `asset_ids`.

| Direction | Type |
| --- | --- |
| Request | [`FolderUpdateParams`](./src/gumlet/types/folder_update_params.py) |
| Response | [`FolderUpdateResponse`](./src/gumlet/types/folder_update_response.py) |

```python
folder = client.folders.update(
    workspace_id="workspaceId",
    folder_id="folderId",
    name="Course Assets Updated",
)
```

### Delete Folder

Delete a folder. Descendant folders and assets inside them are deleted by the backend workflow.

| Direction | Type |
| --- | --- |
| Response | [`FolderDeleteResponse`](./src/gumlet/types/folder_delete_response.py) |

```python
folder = client.folders.delete(
    workspace_id="workspaceId",
    folder_id="folderId",
)
```

### Remove Assets From Folder

Remove one or more assets from their current folder assignment inside the workspace.

| Direction | Type |
| --- | --- |
| Request | [`FolderDeleteAssetsParams`](./src/gumlet/types/folder_delete_assets_params.py) |
| Response | [`FolderDeleteAssetsResponse`](./src/gumlet/types/folder_delete_assets_response.py) |

```python
folder = client.folders.delete_assets(
    workspace_id="workspaceId",
    asset_ids=["67e4f2b4403562dbea654301", "67e4f2bb403562dbea654302"],
)
```

## `ChannelViewers`

Invite and remove viewers on a private video channel.

### Invite Channel Viewers

Invite one or more viewers to a members-only channel.

| Direction | Type |
| --- | --- |
| Request | [`ChannelViewerInviteParams`](./src/gumlet/types/channel_viewer_invite_params.py) |
| Response | [`ChannelViewerInviteResponse`](./src/gumlet/types/channel_viewer_invite_response.py) |

```python
channel_viewer = client.channel_viewers.invite(
    video_workspace_id="videoWorkspaceId",
    users=[
        {"email": "test@gumlet.com", "name": "Test User-0"},
        {"email": "test+1@gumlet.com", "name": "Test User-1"},
        {"email": "test+2@gumlet.com", "name": "Test User-2"},
    ],
)
```

### Remove Channel Viewers

Remove one or more viewers from a channel by email address.

| Direction | Type |
| --- | --- |
| Request | [`ChannelViewerDeleteParams`](./src/gumlet/types/channel_viewer_delete_params.py) |
| Response | [`ChannelViewerDeleteResponse`](./src/gumlet/types/channel_viewer_delete_response.py) |

```python
channel_viewer = client.channel_viewers.delete(
    video_workspace_id="videoWorkspaceId",
    emails=["test@gumlet.com", "test+2@gumlet.com"],
)
```

### Invite Channel Viewers via CSV

Invite viewers to a channel by uploading a CSV file.

| Direction | Type |
| --- | --- |
| Request | [`ChannelViewerInviteCsvParams`](./src/gumlet/types/channel_viewer_invite_csv_params.py) |
| Response | [`ChannelViewerInviteCsvResponse`](./src/gumlet/types/channel_viewer_invite_csv_response.py) |

```python
channel_viewer = client.channel_viewers.invite_csv(
    video_workspace_id="videoWorkspaceId",
    viewers_csv=b"viewers.csv",
)
```

### List Subscribers

List all channel subscribers.

| Direction | Type |
| --- | --- |
| Request | [`ChannelViewerListSubscribersParams`](./src/gumlet/types/channel_viewer_list_subscribers_params.py) |
| Response | [`ChannelViewerListSubscribersResponse`](./src/gumlet/types/channel_viewer_list_subscribers_response.py) |

```python
channel_viewer = client.channel_viewers.list_subscribers(
    workspace_id="workspaceId",
    page_number=1,
    page_size=10,
)
```

## `VideoAnalytics`

Query aggregated and chart-ready video analytics data.

### Viewer Analytics

This endpoint retrieves viewer analytics data. This endpoint is use for deep insights on the analytics data.

| Direction | Type |
| --- | --- |
| Request | [`VideoAnalyticChartDataParams`](./src/gumlet/types/video_analytic_chart_data_params.py) |
| Response | [`VideoAnalyticChartDataResponse`](./src/gumlet/types/video_analytic_chart_data_response.py) |

```python
video_analytic = client.video_analytics.chart_data(
    metrics=[""],
    workspace_id="",
    date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
    group_by="daily",
)
```

### Breakdown Data

This endpoint retrieves breakdown data of the given metrics by given breakdown field

| Direction | Type |
| --- | --- |
| Request | [`VideoAnalyticBreakdownDataParams`](./src/gumlet/types/video_analytic_breakdown_data_params.py) |
| Response | [`VideoAnalyticBreakdownDataResponse`](./src/gumlet/types/video_analytic_breakdown_data_response.py) |

```python
video_analytic = client.video_analytics.breakdown_data(
    date_range={"start_at": "2026-07-20", "end_at": "2026-08-20"},
    filters=[],
    breakdowns=[
        {"name": "custom_video_id", "metric": "views", "page": 1, "page_size": 10},
        {"name": "custom_video_title", "metric": "completion_percent_by_views", "page": 1, "page_size": 10},
    ],
    workspace_id="6694c405e63913eecf3cf5fb",
)
```

### Aggregated Data

This endpoint retrieves aggregated data of the given metrics.

| Direction | Type |
| --- | --- |
| Request | [`VideoAnalyticAggregatedDataParams`](./src/gumlet/types/video_analytic_aggregated_data_params.py) |
| Response | [`VideoAnalyticAggregatedDataResponse`](./src/gumlet/types/video_analytic_aggregated_data_response.py) |

```python
video_analytic = client.video_analytics.aggregated_data(
    aggregate=[{"metric": "views", "function": "sum"}],
    workspace_id="",
    timeframe={},
)
```

## `OrganizationData`

Endpoints to get organization details.

### Get Organization Details

You can get organization data using this API.

| Direction | Type |
| --- | --- |
| Response | [`OrganizationDataFetchOrgResponse`](./src/gumlet/types/organization_data_fetch_org_response.py) |

```python
organization_data = client.organization_data.fetch_org()
```

## `UserData`

Endpoints to get user details.

### Get User

This endpoint gives information about the user account.

| Direction | Type |
| --- | --- |
| Response | [`UserDataFetchResponse`](./src/gumlet/types/user_data_fetch_response.py) |

```python
user_data = client.user_data.fetch()
```

## `AuditLogs`

Get detailed user activity logs for the entire organisation.

### Fetch Audit Logs

Get audit logs for the user activity in your organisation. Please note that this endpoint can only be accessed by `owner` and `admin` role users.

| Direction | Type |
| --- | --- |
| Request | [`AuditLogFetchParams`](./src/gumlet/types/audit_log_fetch_params.py) |
| Response | [`AuditLogFetchResponse`](./src/gumlet/types/audit_log_fetch_response.py) |

```python
audit_log = client.audit_logs.fetch(
    date_range={"start_at": "2026-08-25", "end_at": "2026-08-29"},
    page_number=1,
    page_size=100,
)
```

## `Billing`

Get / change all details about billing and invoices.

### List Invoices

Liost all invoices that are generated so far.

| Direction | Type |
| --- | --- |
| Response | [`BillingListInvoicesResponse`](./src/gumlet/types/billing_list_invoices_response.py) |

```python
billing = client.billing.list_invoices()
```

### Get Billing Details

Get billing details for this organization.

| Direction | Type |
| --- | --- |
| Response | [`BillingFetchDetailsResponse`](./src/gumlet/types/billing_fetch_details_response.py) |

```python
billing = client.billing.fetch_details()
```

### Update Billing Details

Update billing details

| Direction | Type |
| --- | --- |
| Request | [`BillingUpdateDetailsParams`](./src/gumlet/types/billing_update_details_params.py) |
| Response | [`BillingUpdateDetailsResponse`](./src/gumlet/types/billing_update_details_response.py) |

```python
billing = client.billing.update_details(
    address_line="",
    city="",
    company_name="",
    country_code="",
    gst_number="",
    postal="",
    state_code="",
)
```

### Upcoming Invoice

Get details about upcoming invoice.

| Direction | Type |
| --- | --- |
| Response | [`BillingFetchUpcomingInvoiceResponse`](./src/gumlet/types/billing_fetch_upcoming_invoice_response.py) |

```python
billing = client.billing.fetch_upcoming_invoice()
```

## `LiveStreamWorkspaces`

Create and manage live stream workspaces.

### List Workspaces

List all live stream workspaces.

| Direction | Type |
| --- | --- |
| Response | [`LiveStreamWorkspaceListResponse`](./src/gumlet/types/live_stream_workspace_list_response.py) |

```python
live_stream_workspace = client.live_stream_workspaces.list()
```

### Create Workspace

Create live stream workspace.

| Direction | Type |
| --- | --- |
| Request | [`LiveStreamWorkspaceCreateParams`](./src/gumlet/types/live_stream_workspace_create_params.py) |
| Response | [`LiveStreamWorkspaceCreateResponse`](./src/gumlet/types/live_stream_workspace_create_response.py) |

```python
live_stream_workspace = client.live_stream_workspaces.create(
    name="",
)
```

### Update Workspace

Update live stream workspace.

| Direction | Type |
| --- | --- |
| Request | [`LiveStreamWorkspaceUpdateParams`](./src/gumlet/types/live_stream_workspace_update_params.py) |
| Response | [`LiveStreamWorkspaceUpdateResponse`](./src/gumlet/types/live_stream_workspace_update_response.py) |

```python
live_stream_workspace = client.live_stream_workspaces.update(
    live_workspace_id="liveWorkspaceId",
    name="live-stream-collections",
    video_source_id="67bea1d66ca0059a95bf7de9",
)
```

### Delete Workspace

Delete the live stream workspace.

| Direction | Type |
| --- | --- |
| Response | [`LiveStreamWorkspaceDeleteResponse`](./src/gumlet/types/live_stream_workspace_delete_response.py) |

```python
live_stream_workspace = client.live_stream_workspaces.delete(
    live_workspace_id="liveWorkspaceId",
)
```

## `LiveStreamAnalytics`

Get usage analytics for live streams.

### Usage Analytics

Get usage analytics for your live streams.

| Direction | Type |
| --- | --- |
| Request | [`LiveStreamAnalyticUsageParams`](./src/gumlet/types/live_stream_analytic_usage_params.py) |
| Response | [`LiveStreamAnalyticUsageResponse`](./src/gumlet/types/live_stream_analytic_usage_response.py) |

```python
live_stream_analytic = client.live_stream_analytics.usage(
    date_range={"start_at": "2024-01-01", "end_at": "2024-01-01"},
    group_by="daily",
    metrics=["bandwidth_consumption"],
)
```
