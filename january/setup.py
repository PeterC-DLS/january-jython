from jip.dist import setup

requires_java = {
    'dependencies':[
        ## (groupdId, artifactId, version)
        ('org.slf4j', 'slf4j-api', '1.7.21'),
        ('ch.qos.logback', 'logback-core', '1.2.2'),
        ('org.lucee', 'commons-lang', '2.6.0'),
        ('org.apache.commons', 'commons-math3', '3.6.1'),
#        ('org.eclipse', 'eclipse-january', '2.0.2'),
    ],
    'repositories':[
        ('sonatype-oss-snapshot', 'http://oss.sonatype.org/content/repositories/snapshots/')
    ]
}

setup(
    name='january',
    version='0.1',
    description='Eclipse January Jython bindings',
    long_description='Jython bindings to provide a NumPy-like ndarray',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
    ],
    keywords='array processing',
    url='https://github.com/eclipse/january-jython',
    author='Peter Chang',
    author_email='peter.chang@diamond.ac.uk',
    license='ALv2',
    packages=['january'],
    # zip_safe=False,
    requires_java=requires_java,
    requires=['decorator'], # install_requires is not in Jython 2.7
    )

