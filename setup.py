# Copyright (c) 2013, Salesforce.com, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# Neither the name of Salesforce.com nor the names of its contributors
# may be used to endorse or promote products derived from this
# software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from setuptools import setup, Extension, Feature
build_ext = None
try:
    from Cython.Distutils import build_ext
except ImportError:
    print 'WARNING cython support disabled'


def conj_ext(name):
    return Extension(
        'distributions.conjugate.{0}'.format(name),
        ['distributions/conjugate/{0}.pyx'.format(name)],
        libraries=['m'],
        extra_compile_args=['-std=c++0x'],
        language='c++')


conj_ext_feature = Feature(
    'cython component models',
    standard=True,
    optional=True,
    ext_modules=[
        conj_ext('scimath'),
        conj_ext('cynich'),
        conj_ext('cydd'),
        conj_ext('cydpm'),
        conj_ext('cygp'),
        ]
    )

config = {
    'features': {'cython': conj_ext_feature},
    'name': 'distributions',
    'packages': [
        'distributions',
        'distributions.basic',
        'distributions.conjugate',
        ],
    }

if build_ext is not None:
    config['cmdclass'] = {'build_ext': build_ext}

setup(**config)
