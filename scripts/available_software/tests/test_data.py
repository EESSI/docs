import os
from available_software import modules_eessi, get_unique_software_names


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
        os.environ["MOCK_FILE_SWAP"] = cls.path + "/data/data_swap_CLUSTER.txt"
        os.environ["MOCK_FILE_AVAIL_CLUSTER"] = cls.path + "/data/data_avail_cluster_simple.txt"
        os.environ["MOCK_FILE_AVAIL_CLUSTER_AMD_INTEL"] = cls.path + "/data/data_avail_cluster_amd_intel.txt"

    # ---------------------------
    # Module tests
    # ---------------------------

    def test_data_eessi(self):
        sol = modules_eessi()
        assert len(sol) == 2
        assert len(sol["/cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/generic"]) == 13
        assert len(sol["/cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2"]) == 15
        assert list(get_unique_software_names(sol["/cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/generic"])) == ["Markov", "cfd", "science"]
        assert list(get_unique_software_names(sol["/cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2"])) == ["cfd", "llm", "science"]
