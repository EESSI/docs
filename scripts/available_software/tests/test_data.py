import os
from available_software import modules_eessi, get_unique_software_names

GENERIC = "/cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/generic"
ZEN2 = "/cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2"


class TestData:
    # ---------------------------
    # Class level setup/teardown
    # ---------------------------
    path = os.path.dirname(os.path.realpath(__file__))

    @classmethod
    def setup_class(cls):
        os.environ["TESTS_PATH"] = cls.path
        os.environ["LMOD_CMD"] = cls.path + "/data/lmod_mock.sh"
        os.environ["SHELL"] = cls.path + "/data/bash_mock.sh"
        os.environ["MOCK_FILE_SWAP"] = cls.path + "/data/data_swap_TARGET.txt"
        os.environ["MOCK_FILE_AVAIL_TARGET"] = cls.path + "/data/data_avail_target_simple.txt"
        os.environ["MOCK_FILE_AVAIL_TARGET_AMD_INTEL"] = cls.path + "/data/data_avail_target_amd_intel.txt"

    # ---------------------------
    # Module tests
    # ---------------------------

    def test_data_eessi(self):
        sol = modules_eessi()
        assert len(sol) == 2
        assert len(sol[GENERIC]) == 13
        assert len(sol[ZEN2]) == 15
        assert list(get_unique_software_names(sol[GENERIC])) == ["Markov", "cfd", "science"]
        assert list(get_unique_software_names(sol[ZEN2])) == ["cfd", "llm", "science"]
