from distutils.core import setup
setup(
  name = 'github_traffic_stats2',
  packages = ['github_traffic_stats2'],
  version = '18.03.1',
  description = 'A project to pull and store traffic stats for GitHub projects using GitHub API',
  author = 'seladb',
  author_email = 'pcapplusplus@gmail.com',
  entry_points={
    "console_scripts": ['github_traffic_stats = github_traffic_stats2.github_traffic_stats:main']
  },
  url = 'https://github.com/seladb/github-traffic-stats',
  download_url = 'https://github.com/seladb/github-traffic-stats/archive/master.tar.gz',
  keywords = ['github', 'github-traffic', 'github-api'],
  install_requires=['githubpy', 'pickledb', 'simplejson'],
  classifiers = [],
)
