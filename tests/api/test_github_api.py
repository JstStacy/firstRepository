import pytest
import requests
from modules.api.clients.github import GitHub

# Create tests for GitHub API
@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('anastasiiataran')
    assert r['message'] == 'Not Found'  

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 43
    assert 'become-qa-auto' in r['items'][0]['name']
   
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('anastasiiataran_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

# Start of individual part
@pytest.mark.api
def test_combined_status_for_a_specific_reference(github_api):
    r = github_api.get_a_combined_status('JstStacy','firstRepository', 'c7cee272b4e5d938ca0d86210900aeb05e7853c5')
    assert r['state'] == 'pending'

@pytest.mark.api
def test_combined_status_for_non_exicting_reference(github_api):
    r = github_api.get_a_combined_status('JstStacy','firstRepository', 'ascee274e5d938ca0d86210900aeb05e7853c5')
    assert r['message'] == 'Ref not found'

@pytest.mark.api
def test_combined_status_for_non_exicting_user(github_api):
    r = github_api.get_a_combined_status('anastasiiataran','firstRepository', 'ascee274e5d938ca0d86210900aeb05e7853c5')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_emojis(github_api):
    r = github_api.get_emojis()
    assert r['100'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f4af.png?v8'




