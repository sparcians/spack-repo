# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install sparta
#
# You can edit this file again by typing:
#
#     spack edit sparta
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.sparcians.classes.sparcians import SparciansPackage
from spack.package import *


class StfTools(SparciansPackage):
    """Provides the Simulation Trace Format tools"""

    homepage = "https://github.com/sparcians/stf_tools"
    git = "https://github.com/sparcians/stf_tools.git"
    maintainers("bdutro")
    license("Apache-2.0", checked_by="bdutro")

    version("develop", submodules=True)
    version("1.5", tag="v1.5", submodules=True)

    variant("build_type", default="Release", description="CMake build type", values=("Release", "FastDebug", "Debug", "Profile"))

    depends_on("libiconv")
    depends_on("gettext")
    depends_on("hdf5+cxx+hl")
    depends_on("mpi", when="^hdf5+mpi")
    depends_on("zstd")
    depends_on("rapidjson")
    depends_on("lz4")
    depends_on("zlib-api")
    depends_on("bzip2")
    depends_on("boost +json")

    depends_on("automake", type="build")
    depends_on("autoconf", type="build")
    depends_on("libtool", type="build")
    depends_on("pkgconfig", type="build")

    def cmake_args(self):
        args = [
            self.define("DISABLE_STF_PYTHON_LIB", True),
            self.define('STF_INSTALL_DIR', self.prefix.bin)
        ]
        return args

    def install(self, spec, prefix):
        super().install(spec, prefix)
        install_tree("mavis/json", prefix.share.join("stf_tools/mavis/json"))
