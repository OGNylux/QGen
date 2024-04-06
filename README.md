# QGen

QGen is an app that helps you create quests or entire questlines for the Minecraft Bedrock Edition. Simply fill out the form, click generate and follow the intructions to get fully working quests in your game!

## Prerequisites

- [Node.js](https://nodejs.org/de) (>= 18.0.0)
- [Python](https://www.python.org/) (>= 3.12)

## Developing

Once you've cloned the project and install the dependencies:

NPM:

```bash
npm install
```

Python:

```bash
pip install -r requirements.txt
```

And start a development server:

NPM:

```bash
npm run dev
```

Python:

```bash
python app.py
```

## Building

### NPM

To create a production version of the app:

```bash
npm run build
```

(preview the production build with `npm run preview`.)

### Docker

**Swap the database connection in app.py.**

To create a production version of the app:

```bash
docker-compose build
```

Start the docker:

```bash
docker-compose up -d
```
