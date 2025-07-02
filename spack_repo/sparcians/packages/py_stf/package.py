from spack_repo.sparcians.classes.sparcians import SparciansPackage
from spack.package import *


class PyStf(SparciansPackage):
    """Provides the Simulation Trace Format Python library"""

    homepage = "https://github.com/sparcians/stf_lib"
    git = "https://github.com/sparcians/stf_lib.git"
    maintainers("bdutro")
    license("Apache-2.0", checked_by="bdutro")

    version("develop", submodules=True)
    version("1.5", tag="v1.5", submodules=True)

    variant("build_type", default="Release", description="CMake build type", values=("Release", "FastDebug", "Debug", "Profile"))

    depends_on("python")
    depends_on("py-cython")
    depends_on("py-setuptools")
    depends_on("py-wheel")
    depends_on("boost")
    depends_on("zstd")

    def setup_build_environment(self, env):
        # This is automatically set in the build environment by py-cython, but the stfpy CMake flow already handles this internally.
        # Unsetting the variable avoids an unnecessary second recompilation
        env.unset("CYTHON_FORCE_REGEN")

    def cmake_args(self):
        args = [
            self.define("FULL_LTO", True),
            self.define("BUILD_STF_PYTHON_LIB", True),
            self.define("DISABLE_STF_TESTS", True),
            self.define("DISABLE_STF_DOXYGEN", True),
            self.define('STF_INSTALL_DIR', self.prefix.bin),
            self.define("STFPY_INSTALL_DIR", self.prefix)
        ]
        return args
