# january-jython

Jython bindings to Eclipse January to provide NumPy-like ndarrays

## Quick start

Firstly, install Jython and virtualenv. Then configure a custom
environment for Jython:

    $ virtualenv -p /path/to/jython jython-env
    $ source jython-env/bin/activate
    $ pip install decorator

Download source:

    $ git clone git@github.com:PeterC-DLS/january-jython.git

To use, first ensure you are using the `jython-env` created earlier:
     
    $ source jython-env/bin/activate

then start the Jython interperter:

    $ cd january-jython/january
    $ CLASSPATH="../jars/*" python

finally, test:

    >>> import january as np

    # create a 2D array
    >>> a = np.arange(12.).reshape(4,3)

    >>> print a
    Dataset [[0.0000000, 1.0000000, 2.0000000],
     [3.0000000, 4.0000000, 5.0000000],
     [6.0000000, 7.0000000, 8.0000000],
     [9.0000000, 10.000000, 11.000000]]

    # index
    >>> print a[0,2]
    2.0

    # slice
    >>> print a[1]
    Dataset [3.0000000, 4.0000000, 5.0000000]
    >>> print a[:,2:3]
    Dataset [[2.0000000],
     [5.0000000],
     [8.0000000],
     [11.000000]]
    >>> print a[::-1,2]
    Dataset [11.000000, 8.0000000, 5.0000000, 2.0000000]



