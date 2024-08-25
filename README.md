# Audio Transcription Tool

This tool is designed to convert audio files to text using Google's speech recognition API. It supports various audio formats by converting them to WAV format before transcription. This project is ideal for quickly transcribing lectures, interviews, or any audio content into text.

## Getting Started

### Prerequisites

Before you can use this tool, you need to have Python installed on your system. Additionally, you'll need to set up a virtual environment and install the required dependencies.

1. **Python**: Ensure you have Python installed. You can download it from python.org.

2. **Virtual Environment**: It's recommended to use a virtual environment for Python projects. You can create one by running:

```sh
python3 -m venv venv
```

Activate the virtual environment:

- On Windows:
    ```sh
    .\venv\Scripts\activate
    ```

- On Unix or MacOS:
    ```sh
    source venv/bin/activate
    ```

3. **Install Dependencies**: Install the required Python packages using:
    ```sh
    pip install -r requirements.txt
    ```

### Installation

Clone this repository to your local machine using:

```sh
git clone https://github.com/FrancoisSchoeman/AudioTransciptionTool.git
```

Navigate to the cloned directory:

```sh
cd AudioTransciptionTool
```

Ensure you have followed the steps in the Prerequisites section to set up the virtual environment and install dependencies.

## Usage

To use this tool, you need to have an audio file that you want to transcribe. The tool accepts the path to the audio file as an input argument.

Run the tool using:

```sh
python main.py -i <path-to-your-audio-file>
```

Replace <path-to-your-audio-file> with the actual path to your audio file. The tool will convert the audio to WAV format (if necessary), transcribe it, and print the transcription to the console.

## Example

```sh
python main.py -i recordings/hello_world.mp3
```

Will output:

```
Transcription:
hello world
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions or encounter any problems.

License

This project is licensed under the MIT License - see the LICENSE file for details.