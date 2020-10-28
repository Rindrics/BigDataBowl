from plays import fill_personnel, extract_positions, extract_numbers
import pytest


@pytest.mark.parametrize(
    'personnel, all_positions, expect',
    [('2AB, 1CD', {'AB', 'BC', 'CD'}, 'AB 2, BC 0, CD 1'),
     ('4 DL, 2 LB, 5 DB',
      {'DB', 'DL', 'K', 'LB', 'LS', 'OL', 'P', 'QB', 'RB', 'TE', 'WR'},
      'DB 5, DL 4, K 0, LB 2, LS 0, OL 0, P 0, QB 0, RB 0, TE 0, WR 0')])
def test_fill_personnel(personnel, all_positions, expect):
    assert fill_personnel(personnel, all_positions) == expect


def test_extract_positions():
    assert extract_positions('4 DL, 2 LB, 5 DB') == ['DL', 'LB', 'DB']


def test_extract_numbers():
    assert extract_numbers('4 DL, 2 LB, 5 DB') == ['4', '2', '5']
