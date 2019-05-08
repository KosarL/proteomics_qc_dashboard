try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

project_name = 'proteomics_qc_dashboard'
config = {
    'description': 'A dashboard for proteomics pipelines based MaxQuant.',
    'author': 'Soren Wacker',
    'url': 'https://github.com/soerendip',
    'download_url': f'https://github.com/soerendip/{project_name}',
    'author_email': 'swacker@ucalgary.ca',
    'packages': [f'{project_name}'],
    'scripts': ['scripts/proteomics_qc_dashboard.py'],
    'name': f'{project_name}'
}

setup(**config)
