import available_software
import os
import filecmp


class TestMarkdown:
    # ---------------------------
    # Class level setup/teardown
    # ---------------------------

    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_dir')

    @classmethod
    def setup_class(cls):
        os.environ["AVAIL_SOFTWARE_TEST_DIRECTORY"] = cls.path

    @classmethod
    def teardown_class(cls):
        directories = [os.path.join(cls.path, "detail"), os.path.join(cls.path + '_riscv', "detail")]
        for directory in directories:
            if os.path.exists(directory):
                for file in os.listdir(directory):
                    if file.endswith(".md"):
                        os.remove(os.path.join(directory, file))

    # ---------------------------
    # Markdown tests
    # ---------------------------

    def test_md_detailed_template(self):
        available_software.main()
        directories = [self.path, self.path + '_riscv']
        for directory in directories:
            for markdown_file in os.listdir(os.path.join(directory, "reference_detail")):
                target_markdown_file = os.path.join(directory, 'detail', markdown_file)
                assert os.path.exists(target_markdown_file)
                assert filecmp.cmp(target_markdown_file, os.path.join(directory, "reference_detail", markdown_file))
