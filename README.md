# Guess-The-Capital, an OpenAI web application
- Guess-The-Capital is a streamlit web application developed in python utilizing OpenAI's GPT API to send prompts and receive completions.
- A random country name to be generated is sent as a prompt and the completion is displayed to the user to guess the capital of the country.
- The input for the capital is retrieved from a text input element and verified for correctness through another prompt.
- The completion for the above prompt would either be a "yes" or "no" followed by an explanation.
- A positive score is awarded if the player/user has guessed it correct, else a negative score or 0 is awarded.
- The player with the highest score will be the winner.
- Number of guesses for a country's capital is limited to one at the moment.

**NOTE :** Please do remember since the application uses the free-trial version of the OpenAI service, the no.of requests per minute (RPM) is limited to 3. Please find the link below on rate limits for more information.


# Links
1. [OpenAI API rate limits](https://platform.openai.com/docs/guides/rate-limits/overview)

# Task lists
- [ ] Increase the guess count to 3 per country.
- [ ] Display a countdown timer for 1 minute when RPM is exhausted.
