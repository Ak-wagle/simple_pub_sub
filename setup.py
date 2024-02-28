from setuptools import find_packages, setup

package_name = 'simple_pub_sub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/pubsub_launch.py']),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wagle',
    maintainer_email='wagle@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "pub = simple_pub_sub.numpub:main",
            "sub = simple_pub_sub.numsub:main",
        ],
    },
)
