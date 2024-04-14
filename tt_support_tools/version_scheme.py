import setuptools_scm

def get_tt_tools_version(scm_version: setuptools_scm.version.ScmVersion):
    return f"{scm_version.branch} {scm_version.node}"
