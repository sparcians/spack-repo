# This is just a placeholder for the rapidjson package that allows the sparta package
# to apply a dependency patch
# Workaround for https://github.com/spack/spack/issues/34961

from spack_repo.builtin.packages.rapidjson.package import Rapidjson as BuiltinRapidjson


class Rapidjson(BuiltinRapidjson):
    pass
