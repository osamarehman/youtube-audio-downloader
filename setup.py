from setuptools import setup, find_packages

setup(
    name='youtube-audio-downloader',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pytube>=10.0.0',
        'pydub>=0.24.1'
    ],
    entry_points={
        'console_scripts': [
            'youtube-audio-downloader=youtube_audio_downloader.downloader:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A command-line tool to download audio from YouTube videos',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/youtube-audio-downloader',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
) 