from pages.feature_page import FeaturePage

def test_p3_spotify_search_arijit_singh(page):
    feature = FeaturePage(page)
    feature.open('https://open.spotify.com')
    feature.search('arijit singh')
    feature.submit_search()
    feature.wait_for_results()
    feature.screenshot('result.png')