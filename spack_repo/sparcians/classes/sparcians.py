from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


# Simple package class that adds dependencies on modern GCC and Clang
# Most/all Sparcians packages use CMake at the moment
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


# Patches rapidjson with additional commits beyond the 1.2.0-2024-08-16 version tag
# This changeset reverts the rapidjson include path provided by the CMake config back to the one that Sparta expects
# This class can be removed once the upstream Spack rapidjson package is updated to include these commits
class RapidJSONSparciansPackage(SparciansPackage):
    depends_on(
        "rapidjson@1.2.0-2024-08-16",
        patches=patch(
            "https://github.com/Tencent/rapidjson/compare/7c73dd7...24b5e7a.patch",
            sha256="87c4cfd78cee7f0533a2c49574c4a084bb72f6912e9a21203c86ff54f45d1711"
        )
    )
