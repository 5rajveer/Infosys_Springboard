import pprint
import sys, os
sys.path.append(r'c:\Users\lovan\OneDrive\Desktop\Code_genie_1')
from backend.admin_dashboard_module import get_dashboard_stats
stats = get_dashboard_stats()
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(stats)
print('\n--- done ---')
