from setuptools import setup, find_namespace_packages

setup(name='Clean_folder',
      version='1.1',
      description='Clean Folder',
      author='Maryna Tiumienieva',
      author_email='testm@example.com',
      license = 'MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['Clean_folder=Clean_folder.Clean:start']}
)