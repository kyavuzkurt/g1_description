import os
from setuptools import find_packages, setup

package_name = 'g1_description'

mesh_files = []
xacro_files = []

for root, dirs, files in os.walk('meshes'):
    for file in files:
        if file.endswith('.STL'):
            mesh_files.append(os.path.join(root, file))


setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/robot.launch.py']),
        ('share/' + package_name + '/rviz', ['rviz/default.rviz']),
        ('share/' + package_name + '/urdf', ['urdf/robot.urdf']),
        ('share/' + package_name + '/meshes', mesh_files),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kadir Yavuz Kurt',
    maintainer_email='k.yavuzkurt1@gmail.com',
    description='ROS 2 Package for Unitree G1 Robot Description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)