# SmartViewer-NodeMCU

## Overview

SmartViewer-NodeMCU is an innovative project that combines the power of the NodeMCU microcontroller, socket programming, and machine learning to create an autonomous car equipped with a virtual camera. This project aims to enhance security and surveillance capabilities by allowing remote control and monitoring of the car's movements and surroundings. The car is programmed using Micropython, and the server is developed using Flask, with plans to transition to a socket-based server for enhanced performance.

## Features

- **Autonomous Control:** The NodeMCU listens to requests made to it using sockets, allowing for remote control of the car's motors connected to an L298N motor driver.
- **Virtual Camera:** A phone placed on the car acts as a virtual camera, capturing real-time video feed.
- **Image Processing:** The server uses OpenCV to process the video feed, enhancing the car's ability to detect and respond to its environment.
- **Artificial Intelligence Integration:** The processed images are sent to Llava through a Gradio API call, which returns a description of the scene. This description is then rendered on the HTML page used for controlling the car.
- **Flask Server:** Initially developed with Flask, the server is designed to render an HTML file through which users can control the car's motors. Future plans include transitioning to a socket-based server for improved performance.

## Setup

### Hardware Requirements

- NodeMCU microcontroller
- L298N motor driver
- Phone (for the virtual camera)

### Software Requirements

- Micropython for NodeMCU programming
- Flask for the server (planned transition to socket-based server)
- OpenCV for image processing
- Gradio for machine learning integration

## Installation

1. **NodeMCU Setup:** Program the NodeMCU with Micropython to listen for socket requests and control the motors.
2. **Server Setup:** Install Flask and set up the server to render the HTML control page and process the video feed.
3. **Machine Learning Integration:** Integrate Gradio for sending the video feed to Llava and receiving scene descriptions.

## Usage

1. **Control the Car:** Use the HTML page rendered by the Flask server to send commands to the NodeMCU, controlling the car's motors.
2. **Monitor the Environment:** The virtual camera feed is processed and analyzed, with descriptions of the scene rendered on the control page.

## Future Enhancements

- **Socket-Based Server:** Transition from Flask to a socket-based server for improved performance.
- **Advanced Object Detection:** Enhance the machine learning model for more accurate scene descriptions.

