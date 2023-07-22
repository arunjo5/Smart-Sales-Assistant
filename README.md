# Smart-Sales-Assistant
Raspberry Pi can be used to build a voice assistant on custom data by using ChatGPT and Whisper APIs from OpenAI. 

<img width="300" alt="Screen Shot 2023-07-22 at 4 24 21 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/4d07d64f-35b5-46a0-886c-18d41d39a79a">

Hardware components:
Raspberry Pi, Micro SD Card, Power Supply, USB Speaker, USB Microphone

Recommended for initial setup:
USB Mouse, USB Keyboard, HDMI Cable, Monitor

Software Apps: Python, ChatGPT, Whisper, Speech Recognition, Pysttx3 libraries

Raspberry pi operating system needs to be installed on a micro SD card before installing any ChatGPT based libraries. Raspberry Pi Imager (scroll down from the website https://www.raspberrypi.com/software/) running on another computer can be used to copy the operating system into the SD card.

<img width="400" alt="Screen Shot 2023-07-22 at 4 18 32 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/f9145019-8340-44ac-8ee4-fb6b677a5019">

Click on 'CHOOSE OS' button and select Raspberry Pi OS (64-bit) option and select 'WRITE' button to install the operating system on the SD card.

<img width="400" alt="Screen Shot 2023-07-22 at 4 19 57 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/08e99e6f-cc39-41ca-b7a8-3c230007cab9">

After installing Raspberry pi os on SD card, it can be inserted into Raspberry pi and connect to Monitor and keyboard for installing the required voice assistant integrations. First setup username and password.

<img width="400" alt="Screen Shot 2023-07-22 at 4 20 30 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/72a950b6-5a05-4c17-a812-0db222e73306">

<img width="400" alt="Screen Shot 2023-07-22 at 4 20 52 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/3696bd6b-595a-4fce-b55b-6c7af7f0f877">

Select Preferences -> Raspberry Pi Configuration.

<img width="400" alt="Screen Shot 2023-07-22 at 4 21 14 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/6a032fee-f750-4cc3-8f7b-49118776a2ab">

Click on the Interfaces tab and select SSH and VNC. These options will enable you to access Raspberry pi remotely using SSH or VNC.

<img width="400" alt="Screen Shot 2023-07-22 at 4 21 27 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/55106555-6dea-49a0-b0aa-64bd7c45c94a">

Advanced configurations can be set using raspi-config comand on the Terminal.

`sudo raspi-config`

Select System -> Audio -> USB Audio

<img width="400" alt="Screen Shot 2023-07-22 at 4 21 49 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/df705bc0-7c66-4c54-8449-101dad87e299">

<img width="400" alt="Screen Shot 2023-07-22 at 4 22 06 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/6556e44a-2457-4109-9a2c-1bc5282a6988">

<img width="300" alt="Screen Shot 2023-07-22 at 4 22 21 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/de88fdb2-93da-4342-a37c-2b497d2a1750">


Sound settings can be modified using alsamixer command on the Termial.

<img width="400" alt="Screen Shot 2023-07-22 at 4 22 53 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/8127cba2-4173-4263-8a64-70a705bdd361">


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

<img width="400" alt="Screen Shot 2023-07-22 at 4 23 43 PM" src="https://github.com/arunjo5/Smart-Sales-Assistant/assets/136642643/5cc3c237-68fa-43bf-a6f4-4d061d80dbf6">

Run voice_assistant.py and the code should work!



