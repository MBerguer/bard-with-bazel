# Common bazel setup
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# Download and enable Bazel skylib macro
http_archive(
    name = "bazel_skylib",
    sha256 = "66ffd9315665bfaafc96b52278f57c7e2dd09f5ede279ea6d39b2be471e7e3aa",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.4.2/bazel-skylib-1.4.2.tar.gz",
        "https://github.com/bazelbuild/bazel-skylib/releases/download/1.4.2/bazel-skylib-1.4.2.tar.gz",
    ],
)
load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")
bazel_skylib_workspace()



# Project specifics (in this case, python)
# Download Bazel Python Rules
http_archive(
    name="rules_python",
    sha256="84aec9e21cc56fbc7f1335035a71c850d1b9b5cc6ff497306f84cced9a769841",
    strip_prefix="rules_python-0.23.1",
    url="https://github.com/bazelbuild/rules_python/releases/download/0.23.1/rules_python-0.23.1.tar.gz",
)


# importamos pip_parse que se encarga de compilar dependencias
load("@rules_python//python:pip.bzl", "pip_parse")


# Create a central repo that knows about the dependencies needed from
# requirements_lock.txt.
pip_parse(
    name = "python_deps",
    requirements_lock = "//:requirements_lock.txt",   # See BUILD.bazel (//) for how this file is generated.
)

load("@python_deps//:requirements.bzl", "install_deps")

#
install_deps()
