# Ollama logs checker

This is a Python pet project which you can use to check where [ollama](https://ollama.com/) keeps its log files and
how it updates it. It uses watchdog library to check for changes in ollama logs. Under Windows ollama logs are 
stored in a file with name `history` which is located in `%USERPROFILE\.ollama`. This logs keeps all questions 
which you ask a model. It comes out is is impossible to follow the changes in the file by using `type -f history`
because ollama creates first history.tmp file and then replaces it every time. If you start ollama and ask 
a model a question is such a way: 
```
C:\Users\georgi.naumov\.ollama>ollama run llama3
>>> Why the sky is blue?
A classic question!

The color of the sky appears blue to our eyes because of a phenomenon called scattering, which occurs when sunlight interacts with tiny molecules of gases in the Earth's atmosphere. Here's why:

1. **Sunlight**: When the sun emits light, it contains all the colors of the visible spectrum (red, orange, yellow, green, blue, indigo, and violet). This is known as white light.
2. **Atmospheric gases**: The Earth's atmosphere is made up of a mixture of gases, including nitrogen (N2), oxygen (O2), argon (Ar), carbon dioxide (CO2), and others. These gases are very small compared
to the wavelength of light.
3. **Scattering**: When sunlight enters the Earth's atmosphere, it encounters these tiny gas molecules. The shorter wavelengths of light (like blue and violet) are scattered more than the longer
wavelengths (like red and orange) because they interact with the gas molecules more strongly. This is known as Rayleigh scattering, named after the British physicist Lord Rayleigh, who first described
the phenomenon in 1871.
4. **Blue dominance**: As a result of this scattering, the blue light is dispersed throughout the atmosphere, reaching our eyes from all directions. Since we don't see the other colors (like red and
orange) being scattered as much, the blue color becomes dominant, giving the sky its blue appearance.

Other factors can influence the apparent color of the sky:

* **Dust and water vapor**: Tiny particles in the air, like dust, smoke, or water vapor, can absorb or scatter light, changing the color of the sky. For example, during sunrise and sunset, the longer
wavelengths of light (like red and orange) are more scattered by atmospheric particles, making the sky appear more reddish.
* **Clouds**: Clouds can reflect sunlight, adding white or gray tones to the sky.
* **Altitude and atmospheric conditions**: The color of the sky can vary depending on factors like altitude, atmospheric pressure, temperature, and humidity.

So, in summary, the sky appears blue because the shorter wavelengths of sunlight (like blue) are scattered more by the tiny gas molecules in the Earth's atmosphere, making them visible to our eyes.

>>> Send a message (/? for help)
```
After quiting and checking the log file you will see the following: 
```
>>> /bye

C:\Users\georgi.naumov\.ollama>type history
Why the sky is blue?
/bye

C:\Users\georgi.naumov\.ollama>
```

However, how it works internally? If you run `main.py` Python script you will see that. The logs 
are not directly appended to `history` file. Every time ollama creates file `history.tmp` them 
replaces current `history` file with the new one. Here is the output which you can see from
`main.py` file. 

```
C:\Users\georgi.naumov\PycharmProjects\ollama_logs_checker\.venv\Scripts\python.exe C:\Users\georgi.naumov\PycharmProjects\ollama_logs_checker\main.py 
Watchdog received modified event with src_path - C:\Users\georgi.naumov\.ollama\history.tmp dest_path - .
Watchdog received modified event with src_path - C:\Users\georgi.naumov\.ollama\history.tmp dest_path - .
Watchdog received modified event with src_path - C:\Users\georgi.naumov\.ollama\history.tmp dest_path - .
Watchdog received deleted event with src_path - C:\Users\georgi.naumov\.ollama\history dest_path - .
Watchdog received moved event with src_path - C:\Users\georgi.naumov\.ollama\history.tmp dest_path - C:\Users\georgi.naumov\.ollama\history.
```
I hope this helps someone who is interested where logs are stored. 