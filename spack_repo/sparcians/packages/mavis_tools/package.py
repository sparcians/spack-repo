from spack_repo.sparcians.classes.sparcians import SparciansPackage
from spack.package import *


class MavisTools(SparciansPackage):
    """Provides tools based on the Mavis decoder library"""

    homepage = "https://github.com/sparcians/mavis_tools"
    git = "https://github.com/sparcians/mavis_tools.git"
    maintainers("bdutro")
    license("Apache-2.0", checked_by="bdutro")

    version("develop", submodules=True)
    version("1.0", tag="v1.0", submodules=True)

    variant("build_type", default="Release", description="CMake build type", values=("Release", "FastDebug", "Debug", "Profile"))

    depends_on("boost +json")

    def cmake_args(self):
        args = [
            self.define('MAVIS_TOOLS_INSTALL_DIR', self.prefix.bin)
        ]
        return args

    def install(self, spec, prefix):
        super().install(spec, prefix)
