# Number Sign Language Translator

 This is an AI Number Sign Language Interpreter using a Jetson Nano!

## The Algorithm

### Meet the AI Sign Language Interpreter Robot

My AI Sign Language Interpreter Robot uses advanced technology to interpret ASL number gestures in real-time. It displays accurate translations instantly on its user-friendly screen. Designed to enhance communication between the Deaf and hearing communities, it's your portable bridge to clear understanding anywhere you need it. 

## Running this project

1. Run the Docker Pull command in the VS Code terminal: sudo docker pull \
    us-central1-docker.pkg.dev/woven-edge-323322/jetson/tensorflow:latest
2. Run the docker container: sudo docker run --runtime nvidia -it --rm --volume=`pwd`/my_project:/my_project --device=/dev/video0 put your image id here
3. Install pillow: pip install pillow
4. Cd into the project: cd my_project
5. Then paste this once you run that: python3 sign_language_translator.py

[Once these steps are completed, follow a video explanation here:] https://youtu.be/z7vK0fAZQ14
