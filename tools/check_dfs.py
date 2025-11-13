import sys, os, pprint
sys.path.append(r'c:\Users\lovan\OneDrive\Desktop\Code_genie_1')
from backend.admin_dashboard_module import get_dashboard_stats
import pandas as pd

stats = get_dashboard_stats()
pp = pprint.PrettyPrinter(indent=2)
print('language_stats:')
pp.pprint(stats.get('language_stats'))
lang_stats = stats.get('language_stats', {})
if lang_stats:
    df_lang = pd.DataFrame(list(lang_stats.items()), columns=['Language', 'Count'])
    print('\ndf_lang:')
    print(df_lang)
    print('\ndf_lang.set_index:\n', df_lang.set_index('Language'))

print('\ncode_quality:')
pp.pprint(stats.get('code_quality'))

cq = stats.get('code_quality', {})
runtime = cq.get('runtime', {})
print('\nruntime:')
pp.pprint(runtime)
if runtime:
    df_runtime = pd.DataFrame(list(runtime.items()), columns=['Category', 'Count']).set_index('Category')
    print('\ndf_runtime:')
    print(df_runtime)

syntax = cq.get('syntax', {})
print('\nsyntax:')
pp.pprint(syntax)
py_checked = syntax.get('python_checked', 0)
py_ok = syntax.get('python_syntax_ok', 0)
py_not_ok = max(0, py_checked - py_ok)
pie_labels = ['OK', 'Syntax Error', 'Not Checked']
pie_vals = [py_ok, py_not_ok, max(0, stats.get('total_queries', 0) - py_checked)]
print('\npie_vals:', pie_vals)
if __name__ == '__main__':
    print('\n--- done ---')
