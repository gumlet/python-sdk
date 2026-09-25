# Changelog

## [1.0.8](https://github.com/gumlet/python-sdk/compare/v1.0.6...v1.0.8) (2026-09-25)


### Features

* **api:** add operation multipartUpload.abort (+1 more change) ([4812260](https://github.com/gumlet/python-sdk/commit/48122605f0f8ced3cde4a9b78875eaa3c95e6e45))


### Chores

* **api:** regenerate SDK ([a1f8ed9](https://github.com/gumlet/python-sdk/commit/a1f8ed9cb0fad9a745954b62d8e74841cba483d4))
* release 1.0.8 ([f27dc4b](https://github.com/gumlet/python-sdk/commit/f27dc4bb85be957747f9193ac92f99c42d24737e))
* release 1.0.8 ([aecfd81](https://github.com/gumlet/python-sdk/commit/aecfd81e9034a21fda71e42c7708e600da693579))

## [1.0.6](https://github.com/gumlet/python-sdk/compare/v1.0.5...v1.0.6) (2026-09-21)


### Chores

* **api:** update generated SDK content ([2eb4c7e](https://github.com/gumlet/python-sdk/commit/2eb4c7e2e70a942e6a70cb823778971720fca95b))
* **api:** update generated SDK content ([687091f](https://github.com/gumlet/python-sdk/commit/687091f7e8d5d5b3ad53cf7903d2994b9fae851c))
* **api:** update generated SDK content ([7a90920](https://github.com/gumlet/python-sdk/commit/7a9092023d74162fad2033615b58a76952866d9e))

## [1.0.5](https://github.com/gumlet/python-sdk/compare/v1.0.4...v1.0.5) (2026-09-21)


### ⚠ BREAKING CHANGES

* **api:** 187 breaking changes to the SDK surface.
    - `401` error response of `videoAssets.create` changed from `application/json` to `error`.
    - `403` error response of `videoAssets.create` changed from `application/json` to `error`.
    - `422` error response of `videoAssets.create` changed from `application/json` to `error`.
    - `500` error response of `videoAssets.create` changed from `application/json` to `error`.
    - `403` error response of `videoAssets.upload` changed from `application/json` to `error`.
    - `422` error response of `videoAssets.upload` changed from `application/json` to `error`.
    - `500` error response of `videoAssets.upload` changed from `application/json` to `error`.
    - `403` error response of `videoAssets.delete` changed from `application/json` to `error`.
    - `401` error response of `videoAssets.update` changed from `application/json` to `error`.
    - `403` error response of `videoAssets.update` changed from `application/json` to `error`.
    - `422` error response of `videoAssets.update` changed from `application/json` to `error`.
    - `401` error response of `videoAssets.thumbnailSelect` changed from `application/json` to `error`.
    - `403` error response of `videoAssets.thumbnailSelect` changed from `application/json` to `error`.
    - `500` error response of `videoAssets.thumbnailSelect` changed from `application/json` to `error`.
    - `401` error response of `videoAssets.thumbnailUpload` changed from `application/json` to `error`.
    - `403` error response of `videoAssets.thumbnailUpload` changed from `application/json` to `error`.
    - `500` error response of `videoAssets.thumbnailUpload` changed from `application/json` to `error`.
    - `401` error response of `videoAssets.createUpdateChapter` changed from `application/json` to `error`.
    - `403` error response of `videoAssets.createUpdateChapter` changed from `application/json` to `error`.
    - `500` error response of `videoAssets.createUpdateChapter` changed from `application/json` to `error`.
    - `401` error response of `videoAssets.list` changed from `application/json` to `error`.
    - `403` error response of `videoAssets.list` changed from `application/json` to `error`.
    - `403` error response of `videoAssets.listDeprecated` changed from `application/json` to `error`.
    - `401` error response of `videoAssets.deleteMany` changed from `application/json` to `error`.
    - `403` error response of `videoAssets.deleteMany` changed from `application/json` to `error`.
    - `500` error response of `videoAssets.deleteMany` changed from `application/json` to `error`.
    - `401` error response of `videoAssets.tagMany` changed from `application/json` to `error`.
    - `403` error response of `videoAssets.tagMany` changed from `application/json` to `error`.
    - `500` error response of `videoAssets.tagMany` changed from `application/json` to `error`.
    - `401` error response of `videoAssets.analytics` changed from `application/json` to `error`.
    - `403` error response of `videoAssets.analytics` changed from `application/json` to `error`.
    - `500` error response of `videoAssets.analytics` changed from `application/json` to `error`.
    - `401` error response of `subtitleUpload.upload` changed from `application/json` to `error`.
    - `403` error response of `subtitleUpload.upload` changed from `application/json` to `error`.
    - `500` error response of `subtitleUpload.upload` changed from `application/json` to `error`.
    - `401` error response of `subtitleUpload.complete` changed from `application/json` to `error`.
    - `403` error response of `subtitleUpload.complete` changed from `application/json` to `error`.
    - `500` error response of `subtitleUpload.complete` changed from `application/json` to `error`.
    - `401` error response of `audioUpload.upload` changed from `application/json` to `error`.
    - `403` error response of `audioUpload.upload` changed from `application/json` to `error`.
    - `500` error response of `audioUpload.upload` changed from `application/json` to `error`.
    - `401` error response of `audioUpload.complete` changed from `application/json` to `error`.
    - `403` error response of `audioUpload.complete` changed from `application/json` to `error`.
    - `500` error response of `audioUpload.complete` changed from `application/json` to `error`.
    - `401` error response of `videoUsageAnalytics.retrieve` changed from `application/json` to `error`.
    - `403` error response of `videoUsageAnalytics.retrieve` changed from `application/json` to `error`.
    - `401` error response of `videoUsageAnalytics.topAssets` changed from `application/json` to `error`.
    - `403` error response of `videoUsageAnalytics.topAssets` changed from `application/json` to `error`.
    - `401` error response of `multipartUpload.retrievePartUrl` changed from `application/json` to `error`.
    - `403` error response of `multipartUpload.retrievePartUrl` changed from `application/json` to `error`.
    - `401` error response of `multipartUpload.complete` changed from `application/json` to `error`.
    - `403` error response of `multipartUpload.complete` changed from `application/json` to `error`.
    - `403` error response of `videoProfiles.create` changed from `application/json` to `error`.
    - `422` error response of `videoProfiles.create` changed from `application/json` to `error`.
    - `500` error response of `videoProfiles.create` changed from `application/json` to `error`.
    - `401` error response of `videoProfiles.list` changed from `application/json` to `error`.
    - `403` error response of `videoProfiles.list` changed from `application/json` to `error`.
    - `401` error response of `videoProfiles.update` changed from `application/json` to `error`.
    - `403` error response of `videoProfiles.update` changed from `application/json` to `error`.
    - `500` error response of `videoProfiles.update` changed from `application/json` to `error`.
    - `403` error response of `videoProfiles.retrieve` changed from `application/json` to `error`.
    - `403` error response of `videoProfiles.delete` changed from `application/json` to `error`.
    - `401` error response of `videoPlaylists.create` changed from `application/json` to `error`.
    - `403` error response of `videoPlaylists.create` changed from `application/json` to `error`.
    - `422` error response of `videoPlaylists.create` changed from `application/json` to `error`.
    - `401` error response of `videoPlaylists.listAll` changed from `application/json` to `error`.
    - `403` error response of `videoPlaylists.listAll` changed from `application/json` to `error`.
    - `401` error response of `videoPlaylists.createAsset` changed from `application/json` to `error`.
    - `403` error response of `videoPlaylists.createAsset` changed from `application/json` to `error`.
    - `401` error response of `videoPlaylists.deleteAsset` changed from `application/json` to `error`.
    - `403` error response of `videoPlaylists.deleteAsset` changed from `application/json` to `error`.
    - `401` error response of `videoPlaylists.update` changed from `application/json` to `error`.
    - `403` error response of `videoPlaylists.update` changed from `application/json` to `error`.
    - `401` error response of `videoPlaylists.delete` changed from `application/json` to `error`.
    - `403` error response of `videoPlaylists.delete` changed from `application/json` to `error`.
    - `401` error response of `videoPlaylists.listAssets` changed from `application/json` to `error`.
    - `403` error response of `videoPlaylists.listAssets` changed from `application/json` to `error`.
    - `401` error response of `videoPlaylists.reorderAsset` changed from `application/json` to `error`.
    - `403` error response of `videoPlaylists.reorderAsset` changed from `application/json` to `error`.
    - `401` error response of `webhooks.create` changed from `application/json` to `error`.
    - `403` error response of `webhooks.create` changed from `application/json` to `error`.
    - `422` error response of `webhooks.create` changed from `application/json` to `error`.
    - `401` error response of `webhooks.list` changed from `application/json` to `error`.
    - `403` error response of `webhooks.list` changed from `application/json` to `error`.
    - `401` error response of `webhooks.update` changed from `application/json` to `error`.
    - `403` error response of `webhooks.update` changed from `application/json` to `error`.
    - `401` error response of `webhooks.delete` changed from `application/json` to `error`.
    - `403` error response of `webhooks.delete` changed from `application/json` to `error`.
    - `401` error response of `webhooks.history` changed from `application/json` to `error`.
    - `403` error response of `webhooks.history` changed from `application/json` to `error`.
    - `401` error response of `imageSources.create` changed from `application/json` to `error`.
    - `422` error response of `imageSources.create` changed from `application/json` to `error`.
    - `401` error response of `imageSources.list` changed from `application/json` to `error`.
    - `403` error response of `imageSources.list` changed from `application/json` to `error`.
    - `401` error response of `imageSources.retrieve` changed from `application/json` to `error`.
    - `403` error response of `imageSources.retrieve` changed from `application/json` to `error`.
    - `401` error response of `imageSources.update` changed from `application/json` to `error`.
    - `403` error response of `imageSources.update` changed from `application/json` to `error`.
    - `401` error response of `imageSources.delete` changed from `application/json` to `error`.
    - `403` error response of `imageSources.delete` changed from `application/json` to `error`.
    - `401` error response of `imageSources.purgeCache` changed from `application/json` to `error`.
    - `403` error response of `imageSources.purgeCache` changed from `application/json` to `error`.
    - `401` error response of `imageSources.purge` changed from `application/json` to `error`.
    - `403` error response of `imageSources.purge` changed from `application/json` to `error`.
    - `401` error response of `imageUsageAnalytics.retrieve` changed from `application/json` to `error`.
    - `403` error response of `imageUsageAnalytics.retrieve` changed from `application/json` to `error`.
    - `422` error response of `liveStreamAssets.create` changed from `application/json` to `error`.
    - `403` error response of `liveStreamAssets.update` changed from `application/json` to `error`.
    - `403` error response of `liveStreamAssets.retrieveStatus` changed from `application/json` to `error`.
    - `403` error response of `liveStreamAssets.delete` changed from `application/json` to `error`.
    - `403` error response of `liveStreamAssets.complete` changed from `application/json` to `error`.
    - `403` error response of `liveStreamAssets.filter` changed from `application/json` to `error`.
    - `401` error response of `liveStreamAssets.start` changed from `application/json` to `error`.
    - `403` error response of `liveStreamAssets.start` changed from `application/json` to `error`.
    - `401` error response of `liveStreamAssets.upload` changed from `application/json` to `error`.
    - `500` error response of `liveStreamAssets.upload` changed from `application/json` to `error`.
    - `403` error response of `liveStreamAssets.statusHistory` changed from `application/json` to `error`.
    - `401` error response of `recycleBin.recover` changed from `application/json` to `error`.
    - `403` error response of `recycleBin.recover` changed from `application/json` to `error`.
    - `401` error response of `recycleBin.list` changed from `application/json` to `error`.
    - `403` error response of `recycleBin.list` changed from `application/json` to `error`.
    - `401` error response of `videoWorkspaces.list` changed from `application/json` to `error`.
    - `403` error response of `videoWorkspaces.list` changed from `application/json` to `error`.
    - `401` error response of `videoWorkspaces.create` changed from `application/json` to `error`.
    - `422` error response of `videoWorkspaces.create` changed from `application/json` to `error`.
    - `401` error response of `videoWorkspaces.update` changed from `application/json` to `error`.
    - `403` error response of `videoWorkspaces.update` changed from `application/json` to `error`.
    - `401` error response of `videoWorkspaces.retrieve` changed from `application/json` to `error`.
    - `403` error response of `videoWorkspaces.retrieve` changed from `application/json` to `error`.
    - `401` error response of `videoWorkspaces.delete` changed from `application/json` to `error`.
    - `403` error response of `videoWorkspaces.delete` changed from `application/json` to `error`.
    - `401` error response of `folders.create` changed from `application/json` to `error`.
    - `403` error response of `folders.create` changed from `application/json` to `error`.
    - `422` error response of `folders.create` changed from `application/json` to `error`.
    - `401` error response of `folders.list` changed from `application/json` to `error`.
    - `403` error response of `folders.list` changed from `application/json` to `error`.
    - `401` error response of `folders.retrieve` changed from `application/json` to `error`.
    - `403` error response of `folders.retrieve` changed from `application/json` to `error`.
    - `401` error response of `folders.update` changed from `application/json` to `error`.
    - `403` error response of `folders.update` changed from `application/json` to `error`.
    - `401` error response of `folders.delete` changed from `application/json` to `error`.
    - `403` error response of `folders.delete` changed from `application/json` to `error`.
    - `401` error response of `folders.deleteAssets` changed from `application/json` to `error`.
    - `403` error response of `folders.deleteAssets` changed from `application/json` to `error`.
    - `401` error response of `channelViewers.invite` changed from `application/json` to `error`.
    - `403` error response of `channelViewers.invite` changed from `application/json` to `error`.
    - `401` error response of `channelViewers.delete` changed from `application/json` to `error`.
    - `403` error response of `channelViewers.delete` changed from `application/json` to `error`.
    - `401` error response of `channelViewers.inviteCsv` changed from `application/json` to `error`.
    - `403` error response of `channelViewers.inviteCsv` changed from `application/json` to `error`.
    - `401` error response of `channelViewers.listSubscribers` changed from `application/json` to `error`.
    - `403` error response of `channelViewers.listSubscribers` changed from `application/json` to `error`.
    - `403` error response of `videoAnalytics.chartData` changed from `application/json` to `error`.
    - `500` error response of `videoAnalytics.chartData` changed from `application/json` to `error`.
    - `403` error response of `videoAnalytics.breakdownData` changed from `application/json` to `error`.
    - `500` error response of `videoAnalytics.breakdownData` changed from `application/json` to `error`.
    - `403` error response of `videoAnalytics.aggregatedData` changed from `application/json` to `error`.
    - `500` error response of `videoAnalytics.aggregatedData` changed from `application/json` to `error`.
    - `401` error response of `organizationData.fetchOrg` changed from `application/json` to `error`.
    - `403` error response of `organizationData.fetchOrg` changed from `application/json` to `error`.
    - `401` error response of `userData.fetch` changed from `application/json` to `error`.
    - `403` error response of `userData.fetch` changed from `application/json` to `error`.
    - `401` error response of `auditLogs.fetch` changed from `application/json` to `error`.
    - `403` error response of `auditLogs.fetch` changed from `application/json` to `error`.
    - `422` error response of `auditLogs.fetch` changed from `application/json` to `error`.
    - `401` error response of `billing.listInvoices` changed from `application/json` to `error`.
    - `403` error response of `billing.listInvoices` changed from `application/json` to `error`.
    - `401` error response of `billing.fetchDetails` changed from `application/json` to `error`.
    - `403` error response of `billing.fetchDetails` changed from `application/json` to `error`.
    - `401` error response of `billing.updateDetails` changed from `application/json` to `error`.
    - `403` error response of `billing.updateDetails` changed from `application/json` to `error`.
    - `500` error response of `billing.updateDetails` changed from `application/json` to `error`.
    - `401` error response of `billing.fetchUpcomingInvoice` changed from `application/json` to `error`.
    - `403` error response of `billing.fetchUpcomingInvoice` changed from `application/json` to `error`.
    - `500` error response of `billing.fetchUpcomingInvoice` changed from `application/json` to `error`.
    - `401` error response of `liveStreamWorkspaces.list` changed from `application/json` to `error`.
    - `403` error response of `liveStreamWorkspaces.list` changed from `application/json` to `error`.
    - `401` error response of `liveStreamWorkspaces.create` changed from `application/json` to `error`.
    - `422` error response of `liveStreamWorkspaces.create` changed from `application/json` to `error`.
    - `401` error response of `liveStreamWorkspaces.update` changed from `application/json` to `error`.
    - `403` error response of `liveStreamWorkspaces.update` changed from `application/json` to `error`.
    - `401` error response of `liveStreamWorkspaces.delete` changed from `application/json` to `error`.
    - `403` error response of `liveStreamWorkspaces.delete` changed from `application/json` to `error`.
    - `401` error response of `liveStreamAnalytics.usage` changed from `application/json` to `error`.
    - `403` error response of `liveStreamAnalytics.usage` changed from `application/json` to `error`.
    - `401` error response of `globalSearch.search` changed from `application/json` to `error`.
    - `403` error response of `globalSearch.search` changed from `application/json` to `error`.
* **api:** 4 breaking changes to the SDK surface.
    - `400` error response of `videoAssets.deleteMany` changed from `none` to `application/json`.
    - `400` error response of `videoAssets.tagMany` changed from `none` to `application/json`.
    - `400` error response of `userData.fetch` changed from `none` to `application/json`.
    - `400` error response of `liveStreamAnalytics.usage` changed from `none` to `application/json`.

### Features

* **api:** update SDK surface (188 changes) ([48d33e8](https://github.com/gumlet/python-sdk/commit/48d33e8cb141ee71cf27713864695f327662238a))
* **api:** update SDK surface (240 changes) ([a87c378](https://github.com/gumlet/python-sdk/commit/a87c3783e35373327132e0b290d22b19db9ad583))


### Chores

* **api:** update generated SDK content ([03ed245](https://github.com/gumlet/python-sdk/commit/03ed24554589fd44a92604dc5368987921e998a9))
* release 1.0.5 ([5ce3d44](https://github.com/gumlet/python-sdk/commit/5ce3d44a0a184bf576618251703b7684d8d04877))
* release 1.0.5 ([1c1b6ee](https://github.com/gumlet/python-sdk/commit/1c1b6ee81f378775e469dc592a9f079cb64e3eed))

## [1.0.4](https://github.com/gumlet/python-sdk/compare/v1.0.2...v1.0.4) (2026-09-21)


### ⚠ BREAKING CHANGES

* **api:** 2 breaking changes to the SDK surface.
    - Added required body field `workspace_id` to `videoAssets.create`.
    - Removed body field `collection_id` from `videoAssets.create`.

### Features

* **api:** update SDK surface (2 changes) ([6df7d37](https://github.com/gumlet/python-sdk/commit/6df7d37ce176c7953e00a5abb7d0cb926338764e))


### Chores

* **api:** update generated SDK content ([05aee94](https://github.com/gumlet/python-sdk/commit/05aee9405ac0fb7e03a0d9da89ac08c072552842))
* release 1.0.4 ([9413867](https://github.com/gumlet/python-sdk/commit/94138671b8c19e1756d9ff4edf636d8539aa1684))
* release 1.0.4 ([185bd62](https://github.com/gumlet/python-sdk/commit/185bd626d99028b521bf5d612390fdcf238d4159))

## [1.0.2](https://github.com/gumlet/python-sdk/compare/v1.0.1...v1.0.2) (2026-09-21)


### Chores

* **api:** regenerate SDK ([425e252](https://github.com/gumlet/python-sdk/commit/425e25222ebda0df8fb7b62d9a78805c07a5aeae))

## [1.0.1](https://github.com/gumlet/python-sdk/compare/v1.0.0...v1.0.1) (2026-09-21)


### Chores

* **api:** update generated SDK content ([c2292f5](https://github.com/gumlet/python-sdk/commit/c2292f53d0f12751ba308ba9490119ae33f3ea37))

## [1.0.0](https://github.com/gumlet/python-sdk/compare/v0.3.0...v1.0.0) (2026-09-21)


### Features

* **api:** add operation globalSearch.search ([c9a2c9e](https://github.com/gumlet/python-sdk/commit/c9a2c9e615154d7b6e4cf94944921dd5d2b1b817))


### Chores

* **api:** update generated SDK content ([845699d](https://github.com/gumlet/python-sdk/commit/845699da69cc1f5c42598ca4c79b3887abf4035d))
* **api:** update generated SDK content ([291aea8](https://github.com/gumlet/python-sdk/commit/291aea8216202666d891c685212a501fda5b8845))
* **api:** update generated SDK content ([8580466](https://github.com/gumlet/python-sdk/commit/8580466d1130c2031af0bf9e9bbdea9393d1db67))
* release 1.0.0 ([d7118c8](https://github.com/gumlet/python-sdk/commit/d7118c81f86075f054d1a0922435d638b2fcd553))
* release 1.0.0 ([0bbcd73](https://github.com/gumlet/python-sdk/commit/0bbcd73e3fc8a463601854168acfb72f780b68de))

## [0.3.0](https://github.com/gumlet/python-sdk/compare/v0.2.0...v0.3.0) (2026-09-21)


### Features

* **api:** add operation liveStreamAnalytics.usage ([ac60a30](https://github.com/gumlet/python-sdk/commit/ac60a305166b5bcd069f543f67c4a40308d71331))


### Chores

* **api:** regenerate SDK ([02bd3cb](https://github.com/gumlet/python-sdk/commit/02bd3cb58ad9d5bd2f46b0baf29ef9e29e5d4b7a))
* **api:** update generated SDK content ([04b0f2e](https://github.com/gumlet/python-sdk/commit/04b0f2eb66043f416c7779a5507efa648258287a))
* **api:** update generated SDK content ([82f24bf](https://github.com/gumlet/python-sdk/commit/82f24bf8486f195dfc974657c8bb7d40419b1a6d))

## [0.2.0](https://github.com/gumlet/python-sdk/compare/v0.1.0...v0.2.0) (2026-09-18)


### Features

* **api:** initial SDK generation ([860d43a](https://github.com/gumlet/python-sdk/commit/860d43a0575952e5e8d658b65f4f99c332b7af59))
