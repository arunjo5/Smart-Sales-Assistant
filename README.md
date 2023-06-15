# Smart-Sales-Assistant
Raspberry Pi can be used to build a voice assistant on custom data by using ChatGPT and Whisper APIs from OpenAI. 

Hardware components:
Raspberry Pi, Micro SD Card, Power Supply, USB Speaker, USB Microphone

Recommended for initial setup:
USB Mouse, USB Keyboard, HDMI Cable, Monitor

Software Apps: Python, ChatGPT, Whisper, Speech Recognition, Pysttx3 libraries

Raspberry pi operating system needs to be installed on a micro SD card before installing any ChatGPT based libraries. Raspberry Pi Imager (scroll down from the website https://www.raspberrypi.com/software/) running on another computer can be used to copy the operating system into the SD card.

<img width="327" alt="Screen Shot 2023-06-15 at 4 17 36 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/1adc0604-9bd4-4b18-bdf5-2250525f5baa">

Click on 'CHOOSE OS' button and select Raspberry Pi OS (64-bit) option and select 'WRITE' button to install the operating system on the SD card.

<img width="328" alt="Screen Shot 2023-06-15 at 4 18 04 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/46c71fb5-05ca-45bd-8ac1-f7c8e82c8c1e">

After installing Raspberry pi os on SD card, it can be inserted into Raspberry pi and connect to Monitor and keyboard for installing the required voice assistant integrations. First setup username and password.

<img width="322" alt="Screen Shot 2023-06-15 at 4 18 28 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/507a6d00-2917-46ab-928a-bc13bf84878f">

Select Preferences -> Raspberry Pi Configuration.

<img width="455" alt="Screen Shot 2023-06-15 at 4 18 39 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/d4bcd894-f34c-4900-923c-34c14ace5c96">

Click on the Interfaces tab and select SSH and VNC. These options will enable you to access Raspberry pi remotely using SSH or VNC.

<img width="409" alt="Screen Shot 2023-06-15 at 4 18 56 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/4a181476-df20-4192-9eb6-6b17b140a671">

Advanced configurations can be set using raspi-config comand on the Terminal.

`sudo raspi-config`

Select System -> Audio -> USB Audio
<img width="417" alt="Screen Shot 2023-06-15 at 4 20 23 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/11fb1f77-2185-477c-8983-b3fb3ee120d4">

<img width="426" alt="Screen Shot 2023-06-15 at 4 20 35 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/b5786e49-71de-4871-8ab0-2ee39d33f65e">

<img width="437" alt="Screen Shot 2023-06-15 at 4 20 47 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/ffa38a42-ed98-4d9d-b483-0839b64e44b7">

Sound settings can be modified using alsamixer command on the Termial.

<img width="391" alt="Screen Shot 2023-06-15 at 4 21 03 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/a2cf04ec-e354-40a9-9b71-901d9a4a92fe">

Install openai library and then install gpt_index which is also known as LlamaIndex (GPT Index) is a project that provides a central interface to connect your LLM's with external data. Install PyPDF2 library which can be used for processing PDF files.

`pip install openai==0.27.4`

`pip install gpt_index==0.4.24`

`pip install PyPDF2`

Install longchain library which is a framework for developing applications powered by language models. Also install tiktokpn, a tokenizer library and PyCryptodome which provides encryption and decryption algorithms.

`pip install langchain==0.0.132`

`pip install PyCryptodome`

`pip install tiktoken==0.3.3`

`sudo apt-get install libasound-dev`

`sudo apt-get install portaudio19-dev`

`pip install PyAudio`

Install epseak, speechRecoginition and text to speech library (pyttsx3) libraries.

`sudo apt-get install espeak`

`pip install SpeechRecognition`

`pip install pyttsx3`

Now, to train and create an AI chatbot based on a custom knowledge base, we need to get an API key from OpenAI. The API key will allow you to use OpenAI’s model as the LLM to study your custom data and draw inferences.

The Chat GPT library needs to be configured with an account's secret key which is available on the website. Set the api key OPENAI_API_KEY. This API key let you  use OpenAI’s model as the LLM for any  custom data and draw inferences.

`os.environ["OPENAI_API_KEY"] = 'YOUR API KEY'`

Copy the custom data documents on a specific directory on Raspberry pi. e.g., /home/pi/Documents

<img width="396" alt="Screen Shot 2023-06-15 at 4 25 48 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/3459c9f0-073f-489f-bf7f-4ae46e2cff13">

Run voice_assistant.py and the code should work!



