from spack_repo.sparcians.classes.sparcians import RapidJSONSparciansPackage
from spack.package import *


class Sparta(RapidJSONSparciansPackage):
    """Provides the SPARTA simulation framework"""

    homepage = "https://github.com/sparcians/map"
    git = "https://github.com/sparcians/map.git"
    maintainers("bdutro")
    license("Apache-2.0", checked_by="bdutro")

    version("develop")

    # FIXME change this to a tag once there's a new tagged Sparta release
    version("2.0.24", commit="2134cbdcb321f8df1033f3bcf89227043c4419a2")
    version("2.0.23", tag="map_v2.0.23")

    variant("python", default=False, description="Builds SPARTA with Python support enabled")
    variant(
        "build_type",
        default="Release",
        description="CMake build type",
        values=("Release", "RelWithDebInfo", "MinSizeRel", "Debug", "Profile")
    )

    depends_on("yaml-cpp")
    depends_on("sqlite")
    depends_on("hdf5+cxx+hl")
    depends_on("mpi", when="^hdf5+mpi")

    boost_dependency = "boost+date_time+iostreams+serialization+timer+program_options"

    # We need Boost::Python if python support is enabled
    with when("+python"):
        boost_dependency += "+python"

    depends_on(boost_dependency)

    root_cmakelists_dir = "sparta"

    def cmake_args(self):
        args = [self.define_from_variant("COMPILE_WITH_PYTHON", "python")]
        return args
