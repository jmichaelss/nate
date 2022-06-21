<h1 align="center">Nate Backend Challenge</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/jmichaelss/nate?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/jmichaelss/nate?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/jmichaelss/nate?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/jmichaelss/nate?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/{{YOUR_GITHUB_USERNAME}}/nate?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/{{YOUR_GITHUB_USERNAME}}/nate?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/{{YOUR_GITHUB_USERNAME}}/nate?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center">
	🚧  Nate 🚀 Under construction...  🚧
</h4>

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/{{jmichaelss}}" target="_blank">Author</a>
</p>

<br>

## :dart: About

This project is built on [FastApi](https://fastapi.tiangolo.com) and it uses the request library get Html pages and [BeautifulSoup](https://fastapi.tiangolo.com) to parse the page and extract text held within the html tags.

## :rocket: Technologies

The following tools were used in this project:

- [Python](https://www.python.org/)
- [FastApi](https://fastapi.tiangolo.com)
- [BeautifulSoup](https://fastapi.tiangolo.com)
- [Docker](https://www.docker.com/)

## :white_check_mark: Requirements

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com), [Python](https://www.python.org/), and [Docker](https://www.docker.com/) installed.

## :checkered_flag: Starting

```bash
# Clone this project
$ git clone https://github.com/jmichaelss/nate

# Access
$ cd nate/src

# Build docker image
$ docker build -t imagename .

# Run the project
$ docker run -d --name containername -p 8000:8000 imagename

# Test the project
$ docker exec containername pytest .

# Generate pytest coverage reports
$ docker exec mycontainer pytest --cov=app .

# The server will initialize at <http://localhost:8000>
# The API documentation for end users can be at <http://localhost:8000/docs>
```

## :ledger: Reasoning and Observations

- FastApi was becuase of its quick turn-around time and the performance edge it has over frameworks like Django and react. Based on the project specification, BeautifulSoup seemed like a better option in terms of simplicity when compared options like to scrapy or selenium. Pytest was used for testing

- To tackle the question about scalability, the first thing to do would be to profile the code and write more efficient code where necessary. In terms of BeautifulSoup, could switch from BeautifulSoup's synchronous approach to an asynchronous approach. Scrapy could be a better alternative in that sense.

## :memo: License

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.

Made with :heart: by <a href="https://github.com/jmichaelss/" target="_blank">Joel Michaels</a>

&#xa0;

<a href="#top">Back to top</a>
