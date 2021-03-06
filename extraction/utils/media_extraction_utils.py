"""This script contains helper utilities for extractors"""

import re


def has_domain(url, regex):
    return re.compile(regex).match(url)


def get_media_size(node):
    """Returns the size of the media content"""

    if node.has_attr('width') and node.has_attr('height'):
        return int(node['width']), int(node['height'])
    return 0, 0
