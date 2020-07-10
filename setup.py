import setuptools

with open("README.md", "r") as readme_file:
  readme = readme_file.read()

setuptools.setup(
  name='github_traffic_stats2',
  version='20.7.9',
  description='A project to pull and store traffic stats for GitHub projects using GitHub API',
  long_description = readme,
  long_description_content_type='text/markdown',
  author='seladb',
  author_email='pcapplusplus@gmail.com',
  entry_points={
    "console_scripts": ['github_traffic_stats = github_traffic_stats:main']
  },
  url='https://github.com/seladb/github-traffic-stats',
  download_url='https://github.com/seladb/github-traffic-stats/archive/master.tar.gz',
  py_modules=['github_traffic_stats'],
  keywords=['github', 'github-traffic', 'github-api'],
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3',
  install_requires=['githubpy', 'pickledb', 'simplejson'],
)
