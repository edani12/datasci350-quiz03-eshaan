# DATASCI 350 - Quiz 03 (Eshaan Dani)

## AI-Assisted Programming, Local LLMs, and Cloud Computing

In this quiz, you will need to complete two activities. The first involves creating a custom language model using [Ollama](https://ollama.com/). The second involves data analysis in Python using [AWS EC2](https://aws.amazon.com/ec2/). Both tasks relate to content covered in lectures 11, 13, 14, and 15.

As we have done in previous quizzes, answers must be in a fork of the quiz repository, whose link you should submit on Canvas.

**Screenshots will not be accepted.** Files and directories uploaded via the GitHub website (without using the terminal) will have points deducted.

## Activity 1: Creating a Custom Language Model with Ollama

In this first part of the quiz, you will create a chatbot called `conspiracy` that responds to user questions as a paranoid conspiracy theorist. The chatbot should be:

- Paranoid and suspicious of everything, especially technology and governments
- Provides technically correct answers but wraps them in conspiracy theories
- Frequently references "they" and "the powers that be" as controlling forces
- Uses phrases like "wake up", "open your eyes", "follow the money"
- Capable of handling a wide range of topics with a conspiratorial lens
- Blames every technical error on "the algorithm" or "the system"
- **Must always include at least one whispered aside in parentheses in every response**, e.g., "(they're watching)" or "(don't tell anyone I told you this)"

1. Fork this repository and clone your fork to your local machine
2. Create a directory called `ollama`. Inside the `ollama` directory, create a file called `Modelfile` and another called `ollama.md`
3. Install the base model `llama3.2:1b` using Ollama. **You must use this specific model**
4. Create a Modelfile containing:
   - A `FROM` statement specifying `llama3.2:1b`
   - Three `PARAMETER` lines: `temperature`, `top_k`, and `top_p`. Choose values that suit the personality
   - A detailed `SYSTEM` prompt describing the chatbot's personality and behaviour, including the requirement to always include a whispered aside in parentheses
5. Create the chatbot using the `Modelfile`
6. Test the chatbot. Verify it handles various topics with the appropriate conspiratorial tone and always includes whispered asides
7. In `ollama.md`, document:
   - Commands used in the process
   - Three example prompts with the model's responses
8. Add, commit, and push your changes to your forked repository

## Activity 2: Data Analysis with Python on AWS EC2

In this second part, you will use AWS EC2 to perform Python data analysis on streaming platform data. The script `streaming_analysis.py` analyses `streaming_data.txt` (a fictional 30-day streaming platform dataset). Both are available in the `aws` directory of this repository. The script:

- Calculates basic statistics like total hours watched, subscriber growth, and churn rates.
- Creates a visualisation showing streaming trends and genre popularity over the 30-day period.
- Saves the plot as `streaming_analysis.png`.

1. Log into your AWS account and create an EC2 instance with:
   - Ubuntu Server 24.04 LTS
   - SSD Volume Type
   - t2.micro or t3.micro instance type (whichever is free tier eligible)
2. Create an SSH key pair (`.pem`) or use an existing one. Ensure the key pair has the correct permissions with `chmod`
3. Configure security groups to allow SSH access
4. Allocate at least 10GB disk space (but less than 30GB) for the instance
5. Connect to the instance using `ssh -i <key.pem> ubuntu@<public-ip>`
6. Update and upgrade system packages with `apt`
7. Install required packages: `pandas`, `matplotlib`, `numpy`, and `seaborn`
8. From your local terminal, upload the files `streaming_analysis.py` and `streaming_data.txt` to the EC2 instance
9. Run the script `streaming_analysis.py` on the EC2 instance using Python
10. Run the command `cat /etc/os-release > os.txt` on the instance
11. From your local terminal, download the `os.txt` and `streaming_analysis.png` files to the `aws` directory on your machine
12. **Terminate the EC2 instance** to avoid charges and **do not include the .pem file in your repository**. The `.pem` file is sensitive and should never be shared publicly
13. Add, commit, and push your changes
14. Submit your repository link on Canvas

**Good luck!** 😃
