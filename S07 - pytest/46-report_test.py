import json
import report
import pytest


@pytest.fixture
def report_json():
    print("\n[ Fixture ]: requested...")
    report.generate_report()

    with open("report.json") as file:
        print("[ Fixture ]: ...return report data")
        return json.load(file)


def test_report_json(report_json):
    print("[ Test ]: recieved -", report_json)
    assert type(report_json) == dict


def test_report_fields(report_json):
    print("[ Test ]: recieved -", report_json)
    assert "timestamp" in report_json
    assert "status" in report_json