from mdutils.mdutils import MdUtils
from available_software import get_unique_software_names, modules_eessi, generate_table_data, generate_module_table
import os
import filecmp


class TestMarkdown:
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

    @classmethod
    def teardown_class(cls):
        if os.path.exists("test_simple.md"):
            os.remove("test_simple.md")

    # ---------------------------
    # Markdown tests
    # ---------------------------

    def test_table_generate_simple(self):
        simple_data = get_unique_software_names(modules_eessi())
        table_data, col, row = generate_table_data(simple_data)
        assert col == 3
        assert row == 5
        assert len(table_data) == 15

    def test_md_simple(self):
        md_file = MdUtils(file_name='test_simple', title='Overview Modules')
        simple_data = get_unique_software_names(modules_eessi())
        generate_module_table(simple_data, md_file)
        md_file.create_md_file()
        assert os.path.exists("test_simple.md")
        assert filecmp.cmp(self.path + "/data/test_md_simple_sol.md", "test_simple.md")
