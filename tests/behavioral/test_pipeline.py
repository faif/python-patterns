from patterns.behavioral.pipeline import Pipeline, filter_stage, map_stage, take


def test_pipeline_composes_stages_lazily():
    p = Pipeline((
        filter_stage(lambda x: x % 2 == 1),
        map_stage(lambda x: x + 10),
        take(4),
    ))

    assert list(p(range(100))) == [11, 13, 15, 17]


def test_take_rejects_negative():
    try:
        take(-1)
        assert False, "Expected ValueError"
    except ValueError:
        assert True
