    from main import YDisk
    from main import recording_yd
    import requests
    import pytest

    class TestAPIYadex:
        def test_create_folder_yd_1(self):
            path = '1111'
            excepted = 201
            yd_photos = YDisk()
            result = yd_photos.recording_yd(path)
            assert excepted == result

        def test_create_folder_yd_1(self):
            path = '1111'
            excepted = 409
            yd_photos = YDisk()
            result = yd_photos.recording_yd(path)
            assert excepted == result