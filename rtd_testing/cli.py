"""Console script for rtd-testing."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for rtd-testing."""
    click.echo("Replace this message by putting your code into "
               "rtd_testing.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
