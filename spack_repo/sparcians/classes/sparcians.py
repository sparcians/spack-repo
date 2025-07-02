from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *

class SparciansPackage(CMakePackage):
    requires(
        "%gcc", "%clang",
        policy="any_of",
        msg="SPARTA builds only with GCC 13+ or Clang 14+"
    )

    depends_on("c")
    depends_on("cxx")

    depends_on("gcc@13:", when="%gcc", type="build")
    depends_on("gcc-runtime@13:")
    depends_on("clang@14:", when="%clang", type="build")

