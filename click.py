import click

@click.command()
@click.option('--count', default=1)
@click.argument('name')
def hello(count, name):
  for x in range(count):
      print(f"Hello {name}!")
      
if __name__ == '__main__':
    hello()
