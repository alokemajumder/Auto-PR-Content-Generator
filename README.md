

![GitHub stars](https://img.shields.io/github/stars/alokemajumder/Auto-PR-Content-Generator?style=social)
![GitHub forks](https://img.shields.io/github/forks/alokemajumder/Auto-PR-Content-Generator?style=social)
![GitHub issues](https://img.shields.io/github/issues/alokemajumder/Auto-PR-Content-Generator)
![GitHub pull requests](https://img.shields.io/github/issues-pr/alokemajumder/Auto-PR-Content-Generator)
![GitHub](https://img.shields.io/github/license/alokemajumder/Auto-PR-Content-Generator)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/alokemajumder/Auto-PR-Content-Generator)
![GitHub contributors](https://img.shields.io/github/contributors/alokemajumder/Auto-PR-Content-Generator)
![GitHub last commit](https://img.shields.io/github/last-commit/alokemajumder/Auto-PR-Content-Generator)
![GitHub top language](https://img.shields.io/github/languages/top/alokemajumder/Auto-PR-Content-Generator)
![Dependencies](https://img.shields.io/librariesio/github/alokemajumder/Auto-PR-Content-Generator)
![Code size](https://img.shields.io/github/languages/code-size/alokemajumder/Auto-PR-Content-Generator)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)


# Auto PR Content Generator

This GitHub Action uses AI models from OpenAI and Anthropic's Claude 3, and Gemini to automatically generate formatted and insightful content for pull requests based on code changes. It is designed to streamline the PR review process by providing detailed summaries and insights.


## Features

- Automated PR content generation using AI models.
- Supports OpenAI (GPT-3.5) and Gemini for code summaries.
- Manually triggered workflows to avoid unnecessary runs in the development repository.
- Customizable for different AI platforms and integration.

## Getting Started

### Prerequisites

Before you can use this GitHub Action, you need:
- A GitHub account.
- Administrative access to a repository.
- API keys for OpenAI, Anthropic (Claude 3), and Gemini added to your repository's secrets.


### Setup Instructions

1. **Fork or Clone This Repository**
   - Fork this repository to your GitHub account or clone it directly to your local machine.

2. **Configure GitHub Secrets**
   - Go to your repository settings, navigate to 'Secrets', and add your `OPENAI_API_KEY`, `GEMINI_API_KEY`, and `ANTHROPIC_API_KEY`.

3. **Enable GitHub Actions**
   - Ensure that GitHub Actions is enabled for your repository.

## Usage

### Triggering the Actioin
1. Automatically on Pull Requests:
   - The action will automatically run when a pull request is created, reopened, or synchronized.

2. Manually (using workflow_dispatch):
   - You can manually trigger the workflow using the `workflow_dispatch` option. This allows you to specify the base branch, head branch, and the AI provider you wish to use (OpenAI, Anthropic, or Gemini).

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Check out our [contributing guidelines](CONTRIBUTING.md) for more information on how to report bugs, suggest enhancements, and submit pull requests.

## License

Distributed under the MIT License. See `LICENSE` for more information.
