import pandas as pd
from rich import print
from rich.console import Console
from rich.table import Table
pd.options.mode.chained_assignment = None


df = pd.read_excel('./DATABASE.xlsx')


class Check_Report:

    def Fair_Share():
        while (True):
            date = input('Enter Date (yyyy-mm) eg. 2020-01 -> ').lower()
            if date == 'q':
                print('[cyan]Well done![/cyan]')
                break
            else:
                try:
                    df_date = df[df['month'] == date]
                    df_pivot = df_date.pivot(index = 'category', columns = 'month', values = ['brand_sales', 'cate_sales'])
                    df_pivot['market_share'] = (df_pivot['brand_sales'][date]) / (df_pivot['cate_sales'][date])
                    sum_pct_share = (df_pivot['brand_sales'][date].sum()) / (df_pivot['cate_sales'][date].sum())
                    df_pivot['diff_share'] = sum_pct_share - df_pivot['market_share']
                    diff_share_positive = df_pivot[df_pivot['diff_share'] > 0]
                    diff_share_positive['sum_share'] = (diff_share_positive['brand_sales'][date]) * diff_share_positive['diff_share']
                    fair_share = diff_share_positive['sum_share'].sum().round(2)
                    fair_share = str(fair_share)
                    table = Table(title='[bold][yellow]Check Report[/yellow][/bold]', style='cyan')
                    table.add_column('[yellow]Date[/yellow]', justify = 'right', style = 'green')
                    table.add_column('[yellow]Fair Share[/yellow]', justify = 'right', style = 'green')
                    table.add_row(date, fair_share)
                    console = Console()
                    console.print(table)
                except:
                    print('[red]Try again[/red]')
                print('[cyan]Enter "[red]Q[/red]" to [red]quit[/red][/cyan]')


Check_Report.Fair_Share()
