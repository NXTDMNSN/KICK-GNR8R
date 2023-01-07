[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NXTDMNSN/KICK-GNR8R/blob/main/KICK_GNR8R_MAIN.ipynb#scrollTo=-ITvsXU6hCAx]


# KICK-GNR8R
**DIGITAL WARFARE** - ***DIGITALLY DISTORTED DATA DESIGNED TO DESTROY THE DANCE MUSIC INDUSTRY***

---

KICK-GNR8R is a machine learning algorithm designed to generate Hardstyle Kicks from previously trained checkpoint files. The CKPT file provided was trained on over 1500 Hard Dance kicks from various genres spanning Rawstyle to Reverse bass.

It is an extremely powerful tool for producers to generate absolutely unique professional sounding Kickdrums. The days of ripping kicks are over.
This tool is not intended for replacing the traditional process of sound design and kick production, but rather as a companion to streamline the process by generating samples which can be refined layered, and elaborated as most kicks are done today. You can even train a CKPT with your own dataset!


Train your DATASET with [KICK_GNR8R_TRaiNR.py]

Input your CHECKPOINT file that you created with [KICK_GNR8R_MAIN.py]
---

**Audio diffusion tools in this notebook**:

- TRaiNER
> Dataset Trainer

- KICK GNR8R
>  Unconditional (random) Kick sample Generator

- R3GNR8R
> Audio Sample Regenerator / Style Transfer using 2 input Samples

- INTERPOL8R
> Interpolation between 2 audio files to blend them in a specified number of steps

- UNDER DEVELOPMENT: PREPROCESSOR
> Preprocess your audioflaes and standardize them to use any kind of file with TRaiNR

---

# **INSTRUCTIONS** 📖 ℹ

## Before anything else
- Run the "Setup" section
- Sign in to the Google Drive account you want to save your models in
- Select the model you want to sample from in the "Model settings" section, this determines the length and sound of your samples
- Select the sampler you want to use.
- The `save_to_wandb` option futher down adds the ability to log your audio generations to [Weights & Biases](https://www.wandb.ai/site), an experiment tracking and model and data versioning tool.

## For random sample generation
- Choose the number of random samples you would like KICK_GNR8R to generate for you 
- Choose the number of diffusion steps you would like KICK_GNR8R to execute
- Make sure the "skip_for_run_all" checkbox is unchecked
- Run the cell under the "Generate new sounds" header

## To regenerate your own sounds
- Record a file, enter the path to an audio file you want to regenerate, or upload a file when prompted
- Make sure the "skip_for_run_all" checkbox is unchecked
- Run the cell under the "Regenerate your own sounds" header

## To interpolate between two different sounds
- Enter the paths to two audio files you want to interpolate between, or upload them when prompted
- Make sure the "skip_for_run_all" checkbox is unchecked
- Run the cell under the "Interpolate between sounds" header

## To regenerate sounds using built-in audio recording module
- Enter a path to save your audio recordings
- Enter the number of audio recordings you want to combine into one
- Run the cell under the "Regenerate your own sound from the recording" header
- Make sure the "skip_for_run_all" checkbox is unchecked
