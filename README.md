# Vibe Shuffle

*Yet another revolutionary library that will definitely change your life forever.*

## What is this masterpiece?

Congratulations! You've stumbled upon Vibe Shuffle, the library you never knew you desperately needed. Because apparently, the world was missing just one more shuffling algorithm.

## Installation

```bash
pip install vibe-shuffle
```

*Wow, such complexity. Much difficult.*

## Adding environment
You can set the environment variable `DEFAULT_VIBE_SHUFFLE_METHOD` to choose your preferred shuffling method.

All available methods are:
- `deepseek` - Uses the DeepSeek API for shuffling.
- `openai` - Uses the OpenAI API for shuffling.

**Command Prompt:**
```cmd
set DEFAULT_VIBE_SHUFFLE_METHOD=deepseek
```

**PowerShell:**
```powershell
$env:DEFAULT_VIBE_SHUFFLE_METHOD="deepseek"
```

If you choose to use the DeepSeek API for shuffling please set the environment variable `DEEPSEEK_API_KEY` and the environment variable `DEEPSEEK_API_BASE_URL` to your environment.

**Command Prompt:**
```cmd
set DEEPSEEK_API_KEY=your_deepseek_api_key_here
set DEEPSEEK_API_BASE_URL=https://api.deepseek.com/v1
```

**PowerShell:**
```powershell
$env:DEEPSEEK_API_KEY="your_deepseek_api_key_here"
$env:DEEPSEEK_API_BASE_URL="https://api.deepseek.com/v1"
```

## Usage

```python
from vibe_shuffle import shuffle

my_list = [1, 2, 3, 4, 5]
shuffled = shuffle(my_list)
print(shuffled)  # Mind = blown
```

## Features

- ✨ Shuffles lists (groundbreaking innovation)
- 🐍 Works with Python (revolutionary concept)
- 🚀 Returns shuffled lists (who would have thought?)
- 📦 Comes in a neat little package (fancy!)

## API

### `shuffle(list)`

Takes a list and shuffles it. Returns a shuffled list. 

*Rocket science, really.*

## Contributing

Feel free to contribute to this world-changing project. We're sure the internet desperately needs your input on yet another shuffling library.

## License

MIT - Because sharing is caring, apparently.
