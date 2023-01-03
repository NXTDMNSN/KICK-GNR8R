from setuptools import setup, find_packages

setup(
    name='KICK-GNR8R',
    version='1.0.0',
    url='https://github.com/NXTDMNSN/KICK-GNR8R.git',
    author='Digital Divinity',
    packages=find_packages(),    
    install_requires=[
        'einops',
        'pandas',
        'prefigure', 
        'pytorch_lightning',
        'scipy',
        'torch',
        'torchaudio',
        'tqdm',
        'wandb',
    ],
)
