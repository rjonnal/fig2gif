# mpl_gifv

## Make a movie out of matplotlib plots (requires ImageMagick)

## Preliminaries

1. Install [ImageMagick](https://www.imagemagick.org). In Debian/Ubuntu run `apt-get install imagemagick`. For other distros and OSs, see [ImageMagick installation instructions](https://www.imagemagick.org/script/binary-releases.php).

2. To run test.py verify installation of [numpy](http://numpy.org) and [matplotlib](http://matplotlib.org).

## The basic idea:

1. Create a GIFV object.

2. Add frames to it (by passing a matplotlib figure handle to its add function.

3. Call its make function.

