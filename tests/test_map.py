from app import config
from app.map import Map
from app.cells import BlueCell, RedCell, NeutralCell
from app.utils import resource


def test_map_as_emoji():
    words = resource.words(config.DEFAULT_WORD_LIST_NAME)
    map_ = Map.random(words=words)

    assert {
        config.EMOJI_BLUE_HEART,
        config.EMOJI_RED_HEART,
        config.EMOJI_GREEN_HEART,
        config.EMOJI_BLACK_HEART,
    } == {cell.emoji for row in map_.cells for cell in row}


def test_map_as_keyboard():
    words = resource.words(config.DEFAULT_WORD_LIST_NAME)
    map_ = Map.random(words=words)
    assert config.BUTTON_COLOR_DEFAULT in map_.as_keyboard().dump()

    cell = map_.cells[0][0]
    cell.flip()

    assert cell.button_color in map_.as_keyboard().dump()


def test_all_flipped():
    b0 = BlueCell("b0")
    b1 = BlueCell("b1")
    n0 = NeutralCell("r0")
    r0 = RedCell("r1")
    cells = [[b0, b1], [n0, r0]]
    map_ = Map(cells)
    assert not map_.all_flipped(BlueCell)
    assert not map_.all_flipped(RedCell)
    assert not map_.all_flipped(NeutralCell)

    b0.flip()
    assert b0.flipped
    assert not map_.all_flipped(BlueCell)
    assert not map_.all_flipped(RedCell)
    assert not map_.all_flipped(NeutralCell)

    n0.flip()
    assert n0.flipped
    assert not map_.all_flipped(BlueCell)
    assert not map_.all_flipped(RedCell)
    assert map_.all_flipped(NeutralCell)

    b1.flip()
    assert b1.flipped
    assert map_.all_flipped(BlueCell)
    assert not map_.all_flipped(RedCell)
    assert map_.all_flipped(NeutralCell)

    r0.flip()
    assert r0.flipped
    assert map_.all_flipped(BlueCell)
    assert map_.all_flipped(RedCell)
    assert map_.all_flipped(NeutralCell)
