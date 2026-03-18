from mdutils.mdutils import MdUtils
import available_software
import os
import filecmp
import shutil


class TestMarkdown:
    # ---------------------------
    # Class level setup/teardown
    # ---------------------------

    path = os.path.dirname(os.path.realpath(__file__))

    @classmethod
    def setup_class(cls):
        os.environ["AVAIL_SOFTWARE_TEST_DIRECTORY"] = cls.path

    @classmethod
    def teardown_class(cls):
        directory = os.path.join(cls.path, "detail")
        if os.path.exists(directory):
            for file in os.listdir(directory):
                if file.endswith('.md'):
                    os.remove(os.path.join(directory, file))

    # ---------------------------
    # Markdown tests
    # ---------------------------

    def test_md_detailed_template(self):
        markdown_target = "detail"
        available_software.main()
        for markdown_file in os.listdir(os.path.join(self.path, "reference_detail")):
            target_markdown_file = os.path.join(self.path, markdown_target, markdown_file)
            assert os.path.exists(target_markdown_file)
            assert filecmp.cmp(target_markdown_file, os.path.join(self.path, "reference_detail", markdown_file))
