from setuptools import setup

setup(name='robot-toy',
      version='0.2',
      description='A console program that controls a car robot on a 5x5 grid.',
      url='https://github.com/phurichpusapanich/toy_robot_challenge',
      author='Phurich Pusapanich',
      author_email='pusapanich.phurich@gmail.com',
      license='MIT',
      packages=['toy_car'],
      entry_points={
            'console_scripts': ['drive=toy_car.command_reader:main'],
      },
      test_suite="toy_car.tests",
      zip_safe=False)
