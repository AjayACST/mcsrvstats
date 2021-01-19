Welcome to asyncpixel's documentation!
======================================

Asyncpixel is an asyncronous python wrapper for the Hypixel api with 100% coverage.

.. warning::

  Asyncpixel just released version 1 which has major breaking changes please refer to the docs for the new api.

Requirements
------------

- Python 3.8+
- Pydantic
- Aiohttp

Installation
------------

To install Asyncpixel,
run this command in your terminal or use your favourite package manager:

.. code-block:: console

   $ pip install asyncpixel

Basic Example
-------------

.. code-block:: python

   import asyncpixel
   import asyncio

   async def main():
      hypixel = asyncpixel.Hypixel("hypixel_api_key")
      profile = await hypixel.profile("405dcf08b80f4e23b97d943ad93d14fd")
      print(profile)
      await hypixel.close()


   asyncio.run(main())

.. _Contributor Guide: contributing.html

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   reference
   contributing
   codeofconduct
   license
