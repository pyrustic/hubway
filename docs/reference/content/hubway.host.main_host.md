
Back to [Reference Overview](https://github.com/pyrustic/hubway/blob/master/docs/reference/README.md)

# hubway.host.main\_host



<br>


```python

class MainHost:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    @property
    def login(self):
        """
        
        """

    def about_target_project(self):
        """
        Returns a dict:
        {"target": str, "project_name": str, "version": str}
        """

    def auth(self, token):
        """
        Return: status_code, status_text, data
        data = the login if status is 200 or 304, else data is None
        """

    def extract_owner_repo_from_url(self, url):
        """
        Returns a tuple: (owner, repo) 
        """

    def get_asset_version(self, name):
        """
        
        """

    def get_assets_from_dist_folder(self):
        """
        
        """

    def last_activity(self):
        """
        
        """

    def latest_release(self, owner, repo):
        """
        Returns: (status_code, status_text, data}
        data = {"tag_name": str, "published_at": date,
                "downloads_count": int}
        """

    def latest_releases_downloads(self, owner, repo, maxi=10):
        """
        Returns: (status_code, status_text, data}
        data = int, downloads count
        """

    def publishing(self, owner, repo, name, tag_name, target_commitish, description, prerelease, draft, asset_path, asset_name, asset_label):
        """
        Return meta code, status code, status text
        meta code:
            0: temporary copy and zip operation are success
            1: failed to copy the project in temp cache
            2: failed to zip the project
        """

    def rate(self):
        """
        Return: status_code, status_text, data
        data = {"limit": int, "remaining": int}
        """

    def repo_description(self, owner, repo):
        """
        Returns: (status_code, status_text, data)
        data = {"created_at": date, "description": str,
                "stargazers_count": int, "subscribers_count": int}
        """

    def target_project(self):
        """
        
        """

    def unauth(self):
        """
        
        """

    def update_activity(self, operation, owner, repo):
        """
        
        """

```

