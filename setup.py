import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summer"
AUTHOR_USER_NAME = "AbhiramMngi"
SRC_REPO = "textSummer"
AUTHOR_EMAIL = "abhiramreddy2908@gmail.com"


setuptools.setup(
  name = SRC_REPO,
  version=__version__,
  author=AUTHOR_USER_NAME,
  author_email=AUTHOR_EMAIL,
  description="Text Summarizer: For summarizing long text",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/AbhiramMngi/Text-Summer",
  project_urls = {
      "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues/"
  },
  package_dir={"": "src"},
  packages=setuptools.find_packages(where="src")
)