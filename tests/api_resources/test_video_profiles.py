# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestVideoProfiles:
    @smoke_case("videoProfiles.create:required", operation="create", path="/video/profiles")
    def test_method_create(self) -> None:
        video_profile = client.video_profiles.create(
            name="Gumlet-Profile-1",
            format="ABR",
            transcribe=False,
            idempotency_key="",
        )

    @smoke_case("videoProfiles.create:all", operation="create", path="/video/profiles")
    def test_method_create_with_all_params(self) -> None:
        video_profile = client.video_profiles.create(
            name="Gumlet-Profile-1",
            format="ABR",
            width="",
            height="",
            resolution="",
            crop={"horizontal_margin": "", "vertical_margin": "", "width": "", "height": ""},
            pad={"top": "", "left": "", "bottom": "", "right": "", "color": ""},
            trim={"start_offset": 0, "end_offset": 0, "duration": 0},
            image_overlay={
                "url": "",
                "horizontal_margin": "",
                "vertical_margin": "",
                "horizontal_align": "",
                "vertical_align": "",
                "width": "",
                "height": "",
            },
            text_overlay={
                "text": "",
                "horizontal_align": "",
                "vertical_align": "",
                "horizontal_margin": "",
                "vertical_margin": "",
                "color": "",
                "font": "",
                "font_size": "",
                "opacity": "",
                "box": False,
                "box_color": "",
                "box_opacity": "",
                "box_border": "",
            },
            animated_gif={"start_offset": "", "end_offset": "", "width": "", "height": "", "fps": ""},
            generate_subtitles={"subtitle_languages": ""},
            transcribe=False,
            mp4_access=False,
            per_title_encoding=False,
            process_low_resolution_input=False,
            audio_only=False,
            enable_drm=False,
            idempotency_key="",
        )

    @smoke_case("videoProfiles.list:required", operation="list", path="/video/profiles")
    def test_method_list(self) -> None:
        video_profile = client.video_profiles.list(
            page_number=1,
            page_size=20,
        )

    @smoke_case("videoProfiles.list:all", operation="list", path="/video/profiles")
    def test_method_list_with_all_params(self) -> None:
        video_profile = client.video_profiles.list(
            page_number=1,
            page_size=20,
            next_page_token="next_page_token",
        )

    @smoke_case("videoProfiles.update:required", operation="update", path="/video/profiles/{profile_id}")
    def test_method_update(self) -> None:
        video_profile = client.video_profiles.update(
            path_profile_id="profileId",
            body_profile_id="",
            format="ABR",
            transcribe=False,
            vc=["libx264"],
            idempotency_key="",
        )

    @smoke_case("videoProfiles.update:all", operation="update", path="/video/profiles/{profile_id}")
    def test_method_update_with_all_params(self) -> None:
        video_profile = client.video_profiles.update(
            path_profile_id="profileId",
            body_profile_id="",
            name="",
            format="ABR",
            width="",
            height="",
            resolution="",
            crop={"horizontal_margin": "", "vertical_margin": "", "width": "", "height": ""},
            pad={"top": "", "left": "", "bottom": "", "right": "", "color": ""},
            trim={"start_offset": 0, "end_offset": 0, "duration": 0},
            image_overlay={
                "url": "",
                "horizontal_margin": "",
                "vertical_margin": "",
                "horizontal_align": "",
                "vertical_align": "",
                "width": "",
                "height": "",
            },
            text_overlay={
                "text": "",
                "horizontal_align": "",
                "vertical_align": "",
                "horizontal_margin": "",
                "vertical_margin": "",
                "color": "",
                "font": "",
                "font_size": "",
                "opacity": "",
                "box": False,
                "box_color": "",
                "box_opacity": "",
                "box_border": "",
            },
            animated_gif={"start_offset": "", "end_offset": "", "width": "", "height": "", "fps": ""},
            generate_subtitles={"subtitle_languages": [""]},
            transcribe=False,
            mp4_access=False,
            per_title_encoding=False,
            process_low_resolution_input=False,
            audio_only=False,
            enable_drm=False,
            vc=["libx264"],
            generate_chapters=False,
            generate_description=False,
            idempotency_key="",
        )

    @smoke_case("videoProfiles.retrieve:single", operation="retrieve", path="/video/profiles/{profile_id}")
    def test_method_retrieve(self) -> None:
        video_profile = client.video_profiles.retrieve(
            profile_id="profileId",
        )

    @smoke_case("videoProfiles.delete:single", operation="delete", path="/video/profiles/{profile_id}")
    def test_method_delete(self) -> None:
        video_profile = client.video_profiles.delete(
            profile_id="profileId",
            idempotency_key="",
        )
