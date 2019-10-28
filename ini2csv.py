import click
import configparser
import csv


def collapse_output(config, csv_file):
    fieldnames = ["header", "indent_style", "indent_size"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for section in config.sections():
        output = {"header": section}
        for k in config[section]:
            output[k] = config[section][k]
        writer.writerow(output)


@click.command()
@click.argument("ini_file")
@click.argument("csv_file", type=click.File("w"))
@click.option("--collapsed", default=False, help="Collapse CSV output", is_flag=True)
def convert(ini_file, csv_file, collapsed):
    """Convert INI to CSV format"""

    config = configparser.ConfigParser()
    config.read(ini_file)
    if collapsed:
        collapse_output(config, csv_file)
        return
    for section in config.sections():
        for k in config[section]:
            csv_file.write(f"{section},{k},{config[section][k]}\n")


if __name__ == "__main__":
    convert()
