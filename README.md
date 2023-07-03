# The MoFactory
Welcome to the MoFactory! A project with the goal of making a real and functioning BMO from the show adventure time! The side goal in doing so is to learn as much as possible about design, electronics, project management and more. All files are open source so you can build one for yourself and/or contribute to the project too. Now with all that said, "Who wants to play video games?"

<img src="media/bmo.jpg" width="40%">

## Contents

- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [About BMO](#about-bmo)
    - [Hardware specs](#hardware-specs)
    - [Software specs](#software-specs)
    - [Current Games and Features](#current-games-and-features)

        
## Getting started
If you would like to build one, check out [the wiki](https://github.com/NuMellow/theMoFactory/wiki) and choose which version you'd like to build. The Building BMO page will have step-by-step instructions on how to build your own. 
Note: Versions will mostly be similar, but may have updated 3D printed parts and hardware.

### Software
After downloading the repository, navigate to the software folder and run:

`./ setup.sh`

`pip install -r requirements.txt`

This installs the required packages to run the games and use the microphone

To use the physical buttons run:

`python bmoButtons.py &` - This runs the buttons script in the background

To run invidual games, go to the specific game in the games folder and run the .py file e.g:

`python conversation_parade.py`

## Contributing
More details coming soon.

## About BMO

### Hardware Specs
The heart and brain of BMO runs on a raspberry pi. Current models feature a 4inch monitor display, microphone, mini usb speaker, usb and earphone adapters and push button sensors. These are powered by a 5000mAh battery.

### Software Specs
BMO runs mostly on python and pygame. Current programs includes buttons script, games: pro football 1861 and conversation parade, with more programs and features coming soon.

### Current Games and Features
#### Games
- Pro footbal 1861
- Conversation parade

#### Features
- Animation/phrases from old iphone/ipad app
- Voice commands to trigger phrases
