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
  ███    ███                                                                      `'ｰ----‐´ l 
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
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#basic-usage">Basic usage</a></li>
        <li><a href="#powerful-usage">Powerful usage</a></li>
      </ul>
    </li>
    <li><a href="#options">Options</a></li>
    <li><a href="#keybinds">Keybinds</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

When you write a git commit comment, do you find it bothersome to associate it with a Redmine ticket? But it's okay! With REDMAN, you can search for Redmine tickets while you are in the terminal.  

Here's why:  
* You should always be in the terminal during development. You should not open web pages other than developments. Well, I sometimes google, but ne.
* The more productive you are, the more tickets you will be assigned. There is even more potential for streamlining operations.

REDMAN will dramatically change your Redmine life.

<!-- GETTING STARTED -->
## Getting Started

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
![redman projects](assets/images/redman_projects.png)

- ```redman users```
![redman users](assets/images/redman_users.png)

- ```redman issues```
![redman issues](assets/images/redman_issues.png)

#### Query

### Powerful usage
![command chain](assets/videos/redman.gif)
```command chain```
If you press enter to select it, it will be automatically set in the issues query.  
```history```
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
[product-screenshot]: assets/images/redman.png
