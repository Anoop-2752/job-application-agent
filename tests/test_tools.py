from tools.search import search_jobs


def test_search_jobs_returns_results():
    results = search_jobs("Tata Elxsi", "AI ML engineer")
    assert isinstance(results, list)
    assert len(results) > 0
    assert "company" in results[0]


def test_search_jobs_has_required_keys():
    results = search_jobs("Netradyne", "computer vision engineer")
    for result in results:
        assert "company" in result


def test_search_jobs_wrong_company_does_not_crash():
    results = search_jobs("xyzcompanythatdoesnotexist12345")
    assert isinstance(results, list)  # should return empty list, not crash