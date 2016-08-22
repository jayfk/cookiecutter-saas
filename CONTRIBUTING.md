# How to Contribute

## Getting your pull request merged in

- Please create an issue prior to submitting a pull request.
- Keep it small. The smaller the pull request the more likely I'll pull it in.
- If you're not already in the `CONTRIBUTORS.rst` file, add yourself!

## Testing

### Installation

Please install the requirements in `requirement.txt`. You'll also need a working docker and docker-compose installation on your machine.

### Run the Tests

Run:

    py.test tests --capture=sys
