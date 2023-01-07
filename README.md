<a href="https://colab.research.google.com/github/NXTDMNSN/KICK-GNR8R/blob/main/KICK_GNR8R_MAIN.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


# KICK-GNR8R
**DIGITAL WARFARE** - ***DIGITALLY DISTORTED DATA DESIGNED TO DESTROY THE DANCE MUSIC INDUSTRY***

---

KICK-GNR8R is a machine learning algorithm designed to generate Hardstyle Kicks from previously trained checkpoint files. The CKPT file provided was trained on over 1500 Hard Dance kicks from various genres spanning Rawstyle to Reverse bass.

It is an extremely powerful tool for producers to generate absolutely unique professional sounding Kickdrums. The days of ripping kicks are over.
This tool is not intended for replacing the traditional process of sound design and kick production, but rather as a companion to streamline the process by generating samples which can be refined layered, and elaborated as most kicks are done today. You can even train a CKPT with your own dataset!

Train your DATASET with [KICK_GNR8R_TRaiNR.py]

Input your CHECKPOINT file that you created into [KICK_GNR8R_MAIN.py]

---

# KICK-GNR8R INSTRUCTIONS 📖 ℹ

---

###  **GOOGLE DRIVE DIRECTORY SETUP:**
- CREATE A NEW GMAIL ACCOUNT
- OPEN GOOGLE DRIVE
- COPY CHECKPOINT FILE TO GOOGLE DRIVE, PLACE IN ROOT DIRECTORY.
- In Checkpoint directory Right click > More > Connect More Apps > Colaboratory

- Open [KICK-GNR8R](https://colab.research.google.com/github/NXTDMNSN/KICK-GNR8R/blob/main/KICK_GNR8R_MAIN.ipynb) Colab File
- Run first cell SETUP "Check GPU Status" - If no GPU is assigned then ⬇⬇⬇⬇
> - Runtime > Change Runtime Type > GPU (Colab may assign a free standard GPU, is subject to availability. For 100% reliability, purchase 100 compute units for $10 **[HERE](https://colab.research.google.com/signup/pricing)** This is enought to generate approx 100 audio files.

---
### GENERATE RANDOM KICKS
 
Select desired quantity of samples to generate
Select appropriate sampler steps for the generator
Run the GNR8R Cell to generate samples
- R3GENER8R -
LAYER & MIX
Record a file, enter the path to an audio file you want to regenerate, or upload a file when prompted
INTERPOL8R
Enter the paths to two audio files you want to interpolate between, or upload them when prompted
Make sure the "skip_for_run_all" checkbox is unchecked
Run the cell under the "Interpolate between sounds" header
STYLE TRANSFER
Enter a path to save your audio recordings
Enter the number of audio recordings you want to combine into one
Run the cell under the "Regenerate your own sound from the recording" header
Make sure the "skip_for_run_all" checkbox is unchecked
