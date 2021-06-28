<!-- PROJECT SHIELDS -->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
```
   ▄████████    ▄████████ ████████▄    ▄▄▄▄███▄▄▄▄      ▄████████ ███▄▄▄▄   
  ███    ███   ███    ███ ███   ▀███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███▀▀▀██▄ 
  ███    ███   ███    █▀  ███    ███ ███   ███   ███   ███    ███ ███   ███ 
 ▄███▄▄▄▄██▀  ▄███▄▄▄     ███    ███ ███   ███   ███   ███    ███ ███   ███ 
▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ███    ███ ███   ███   ███ ▀███████████ ███   ███ 
▀███████████   ███    █▄  ███    ███ ███   ███   ███   ███    ███ ███   ███     ,  λ,..,,λΨ  ,
  ███    ███   ███    ███ ███   ▄███ ███   ███   ███   ███    ███ ███   ███   ／i＼/ ・ω・ヽ|／i＼
  ███    ███   ██████████ ████████▀   ▀█   ███   █▀    ███    █▀   ▀█   █▀    ⌒⌒l::.:... ｏ⌒⌒
  ███    ███                                                                      `'ｰ---‐´l 
```

<div style="text-align: center; font-size: 24px">
REDMAN is a command line tool that manages Redmine.  
</div>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

""" TODO: Redmineとターミナルが横に並ぶ画面を撮る"""  
[![Product Name Screen Shot][product-screenshot]](https://example.com)

When you write a git commit comment, do you find it bothersome to associate it with a Redmine ticket? But it's okay! With REDMAN, you can search for Redmine tickets while you are in the terminal.  

Here's why:  
* You should always be in the terminal during development. You should not open web pages other than developments. Well, I sometimes google, but ne.
* The more productive you are, the more tickets you will be assigned. There is even more potential for streamlining operations.

REDMAN will dramatically change your Redmine life.

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

#### Command line tool
REDMAN depends on fzf. Please install fzf first.  
[installation for fzf](https://github.com/junegunn/fzf#installation)  
peco and fzy will be ne. But fzf has a cool preview.  

#### Your Redmine settings
- <your redmine url>/settings?tab=api  
✔Enable REST  
✔Enable JSONP  
- <your redmine url>/my/account  
✔Copy API Access Key  

### Installation

```pip
pip install redman
```

```
redman config
###
REDMINE_URL=<your Redmine url>
REDMINE_API_ACCESS_KEY=<your Redmine Access Key>
### this is ~/.redmanrc
```

<!-- USAGE EXAMPLES -->
## Usage
### Basic usage
- ```redman projects```
""" TODO: キャプチャ"""  

- ```redman users```
""" TODO: キャプチャ"""  

- ```redman issues```
""" TODO: キャプチャ"""  
#### Query


### Powerful usage
```command chain```
""" TODO: キャプチャ"""  
projects -> issues  
users -> issues  
If you press enter to select it, it will be automatically set in the issues query.  

```history```
""" TODO: キャプチャ"""  
If you omit the subcommand, the previous query will be executed.

## Options

## Keybinds

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[forks-shield]: https://img.shields.io/github/forks/oktntko/redman.svg?style=for-the-badge
[forks-url]: https://github.com/oktntko/redman/network/members
[stars-shield]: https://img.shields.io/github/stars/oktntko/redman.svg?style=for-the-badge
[stars-url]: https://github.com/oktntko/redman/stargazers
[issues-shield]: https://img.shields.io/github/issues/oktntko/redman.svg?style=for-the-badge
[issues-url]: https://github.com/oktntko/redman/issues
[license-shield]: https://img.shields.io/github/license/oktntko/redman.svg?style=for-the-badge
[license-url]: https://github.com/oktntko/redman/blob/master/LICENSE
[product-screenshot]: images/screenshot.png
