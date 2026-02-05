from spack_repo.sparcians.classes.sparcians import RapidJSONSparciansPackage
from spack.package import *


class Sparta(RapidJSONSparciansPackage):
    """Provides the SPARTA simulation framework"""

    homepage = "https://github.com/sparcians/map"
    git = "https://github.com/sparcians/map.git"
    maintainers("bdutro")
    license("Apache-2.0", checked_by="bdutro")

    version("develop")

    version("2.1.17", tag="map_v2.1.17", submodules=True)
    version("2.1.16", tag="map_v2.1.16", submodules=True)
    version("2.1.15", tag="map_v2.1.15", submodules=True)
    version("2.1.14", tag="map_v2.1.14", submodules=True)
    version("2.1.13", tag="map_v2.1.13", submodules=True)
    version("2.1.12", tag="map_v2.1.12", submodules=True)
    version("2.1.11", tag="map_v2.1.11", submodules=True)
    version("2.1.10", tag="map_v2.1.10", submodules=True)
    version("2.1.9", tag="map_v2.1.9", submodules=True)
    version("2.1.8", tag="map_v2.1.8", submodules=True)
    version("2.1.7", tag="map_v2.1.7", submodules=True)
    version("2.1.6", tag="map_v2.1.6", submodules=True)
    version("2.1.5", tag="map_v2.1.5", submodules=True)
    version("2.1.4", tag="map_v2.1.4", submodules=True)
    version("2.1.3", tag="map_v2.1.3", submodules=True)
    version("2.1.2", tag="map_v2.1.2", submodules=True)
    version("2.1.1", tag="map_v2.1.1", submodules=True)
    version("2.1.0", tag="map_v2.1.0", submodules=True)
    version("2.0.26", tag="map_v2.0.26")
    version("2.0.25", tag="map_v2.0.25")
    version("2.0.24", tag="map_v2.0.24")
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
