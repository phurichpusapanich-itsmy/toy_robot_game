from setuptools import setup

setup(name='robot-toy',
      version='0.1',
      description='A console program that controls a car robot on a 5x5 grid.',
      url='https://github.com/phurichpusapanich-itsmy/toy_robot_game',
      author='Phurich Pusapanich',
      author_email='pusapanich.phurich@gmail.com',
      license='MIT',
      packages=['toy_car'],
      scripts=['bin/drive.py'],
      zip_safe=False)
