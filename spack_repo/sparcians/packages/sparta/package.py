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


class Sparta(SparciansPackage):
    """Provides the SPARTA simulation framework"""

    homepage = "https://github.com/sparcians/map"
    git = "https://github.com/sparcians/map.git"
    maintainers("bdutro")
    license("Apache-2.0", checked_by="bdutro")

    version("develop")
    version("2.0.24", commit="2134cbdcb321f8df1033f3bcf89227043c4419a2")
    version("2.0.23", tag="map_v2.0.23")

    variant("python", default=False, description="Builds SPARTA with Python support enabled")
    variant("build_type", default="Release", description="CMake build type", values=("Release", "RelWithDebInfo", "MinSizeRel", "Debug", "Profile"))

    depends_on("yaml-cpp")
    depends_on("rapidjson@1.2.0-2024-08-16", patches=patch("https://github.com/Tencent/rapidjson/compare/7c73dd7...24b5e7a.patch", sha256="87c4cfd78cee7f0533a2c49574c4a084bb72f6912e9a21203c86ff54f45d1711"))
    depends_on("sqlite")
    depends_on("hdf5+cxx+hl")
    depends_on("mpi", when="^hdf5+mpi")

    # Python disabled
    depends_on("boost +date_time +iostreams +serialization +timer +program_options", when="-python")

    # Python enabled
    depends_on("boost +date_time +iostreams +serialization +timer +program_options +python", when="+python")
    depends_on("python", when="+python")

    root_cmakelists_dir = "sparta"

    def cmake_args(self):
        args = [self.define_from_variant("COMPILE_WITH_PYTHON", "python")]
        return args
