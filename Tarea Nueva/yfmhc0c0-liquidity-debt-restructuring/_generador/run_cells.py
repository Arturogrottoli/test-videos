"""Ejecuta cells.py celda por celda en una carpeta de trabajo, como Colab.
Uso: python run_cells.py <cells.py> <carpeta_con_csv>
"""
import ast, os, sys
import matplotlib
matplotlib.use("Agg")
import pandas as pd
pd.set_option("display.width", 200); pd.set_option("display.max_columns", 30); pd.set_option("display.max_rows", 60)
src = open(sys.argv[1], encoding="utf-8").read()
os.chdir(sys.argv[2])
g = {}
for chunk in src.split("# %% ")[1:]:
    num, code = chunk.split("\n", 1)
    print(f"\n===== CELL {num.strip()} ({len(code.strip())} chars) =====")
    tree = ast.parse(code)
    last = tree.body[-1] if tree.body and isinstance(tree.body[-1], ast.Expr) else None
    if last:
        tree.body = tree.body[:-1]
    exec(compile(tree, "cell", "exec"), g)
    if last:
        val = eval(compile(ast.Expression(last.value), "cell", "eval"), g)
        if val is not None and not hasattr(val, "figure"):
            print(val)
        elif hasattr(val, "figure"):
            val.figure.savefig("chart.png")
