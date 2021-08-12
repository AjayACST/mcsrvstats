# mc-server-stats
<p align="center">
  <a href="https://obsidion-dev.com">
    <img alt="Obsidion-dev" src="https://discord.obsidion-dev.com/img/Bot%20Profile.png" width="60" />
  </a>
</p>
<h1 align="center">
  Mcsrvstats
</h1>

<h3 align="center">
  Easily access Statistcs from Minecraft Servers
</h3>
<p align="center">
  Mcsrvstats is an open source asynchronous python lots of Minecraft servers including, manacube, wyncraft, veltpvp and more.
</p>

<h3 align="center">
 🤖 🎨 🚀
</h3>

<p align="center">
  <a href="https://github.com/Obsidion-dev/mcsrvstats/releases">
    <img alt="GitHub all releases" src="https://img.shields.io/github/downloads/Obsidion-dev/mcsrvstats/total">
  </a>
  <a href="https://github.com/Obsidion-dev/mcsrvstats/releases">
    <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/Obsidion-dev/mcsrvstats">
  </a>
  <a href="https://github.com/Obsidion-dev/mcsrvstats/actions?workflow=Tests">
  <img src="https://github.com/Obsidion-dev/mcsrvstats/workflows/Tests/badge.svg" alt="Test status" />
  </a>
  <a href="https://discord.gg/rnAtymZnzH">
    <img alt="Discord" src="https://img.shields.io/discord/695008516590534758">
  </a href="#contributors-">
   <img src="https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg" alt="Code of conduct" />
</p>

<h3 align="center">
  <a href="https://mcsrvstats.readthedocs.io/">Docs</a>
  <span> · </span>
  <a href="https://github.com/Obsidion-dev/mcsrvstats/discussions?discussions_q=category%3AIdeas">Feature request</a>
  <span> · </span>
  <a href="https://github.com/Obsidion-dev/mcsrvstats/issues">Report a bug</a>
  <span> · </span>
  Support: <a href="https://github.com/Obsidion-dev/mcsrvstats/discussions">Discussions</a>
  <span> & </span>
  <a href="https://discord.gg/fWxtKFVmaW">Discord</a>
</h3>

## ✨ Features

- **Asyncronous.** Unlike other libraries Mcsrvstats is fully asynchronous. This makes it perfect to use in your next discord bot or powerful website without having to worry about blocking.

- **Pydantic models.** All models are checked and validated by [Pydantic](https://github.com/samuelcolvin/pydantic) meaning that the data is always in the correct format perfect for you to use.

- **Available on pypi.** Mcsrvstats is available on pypi meaning no building from source, just use `pip install mcsrvstats` to use it in your project.

## 🏁 Getting Started with Mcsrvstats

To get started check out the documentation which [lives here](https://mcsrvstats.readthedocs.io/) and is generously hosted by readthedocs.

### Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) or your favourite tool to install mcsrvstats.

```bash
pip install mcsrvstats
```

### Example

```python
import mcsrvstats
import asyncio

async def main():
  client = mcsrvstats.Client()
  data = await client.wyncraft("IceWarox")
  print(data.classes[0].class_name)
  await client.close()


asyncio.run(main())
```

## ❗ Code of Conduct

Obsidion-dev is dedicated to providing a welcoming, diverse, and harassment-free experience for everyone. We expect everyone in the Obsidion-dev community to abide by our [**Code of Conduct**](https://github.com/Obsidion-dev/mcsrvstats/blob/main/CODE_OF_CONDUCT.md). Please read it.

## 🙌 Contributing to Mcsrvstats

From opening a bug report to creating a pull request: every contribution is appreciated and welcomed. If you are planning to implement a new feature or change the library please create an issue first. This way we can ensure your work is not in vain.

### Not Sure Where to Start?

A good place to start contributing, are the [Good first issues](https://github.com/Obsidion-dev/mcsrvstats/labels/good%20first%20issue).

## 📝 License

Mcsrvstats is open-source. The library is licensed [GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html).

## 💬 Get in touch

If you have a question or would like to talk with other Asyncpixel users, please hop over to [Github discussions](https://github.com/Obsidion-dev/mcsrvstats/discussions) or join our Discord server:

[Discord chatroom](https://discord.gg/rnAtymZnzH)

![Discord Shield](https://discordapp.com/api/guilds/695008516590534758/widget.png?style=shield)

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://quirky.codes/"><img src="https://avatars2.githubusercontent.com/u/35202521?v=4?s=100" width="100px;" alt=""/><br /><sub><b>AjayACST</b></sub></a><br /><a href="#maintenance-AjayACST" title="Maintenance">🚧 💻 🐛</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!
