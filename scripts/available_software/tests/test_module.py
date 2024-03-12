import os
from available_software import module_avail, filter_fn_eessi_modules, module_swap, module_whatis


class TestModule:
    # ---------------------------
    # Class level setup/teardown
    # ---------------------------
    path = os.path.dirname(os.path.realpath(__file__))

    @classmethod
    def setup_class(cls):
        os.environ["TESTS_PATH"] = cls.path
        os.environ["LMOD_CMD"] = cls.path + "/data/lmod_mock.sh"

    # ---------------------------
    # Module tests
    # ---------------------------

    def test_avail(self):
        os.environ["MOCK_FILE_AVAIL"] = self.path + "/data/data_avail_simple_zen2.txt"
        output = module_avail()
        assert len(output) == 16

    def test_avail_filtered(self):
        os.environ["MOCK_FILE_AVAIL"] = self.path + "/data/data_avail_simple_zen2.txt"
        output = module_avail(filter_fn=filter_fn_eessi_modules)
        assert len(output) == 15
        assert list(output) == [
            "cfd/1.0", "cfd/2.0", "cfd/3.0", "cfd/24", "cfd/", "cfd/5.0",
            "cfd/2.0afqsdf", "llm/20230627", "llm/20230627", "llm/20230627", "science/",
            "science/5.3.0", "science/5.3.0", "science/5.3.0", "science/7.2.0"
        ]

    def test_avail_cluster(self):
        os.environ["MOCK_FILE_AVAIL_CLUSTER"] = self.path + "/data/data_avail_cluster_simple.txt"
        output = module_avail(name="cluster/")
        assert len(output) == 1

    def test_whatis(self):
        os.environ["MOCK_FILE_SHOW"] = self.path + "/data/data_show_science.txt"
        data = module_whatis("science")
        assert data == {
            "Description": "Bundle for scientific software",
            "Homepage": "https://science.com/",
            "URL": "https://science.com/",
            "Extensions": "ext-1.2.3, ext-2.3.4"
        }
