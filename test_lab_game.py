from unittest.mock import Mock
from lab_game import get_random_item, award_badge

# The tests for get_random_item and award_badge functions
def test_get_random_item():
    # Create a mock random generator and set it 
    fake_rng = Mock()
    fake_rng.choice.return_value = "sword"

     # Call get_random_item with your mock as the rng argument
    result = get_random_item("Sham", rng = fake_rng)
    # Assert the full return string
    assert result == "Sham found a sword"
    fake_rng.choice.assert_called_once_with(["sword", "shield", "potion"])


# The test for award_badge function
def test_award_badge():
    # Create a mock logger
    fake_logger = Mock()
    # Call award_badge with your mock logger
    result = award_badge("Papi", "Papa Pickle", logger = fake_logger)
    # Assert that the function returns None and that logger.log correctly
    assert result is None
    fake_logger.log.assert_called_once_with("Papi earned Papa Pickle")