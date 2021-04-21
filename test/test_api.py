import requests
import pytest


class TestsBase:
    def test_upload(self, api):
        s = api.model.generate_template()
        r = api.request_send(method="POST", file=str(s))
        assert r.status_code == 201
        assert s and "Template successfully uploaded" in r.text

    def test_get_templates(self, api):
        r = api.request_send(method="GET")
        assert r.status_code == 200
        assert "templates" in r.text

    def test_install(self, api):
        s = api.model.generate_template()
        r = api.request_send(method="POST", file=str(s))
        r = api.request_send(method="POST", url=f'/{s}/install')
        assert r.status_code == 200
        assert s and "successfully installed" in r.text

    def test_delete_template(self, api):
        s = api.model.generate_template()
        r = api.request_send(method="POST", file=str(s))
        r = api.request_send(method="DELETE", url=f'/{s}')
        assert r.status_code == 200
        assert s and "successfully deleted" in r.text

    @pytest.mark.parametrize('buttons', range(1, 5))
    def test_multiple_upload(self, api, buttons):
        s = api.model.generate_template(buttons)
        r = api.request_send(method="POST", file=str(s))
        assert r.status_code == 201
        assert s and "Template successfully uploaded" in r.text

    @pytest.mark.parametrize('buttons', range(1, 5))
    def test_multiple_install(self, api, buttons):
        s = api.model.generate_template(buttons)
        r = api.request_send(method="POST", file=str(s))
        r = api.request_send(method="POST", url=f'/{s}/install')
        assert r.status_code == 200
        assert s and "successfully installed" in r.text

    def test_multiple_deletions(self, api):
        r = api.request_send(method="GET")
        s = api.get_array(r)
        if len(s["templates"]) > 2:
            for i in s["templates"]:
                r = api.request_send("DELETE", url=f'/{i}')
                assert r.status_code == 200
                assert s and "successfully deleted" in r.text
        else:
            for i in range(1, 5):
                s = api.model.generate_template()
                r = api.request_send(method="POST", file=str(s))
            r = api.request_send(method="GET")
            s = api.get_array(r)
            for i in s["templates"]:
                r = api.request_send("DELETE", url=f'/{i}')
                assert r.status_code == 200
                assert s and "successfully deleted" in r.text

    def test_upload_wrong_file(self, api):
        s = api.model.generate_wrong_template()
        r = api.request_send(method="POST", file=str(s))
        print(r.text)
        assert r.status_code == 400

    def test_upload_worng_format(self, api):
        s = api.model.generate_wrong_format()
        r = api.request_send(method="POST", file=str(s))
        print(r.text)
        assert r.status_code == 400