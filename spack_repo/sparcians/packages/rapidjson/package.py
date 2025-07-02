# This is just a placeholder for the rapidjson package that allows the sparta package
# to apply a dependency patch

from spack_repo.builtin.packages.rapidjson.package import Rapidjson as BuiltinRapidjson

class Rapidjson(BuiltinRapidjson):
    pass
