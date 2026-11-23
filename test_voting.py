from voting import is_eligible


def test_eligible_person():
    assert is_eligible(20)


def test_ineligible_person():
    assert not is_eligible(15)
