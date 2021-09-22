# Source for https://blademaw.github.io
All source content for the blog — usually ahead of current viewable posts.

## Compiling and Building Site
Clone repository into suitable folder, e.g.
```
$ git clone https://github.com/blademaw/blademaw.github.io-src.git ghpages
```

Install related non-local plugins:

```
$ python -m pip install pelican-render-math
```

Make adjustments to `liquid-tags/img.py` by replacing `img.py` with [this file](https://blademaw.github.io/features/code/img_ex.py).

Ensure local version builds via
``` 
$ make html && make serve 
```

Make files to publish:
``` 
$ make publish
 ````

## Acknowledgement

- Site built under Pelican with Python
- Theme adapted from [Jake VanderPlas](https://github.com/jakevdp/jakevdp.github.io-source)' github blog.
- Analytics by Google
- Comments by Disqus
