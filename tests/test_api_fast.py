from api.smr_api import save_search

def test_save_search():
    res = save_search(search_input='test',
                    postcode='test',
                    count_search=1,
                    max_roof_id_number=1,
                    max_roof_area=1,
                    max_roof_number_panels=1,
                    total_count_roofs=1,
                    total_count_panels=5)
    assert res['total_count_panels'] == 5

# test_save_search()
