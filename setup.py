from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='Sort files in directory by categories',
    url='https://github.com/DmytroLievoshko/lesson-six-working-with-files.git',
    author='Dmytro Lievoshko',
    author_email='levka296@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    include_package_data=True,
    entry_points={'console_scripts': [
        'clean_folder = clean_folder.clean:main']}
)
