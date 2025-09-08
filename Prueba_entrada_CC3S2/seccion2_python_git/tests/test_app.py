import pytest
from app.app import summarize

@pytest.fixture
def sample():
    return ["1", "2", "3"]

def test_ok(sample):
    # Arrange–Act–Assert
    # Act
    result = summarize(sample)
    assert result["count"] == 3
    assert result["sum"] == 6.0
    assert result["avg"] == 2.0

def test_empty():
    with pytest.raises(ValueError):
        summarize([])

def test_non_numeric():
    with pytest.raises(ValueError):
        summarize(["a", "2"])