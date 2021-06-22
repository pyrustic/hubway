
Back to [Reference Overview](https://github.com/pyrustic/hubway/blob/master/docs/reference/README.md)

# hubway.host.publishing\_host



<br>


```python

class PublishingHost:
    """
    
    """

    def __init__(self, gurl, owner, repo):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    def publishing(self, name, tag_name, target_commitish, description, prerelease, draft, asset_path, asset_name, asset_label):
        """
        Return {"meta_code":, "status_code", "status_text", "data"}
        meta code:
            0- success
            1- failed to create release (check 'status_code', 'status_text')
            2- failed to upload asset (check 'status_code', 'status_text')
        """

```

