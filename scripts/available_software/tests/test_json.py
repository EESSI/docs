from available_software import (generate_json_overview_data,
                                generate_json_overview,
                                modules_eessi,
                                generate_json_detailed,
                                generate_json_detailed_data)
import os
import json


class TestJSON:
    # ---------------------------
    # Class level setup/teardown
    # ---------------------------

    path = os.path.dirname(os.path.realpath(__file__))

    @classmethod
    def setup_class(cls):
        os.environ["TESTS_PATH"] = cls.path
        os.environ["LMOD_CMD"] = cls.path + "/data/lmod_mock.sh"
        os.environ["MOCK_FILE_SWAP"] = cls.path + "/data/data_swap_CLUSTER.txt"
        os.environ["MOCK_FILE_AVAIL_CLUSTER"] = cls.path + "/data/data_avail_cluster_simple.txt"
        os.environ["MOCK_FILE_SHOW"] = cls.path + "/data/data_show_science.txt"

    @classmethod
    def teardown_class(cls):
        if os.path.exists("json_data.json"):
            os.remove("json_data.json")
            os.remove("json_data_detail.json")

    # ---------------------------
    # Markdown tests
    # ---------------------------

    def test_json_generate_simple(self):
        modules = modules_eessi()
        json_data = generate_json_overview_data(modules)
        assert len(json_data.keys()) == 3
        assert list(json_data["clusters"]) == ["/cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/generic", "/cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2"]
        assert json_data["modules"] == {
                "Markov": [1, 0],
                "cfd": [1, 1],
                "llm": [0, 1],
                "science": [1, 1]
            }

    def test_json_simple(self):
        modules = modules_eessi()
        json_path = generate_json_overview(modules, ".")
        with open(json_path) as json_data:
            data_generated = json.load(json_data)

        with open(self.path + "/data/test_json_simple_sol.json") as json_data:
            data_solution = json.load(json_data)

        assert len(data_generated) == 3
        assert data_generated["modules"] == data_solution["modules"]
        assert data_generated["clusters"] == data_solution["clusters"]

    def test_json_detail_simple(self):
        modules = modules_eessi()
        json_data = generate_json_detailed_data(modules)
        json_path = generate_json_detailed(json_data, ".")
        assert os.path.exists("json_data_detail.json")

        with open(json_path) as json_data:
            data_generated = json.load(json_data)

        with open(self.path + "/data/test_json_simple_sol_detail.json") as json_data:
            data_solution = json.load(json_data)

        assert len(data_generated) == 3
        assert data_generated["clusters"] == data_solution["clusters"]
        assert data_generated["software"] == data_solution["software"]
