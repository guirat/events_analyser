import pytest
from retrieve_data.views import create_event_count


@pytest.mark.parametrize(
    "events",
    [(
            [
                {
                    "timestamp": 1594887666,
                    "id": "ebc76a00-4338-4138-925b-f3a4d9a5820e",
                    "event": "video_25"
                },
                {
                    "timestamp": 1594894866,
                    "id": "999427f4-608c-4f40-a979-01f1ca68cbc1",
                    "event": "impressions"
                }
            ]
    )])
def test_create_event_count(events):
    df = create_event_count(events)
    index = list(df.index)
    items = [str(item) for item in index]
    assert items == ['(1594887665, 1594891265]', '(1594891265, 1594894865]', '(1594894865, 1594898465]']
    assert list(df['impressions']) == [0, 0, 1]
    assert list(df['video_25']) == [1, 0, 0]
