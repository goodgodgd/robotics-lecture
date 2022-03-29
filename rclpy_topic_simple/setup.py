from setuptools import setup, find_packages

package_name = 'rclpy_topic_simple'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='ian',
    author_email='hyukdoo.choi@sch.ac.kr',
    maintainer='ian',
    maintainer_email='hyukdoo.choi@sch.ac.kr',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Programming Language :: Python'
    ],
    description='ROS 2 rclpy basic package to test topic communication',
    license='MIT License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            f'helloworld_publisher = {package_name}.helloworld_publisher:main',
            f'helloworld_subscriber = {package_name}.helloworld_subscriber:main',
        ],
    },
)
