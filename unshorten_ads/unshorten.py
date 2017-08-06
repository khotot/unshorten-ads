import linkshrink


def unshorten(url):
    if 'linkshrink' in url:
        return linkshrink.unshorten(url)
    else:
        return "Not support site\n"
